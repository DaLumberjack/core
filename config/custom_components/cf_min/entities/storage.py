"""Class for storage and the minimal class of that."""

from abc import ABC, abstractmethod

from homeassistant.helpers.entity import Entity


class CommunifarmStorage(Entity, ABC):
    """Abstract base class for storage entities in the Communifarm."""

    def __init__(
        self,
        name,
        device_name,
        unique_id,
        location,
        media_type,
        rows: int = 1,
        columns: int = 1,
        row: int = 1,
        column: int = 1,
        manufacturer: list[str] = "personal",
        in_use: bool = False,
        description: str = "custom",
        cost: float = 0.0,
        media: str = "na",
    ) -> None:
        """Initialize the storage entity."""
        self._name = name
        self._device_name = device_name
        self._unique_id = unique_id
        self._location = location
        self._rows = rows
        self._columns = columns
        self._row = row
        self._column = column
        self._media_type = media_type
        self._manufacturer = manufacturer
        self._in_use = in_use
        self._description = description
        self._state = "operational"
        self.cells = [[False for _ in range(columns)] for _ in range(rows)] | []

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
            "cells": self.cells,
        }

    @property
    def name(self) -> str:
        """Return the name of the storage entity."""
        return self._name

    @property
    def unique_id(self):
        """Return a unique ID for this entity."""
        return self._unique_id

    @property
    def state(self):
        """Return the current state."""
        return self._state

    @abstractmethod
    async def async_update(self):
        """Abstract method for updating the entity's state."""
