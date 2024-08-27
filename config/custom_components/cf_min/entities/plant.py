"""Plant for communifarm component."""

from homeassistant.helpers.entity import Entity

from .seed import CommunifarmSeed


class CommunifarmPlant(Entity):
    """Plant for storing data about a plant."""

    def __init__(
        self,
        name,
        unique_id,
        seeds: list[CommunifarmSeed],
        noots,
        germ_temp,
        grow_temp,
        germ_env: dict,
        grow_env: dict,
        light: dict,
        special_considerations: dict,
    ) -> None:
        """Initialize the reservoir entity."""
        self._name = name
        self._attr_unique_id = unique_id
        self._state = "operational"
        self._seeds = seeds
        self._ideal_noots = noots
        self._germ_temp = germ_temp
        self._grow_temp = grow_temp
        self._germ_env = germ_env
        self._grow_env = grow_env
        self._light = light
        self._special_considerations = special_considerations

    @property
    def name(self) -> any:
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
            "germ_temp": self._germ_temp,
            "grow_temp": self._grow_temp,
            "germ_env": self._germ_env,
            "grow_env": self._grow_env,
            "light": self._light,
            "special_considerations": self._special_considerations,
        }

    async def async_update(self):
        """Update the state of the reservoir."""
        # Here you could aggregate the states of all sensors and pumps
