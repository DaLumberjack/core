"""Class for storage and the minimal class of that."""

from abc import ABC, abstractmethod

from .entity import CommunifarmEntity


class CommunifarmStorage(CommunifarmEntity, ABC):
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
        containing: str = "nothing",
        manufacturer: list[str] = ["personal"],
        in_use: bool = False,
        description: str = "custom",
        cost: float = 0.0,
        media: str = "na",
    ) -> None:
        """Initialize the storage entity."""
        super().__init__(
            name=name,
            device_name=device_name,
            unique_id=unique_id,
            location=location,
            media_type=media_type,
            manufacturer=manufacturer,
            in_use=in_use,
            description=description,
            state="operational",
        )
        self._media_type = media_type
        self._rows = rows
        self._columns = columns
        self._row = row
        self._column = column
        self._cells = ([[False for _ in range(columns)] for _ in range(rows)] | [],)

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
