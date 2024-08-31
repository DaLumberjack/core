"""Climate for a communifarm."""

from homeassistant.components.climate import ClimateEntity


class CommunifarmClimate(ClimateEntity):
    """Representation of a Communifarm climate system."""

    def __init__(self, name, unique_id, hass, config) -> None:
        """Initialize the Communifarm climate device."""
        self._name = name
        self._unique_id = unique_id
        self._hass = hass

        # Extract config parameters
        self._circulation_fans = config.get("circulation_fans", [])
        self._intake_fans = config.get("intake_fans", [])
        self._outtake_fans = config.get("outtake_fans", [])
        self._ac_pump = config.get("ac_pump")
        self._ac_fan = config.get("ac_fan")
        self._humidifier_pump = config.get("humidifier_pump")
        self._humidifier_fan = config.get("humidifier_fan")
        self._dehumidifier = config.get("dehumidifier")
        self._sensor_array = config.get("sensor_array", [])

        # Initial state values
        self._hvac_mode = ClimateEntity.HVACMode.OFF
        self._target_temperature = 22  # Default temperature in Celsius
        self._target_humidity = 50  # Default humidity in percentage
        self._current_temperature = None
        self._current_humidity = None

    @property
    def name(self):
        """Return the name of the climate device."""
        return self._name

    @property
    def unique_id(self):
        """Return the unique ID of the climate device."""
        return self._unique_id

    @property
    def hvac_mode(self):
        """Return the current operation mode."""
        return self._hvac_mode

    @property
    def hvac_modes(self):
        """Return the list of available operation modes."""
        return [
            ClimateEntity.HVACMode.OFF,
            ClimateEntity.HVACMode.HEAT,
            ClimateEntity.HVACMode.COOL,
            ClimateEntity.HVACMode.DRY,
        ]

    @property
    def current_temperature(self):
        """Return the current temperature."""
        return self._current_temperature

    @property
    def target_temperature(self):
        """Return the temperature we try to reach."""
        return self._target_temperature

    @property
    def current_humidity(self):
        """Return the current humidity."""
        return self._current_humidity

    @property
    def target_humidity(self):
        """Return the target humidity."""
        return self._target_humidity

    @property
    def supported_features(self):
        """Return the list of supported features."""
        return self._support_flags

    async def async_set_hvac_mode(self, hvac_mode):
        """Set new target operation mode."""
        self._hvac_mode = hvac_mode

        if hvac_mode == ClimateEntity.HVACMode.OFF:
            await self.turn_off_all()
        elif hvac_mode == ClimateEntity.HVACMode.HEAT:
            await self.run_heating_cycle()
        elif hvac_mode == ClimateEntity.HVACMode.COOL:
            await self.run_cooling_cycle()
        elif hvac_mode == ClimateEntity.HVACMode.DRY:
            await self.run_dehumidification_cycle()

        self.async_write_ha_state()

    async def async_set_temperature(self, **kwargs):
        """Set new target temperature."""
        self._target_temperature = kwargs.get("temperature", self._target_temperature)
        await self.adjust_climate()
        self.async_write_ha_state()

    async def async_set_humidity(self, humidity):
        """Set new target humidity."""
        self._target_humidity = humidity
        await self.adjust_climate()
        self.async_write_ha_state()

    async def adjust_climate(self):
        """Adjust climate based on temperature and humidity targets."""
        if self._hvac_mode == ClimateEntity.HVACMode.COOL:
            await self.run_cooling_cycle()
        elif self._hvac_mode == ClimateEntity.HVACMode.HEAT:
            await self.run_heating_cycle()
        elif self._hvac_mode == ClimateEntity.HVACMode.DRY:
            await self.run_dehumidification_cycle()

    async def turn_off_all(self):
        """Turn off all fans and pumps."""
        await self.turn_off_fans(self._circulation_fans)
        await self.turn_off_fans(self._intake_fans)
        await self.turn_off_fans(self._outtake_fans)
        await self.hass.services.async_call(
            "switch", "turn_off", {"entity_id": self._ac_pump}
        )
        await self.hass.services.async_call(
            "fan", "turn_off", {"entity_id": self._ac_fan}
        )
        await self.hass.services.async_call(
            "switch", "turn_off", {"entity_id": self._humidifier_pump}
        )
        await self.hass.services.async_call(
            "fan", "turn_off", {"entity_id": self._humidifier_fan}
        )
        if self._dehumidifier:
            await self.hass.services.async_call(
                "switch", "turn_off", {"entity_id": self._dehumidifier}
            )

    async def run_heating_cycle(self):
        """Run heating cycle, primarily using circulation fans."""
        await self.turn_on_fans(self._circulation_fans)
        await self.turn_off_fans(self._intake_fans)
        await self.turn_off_fans(self._outtake_fans)
        await self.hass.services.async_call(
            "switch", "turn_off", {"entity_id": self._ac_pump}
        )
        await self.hass.services.async_call(
            "fan", "turn_off", {"entity_id": self._ac_fan}
        )

    async def run_cooling_cycle(self):
        """Run cooling cycle, utilizing AC and intake/outtake fans."""
        await self.turn_on_fans(self._intake_fans)
        await self.turn_on_fans(self._outtake_fans)
        await self.hass.services.async_call(
            "switch", "turn_on", {"entity_id": self._ac_pump}
        )
        await self.hass.services.async_call(
            "fan", "turn_on", {"entity_id": self._ac_fan}
        )

    async def run_dehumidification_cycle(self):
        """Run dehumidification cycle, using dehumidifier and fans."""
        if self._dehumidifier:
            await self.hass.services.async_call(
                "switch", "turn_on", {"entity_id": self._dehumidifier}
            )
        await self.turn_on_fans(self._outtake_fans)

    async def turn_on_fans(self, fans):
        """Turn on specified fans."""
        for fan in fans:
            await self.hass.services.async_call("fan", "turn_on", {"entity_id": fan})

    async def turn_off_fans(self, fans):
        """Turn off specified fans."""
        for fan in fans:
            await self.hass.services.async_call("fan", "turn_off", {"entity_id": fan})

    async def async_update(self):
        """Update the internal state by reading the sensor array."""
        temperatures = []
        humidities = []

        for sensor in self._sensor_array:
            state = self.hass.states.get(sensor)
            if state:
                attributes = state.attributes
                temperature = attributes.get("temperature")
                humidity = attributes.get("humidity")
                if temperature:
                    temperatures.append(temperature)
                if humidity:
                    humidities.append(humidity)

        if temperatures:
            self._current_temperature = sum(temperatures) / len(temperatures)
        if humidities:
            self._current_humidity = sum(humidities) / len(humidities)

        await self.adjust_climate()
