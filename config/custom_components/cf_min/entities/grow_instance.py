"""Plant for communifarm component."""

from homeassistant.helpers.entity import Entity

from . import plant, seed


class GrowInstance(Entity):
    """Plant for storing data about a plant."""

    def __init__(
        self,
        name,
        unique_id,
        germ_env: dict,
        grow_env: dict,
        light: dict,
        special_considerations: dict,
        unique_actions: dict,
    ) -> None:
        """Initialize the reservoir entity."""
        self._name = name
        self._attr_unique_id = unique_id
        self._state = "operational"
        self._seeds = seed
        self._ideal_noots = plant
        self._special_considerations = special_considerations
        self._unique_actions = unique_actions

    @property
    def name(self) -> str:
        """Name of the reservior."""
        return self._name

    @property
    def unique_id(self):
        """Return a unique ID for this entity."""
        return self._attr_unique_id

    @property
    def state(self):
        """Return the current state."""
        return self._state

    @property
    def extra_state_attributes(self):
        """Return the state attributes of the reservoir."""
        return {
            "seeds": self._seeds,
            "ideal_noots": self._ideal_noots,
            "special_considerations": self._special_considerations,
        }

    async def async_update(self):
        """Update the state of the reservoir."""
        # Here you could aggregate the states of all sensors and pumps
