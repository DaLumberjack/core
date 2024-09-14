"""Tray for the communifarm."""

from homeassistant.helpers.entity import Entity

from .tray import CommunifarmTray
from .tower import CommunifarmTower
from ..helpers.db_helpers import updateTableRow, insertTableRow
from homeassistant.core import HomeAssistant
from homeassistant.components import tag
class CommunifarmLocation(Entity):
    """Tray for germinating seeds."""

    def __init__(
        self,
        name,
        device_name,
        unique_id,
        location_type,
        row_type,
        sql_cf_pk,
        location,
        sql_tent_pk: str | None,
        sql_tower_pk: str | None,
        hass: HomeAssistant,
        nfc_tag: tag
    ) -> None:
        """Initialize the tray entity."""
        self._name = name
        self._device_name = device_name
        self._unique_id = unique_id
        self._state = "operational"
        self._row_type = row_type
        self._location = location
        self._location_type = location_type
        self._sql_tent_pk = sql_tent_pk
        self._sql_cf_pk = sql_cf_pk
        self._sql_tower_pk = sql_tower_pk
        sql_rsp = insertTableRow(
            hass = hass,
            table_name="tent_row",
            columns={
                "name":"4",
                "nfc_tag_id": nfc_tag.TAG_ID,
                "tent_fk": sql_tent_pk,
                "cf_fk": sql_cf_pk,
            }
        )
        self._sql_pk = sql_rsp
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
    def sql_pk(self):
        """Return the pk in its db."""
        return self._sql_pk

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
