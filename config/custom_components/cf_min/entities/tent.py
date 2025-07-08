"""Tray for the communifarm."""

from helpers.db_helpers import getTableRow

from homeassistant.core import HomeAssistant

from .storage import CommunifarmStorage


class CommunifarmTent(CommunifarmStorage):
    """Tray for germinating seeds."""

    def __init__(
        self,
        name,
        device_name,
        unique_id,
        tent,
        flood_trays,
        rows,
        location,
        columns,
        growing_state,
        media_type,
        tent_row,
        sql_pk,
        hass: HomeAssistant,
    ) -> None:
        """Initialize the tray entity."""
        super().__init__(
            name=name,
            device_name=device_name,
            unique_id=unique_id,
            location=location,
            media_type=media_type,
            rows=rows,
            columns=columns,
            row=tent_row,
            column=1,  # Default to 1 for tent, can be adjusted later
            containing=tent,
            manufacturer=["personal"],
            in_use=False,
            description="custom",
        )
        self._flood_trays = flood_trays
        self._growing_state = growing_state
        self._sql_pk = sql_pk
        self._hass = hass

    @classmethod
    def from_pk(cls, pk: int, hass: HomeAssistant) -> "CommunifarmTent":
        """Create a CommunifarmTent from a primary key."""
        # Fetch the data from the database using the primary key
        tbl_name = '"table_name": "tent"'
        wr_cmd = '"where_command": "pk = {pk}"'
        data = getTableRow(
            hass=hass,
            table_name=tbl_name,
            where_command=wr_cmd.format(pk=pk),
            where_id=str(pk),
        )
        if not data or "reason" in data:
            raise ValueError(
                f"Failed to fetch tent with pk {pk}: {data.get('reason', 'Unknown error')}"
            )
        # Ensure the data contains all required fields
        return cls(
            name=data["name"],
            device_name=data["device_name"],
            unique_id=data["unique_id"],
            tent=data["tent_fk"],
            flood_trays=data["flood_trays"],
            rows=data["rows"],
            location=data["location"],
            columns=data["columns"],
            growing_state=data["growing_state"],
            media_type=data["media_type"],
            tent_row=data["tent_row_fk"],
            sql_pk=pk,
            hass=hass,
        )

    @property
    def extra_state_attributes(self):
        """Return the state attributes."""
        return {
            "location": self._location,
            "rows": self._rows,
            "columns": self._columns,
            "row": self._row,
            "column": self._column,
            "media_type": self._media_type,
            "_in_use": self._in_use,
            "_manufacturer": self._manufacturer,
            "_description": self._description,
            "cells": self._cells,
        }

    async def async_update(self):
        """Update the state of the reservoir."""
        # Here you could aggregate the states of all sensors and pumps
