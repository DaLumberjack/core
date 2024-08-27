"""Seed for communifarm component."""

from homeassistant.helpers.entity import Entity


class CommunifarmSeed(Entity):
    """Seed for storing data about a seed."""

    def __init__(self, name, unique_id) -> None:
        """Initialize the seed entity."""
        self._name = name
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

    async def async_update(self):
        """Update the state of the reservoir."""
        # Here you could aggregate the states of all sensors and pumps
