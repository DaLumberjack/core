"""A Controlled Environment for the communifarm."""

from homeassistant.helpers.entity import Entity
from homeassistant.components.fan import FanEntity
from homeassistant.components.humidifier import HumidifierEntity
from homeassistant.components.climate import ClimateEntity
from homeassistant.components.air_quality import AirQualityEntity
from homeassistant.components.sensor import SensorEntity

from .cf_light import CommunifarmLight
from .plant import CommunifarmPlant
from .seed import CommunifarmSeed
from .tray import CommunifarmTray
from .tent import CommunifarmTent


class ControlledEnvironment(Entity):
    """Tray for germinating seeds."""

    def __init__(
        self,
        name,
        device_name,
        unique_id,
        seeds: list[CommunifarmSeed] | None,
        plants: list[CommunifarmPlant] |None,
        trays: list[CommunifarmTray] | None,
        lights: list[CommunifarmLight] | None,
        tents: list[CommunifarmTent] | None,
        fans: list[FanEntity] | None,
        humidifiers: list[HumidifierEntity] | None,
        climate: list[ClimateEntity] | None,
        air_qualities: list[AirQualityEntity] | None,
        sensors: list[SensorEntity] | None,
    ) -> None:
        """Initialize the tray entity."""
        self._name = name
        self._device_name = device_name
        self._unique_id = unique_id
        self._plants = plants
        self._state = "operational"
        self._seeds = seeds
        self._trays = trays
        self._lights = lights
        self._tents = tents
        self._fans = fans
        self._humidifiers = humidifiers
        self._climate = climate
        self._air_qualities = air_qualities
        self._sensors = sensors

    @property
    def name(self) -> str:
        """Name of the tray."""
        return self._name

    @property
    def unique_id(self):
        """Return a unique ID for this entity."""
        return self._unique_id

    @property
    def state(self):
        """Return the current state."""
        return self._state

    @property
    def extra_state_attributes(self):
        """Return the state attributes of the reservoir."""
        return {
            "tent": self._tent.name,
            "seeds": [seed.name for seed in self._seed],
        }

    async def async_update(self):
        """Update the state of the reservoir."""
        # Here you could aggregate the states of all sensors and pumps
        for reservoir in self._reservoirs:
            await reservoir.async_update()
        for pump in self._pumps:
            await pump.async_update()
