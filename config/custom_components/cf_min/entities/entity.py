"""Class for a cf base entity."""

from abc import ABC, abstractmethod

from homeassistant.helpers.entity import Entity


class CommunifarmEntity(Entity, ABC):
    """Abstract base class for entities in the Communifarm."""

    def __init__(
        self,
        name,
        short_name,
        device_name,
        unique_id,
        location,
        manufacturer: list[str] = ["personal"],
        in_use: bool = False,
        description: str = "custom",
    ) -> None:
        """Initialize the storage entity."""
        self._name = name
        self._short_name = short_name
        self._device_name = device_name
        self._unique_id = unique_id
        self._location = location
        self._manufacturer = manufacturer
        self._in_use = in_use
        self._description = description
        self._state = "operational"

    @property
    def extra_state_attributes(self):
        """Return the state attributes."""
        return {
            "location": self._location,
            "in_use": self._in_use,
            "manufacturer": self._manufacturer,
            "description": self._description,
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
