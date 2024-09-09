"""Module for handling Tower entities in Communifarm."""

from homeassistant.core import HomeAssistant

from homeassistant.helpers.entity import Entity
from ..helpers.db_helpers import updateTableRow, insertTableRow

DOMAIN = "cf_min"


class CommunifarmTower(Entity):
    """Tower for storing data about a seed."""

    def __init__(self, name, unique_id, cf_pk: str, hass: HomeAssistant) -> None:
        """Initialize the seed entity."""
        self._name = name
        self._unique_id = unique_id
        self._state = "operational"

        # Database connection
        db_connection = hass.data[DOMAIN]["db_connection"]
        cursor = db_connection.cursor()

        sql_rsp = insertTableRow(
            cursor, 
            db_connection,
            table_name="tower",
            columns={
                "name":self._name,
                "cf": cf_pk
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
    def extra_state_attributes(self):
        """Return the state attributes of the reservoir."""

    async def async_update(self):
        """Update the state of the reservoir."""
        # Here you could aggregate the states of all sensors and pumps
