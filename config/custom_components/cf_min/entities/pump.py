"""Pumps control liquid flows around the communifarm."""

# from homeassistant.components.number import NumberEntity
# from homeassistant.components.switch import SwitchEntity
from homeassistant.core import HomeAssistant


class Pump:
    """pumps do liquid things."""

    def __init__(
        self, name, pwm_entity_id=None, switch_entity_id=None, voltage=None, watts=None
    ) -> None:
        """Initialize the Pump.

        :param name: Name of the pump.
        :param pwm_entity_id: Entity ID of the PWM control (LEDC) in Home Assistant.
        :param switch_entity_id: Entity ID of the on/off switch in Home Assistant.
        :param voltage: Operating voltage of the pump (e.g., 12, 24, 120).
        """
        self._name = name
        self._pwm_entity_id = pwm_entity_id
        self._switch_entity_id = switch_entity_id
        self._voltage = voltage
        self._max_watts = watts

    async def turn_on(self, hass: HomeAssistant | None):
        """Turn on the pump."""
        if self._switch_entity_id:
            await hass.services.async_call(
                "switch", "turn_on", {"entity_id": self._switch_entity_id}
            )

    async def turn_off(self, hass: HomeAssistant | None):
        """Turn off the pump."""
        if self._switch_entity_id:
            await hass.services.async_call(
                "switch", "turn_off", {"entity_id": self._switch_entity_id}
            )

    async def set_speed(self, hass: HomeAssistant | None, speed: int):
        """Set the speed of the pump.

        :param speed: Speed value (0-100).
        """
        if self._pwm_entity_id:
            # Assuming that the PWM entity is controlled through a number entity in HA
            await hass.services.async_call(
                "number",
                "set_value",
                {"entity_id": self._pwm_entity_id, "value": speed / 100.0},
            )

    def get_name(self):
        """Return the name of the pump."""
        return self._name

    def get_voltage(self):
        """Return the operating voltage of the pump."""
        return self._voltage
