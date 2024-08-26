"""Doser for communifarm component."""

from homeassistant.helpers.entity import Entity

from .devices import DoserDevice
from .reservoir import CommunifarmReservoir


class CommunifarmDoser(Entity):
    """Doser for sending nutrients and ."""

    def __init__(
        self,
        name,
        device_name,
        unique_id,
        pumps,
        doserDevice: DoserDevice,
        reservoirs: list[CommunifarmReservoir],
    ) -> None:
        """Initialize the reservoir entity."""
        self._name = name
        self._device_name = device_name
        self._unique_id = unique_id
        self._reservoirs = reservoirs
        self._pumps = pumps
        self._state = "operational"
        self._attr_device_info = doserDevice.device_info

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
        return {
            "reservoirs": [reservoir.name for reservoir in self._reservoirs],
            "pumps": [pump.name for pump in self._pumps],
        }

    async def async_update(self):
        """Update the state of the reservoir."""
        # Here you could aggregate the states of all sensors and pumps
        for reservoir in self._reservoirs:
            await reservoir.async_update()
        for pump in self._pumps:
            await pump.async_update()
