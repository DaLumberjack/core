"""Module for handling Tower location entities in Communifarm."""

from homeassistant.helpers.entity import Entity
from ..helpers.db_helpers import updateTableRow, insertTableRow
from .tower import CommunifarmTower
from homeassistant.core import HomeAssistant

class CommunifarmTowerLocation(Entity):
    """Tower location for storing data about a growth."""

    def __init__(self, name, unique_id, tower: CommunifarmTower, hass: HomeAssistant) -> None:
        """Initialize the tower location entity."""
        self._name = name
        self._unique_id = unique_id
        self._state = "operational"
        sql_rsp = insertTableRow(
            hass = hass,
            table_name="tower_location",
            columns={
                "name": self._name,
                "tower": tower._sql_pk,
            }
        )
        self._sql_pk = sql_rsp

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
    def _sql_pk(self):
        """Return the SQL pk."""
        return self._sql_pk

    @property
    def extra_state_attributes(self):
        """Return the state attributes of the reservoir."""

    async def async_update(self):
        """Update the state of the reservoir."""
        # Here you could aggregate the states of all sensors and pumps
