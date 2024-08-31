"""Grow Cycle for communifarm component."""

from homeassistant.components.sensor import SensorEntity

from ..sensor import DemoSensor
from .harvest import CommunifarmHarvest
from .observation import CommunifarmObservation
from .plant import CommunifarmPlant
from .sale import CommunifarmSale
from .seed import CommunifarmSeed
from .tower import CommunifarmTower
from .tray import CommunifarmTray
from .tray_cell import CommunifarmTrayCell


class CommunifarmPlantLifeCycle(SensorEntity):
    """Doser for sending nutrients and ."""

    def __init__(
        self,
        name,
        device_name,
        unique_id,
        tray: CommunifarmTray | None,
        tray_cell: CommunifarmTrayCell | None,
        tower: CommunifarmTower | None,
        plant: CommunifarmPlant | None,
        seed: CommunifarmSeed | None,
        observations: list[CommunifarmObservation] | None,
        harvest: list[CommunifarmHarvest] | None,
        sale: list[CommunifarmSale] | None,
        sensors: list[DemoSensor] | None,
    ) -> None:
        """Initialize the reservoir entity."""
        self._name = name
        self._device_name = device_name
        self._unique_id = unique_id
        self._state = "operational"

    @property
    def name(self) -> any:
        """Name of the reservior."""
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
        return {}

    async def async_update(self):
        """Update the state of the reservoir."""
        # Here you could aggregate the states of all sensors and pumps
