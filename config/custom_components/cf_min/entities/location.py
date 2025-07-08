"""Tray for the communifarm."""

from cf_min.helpers.db_helpers import insertTableRow
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import Entity

from .tent import CommunifarmTent


class CommunifarmLocation(Entity):
    """Location attributed to Communifarm for germinating seeds.

    This class represents a location in the Communifarm system, which can be a tent, tower, or tray. This can be empty or traverse space, that can be occupied by humans as they traverse their Entire Farm.
    Eventually this and its child classes will be the backbone of efficiency in the Communifarm system, allowing for easy identification and management of different locations within the farm.
    """

    def __init__(
        self,
        name,
        device_name,
        unique_id,
        location_type,
        row_type,
        sql_cf_pk,
        location,
        tent: CommunifarmTent | None,
        sql_tent_pk: str | None,
        sql_tower_pk: str | None,
        hass: HomeAssistant,
        # nfc_tag: tag
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
            hass=hass,
            table_name="tent_row",
            columns={
                "name": name,
                # "nfc_tag_id": nfc_tag.TAG_ID,
                "tent_fk": sql_tent_pk,
                "cf_fk": sql_cf_pk,
            },
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
            "location": self._location,
            "location_type": self._location_type,
            "row_type": self._row_type,
            "tent_pk": self._sql_tent_pk,
            "cf_pk": self._sql_cf_pk,
            "tower_pk": self._sql_tower_pk,
        }

    async def async_update(self):
        """Update the state of the reservoir."""
        # Here you could aggregate the states of all sensors and pumps
