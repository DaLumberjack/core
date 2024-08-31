"""Tray Cell for communifarm component."""

from homeassistant.helpers.entity import Entity


class CommunifarmTrayCell(Entity):
    """Tray Cell for storing data about a seed."""

    def __init__(self, tray_name, row, col, entity_id) -> None:
        """Initialize the seed entity."""
        self._tray_name = tray_name
        self._row = row
        self._col = col
        self._entity_id = entity_id
        self._state = False

    @property
    def name(self) -> any:
        """Name of the reservior."""
        return f"{self._tray_name} Row {self._row} Col {self._col}"

    @property
    def is_on(self):
        """Check if cell is on."""
        return self._state

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

    async def async_turn_on(self):
        """Turn on the cell."""
        self._state = True
        self.async_write_ha_state()

    async def async_turn_off(self):
        """Turn off the cell."""
        self._state = False
        self.async_write_ha_state()

    async def async_update(self):
        """Update the state of the reservoir."""
        # Here you could aggregate the states of all sensors and pumps
