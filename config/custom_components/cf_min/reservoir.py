"""Reservoir for communifarm component."""

from homeassistant.helpers.entity import Entity


class CommunifarmReservoir(Entity):
    """CommunifarmReservoir for maintaining sensors and pumps."""

    def __init__(self, name, unique_id, sensors, pumps) -> None:
        """Initialize the reservoir entity."""
        self._name = name
        self._unique_id = unique_id
        self._sensors = sensors
        self._pumps = pumps
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
        return {
            "sensors": [sensor.name for sensor in self._sensors],
            "pumps": [pump.name for pump in self._pumps],
        }

    async def async_update(self):
        """Update the state of the reservoir."""
        # Here you could aggregate the states of all sensors and pumps
        for sensor in self._sensors:
            await sensor.async_update()
        for pump in self._pumps:
            await pump.async_update()
