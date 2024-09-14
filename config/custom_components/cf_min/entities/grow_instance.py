"""Plant for communifarm component."""

from homeassistant.helpers.entity import Entity

from . import ( 
    row_location, 
    plant, 
    seed,
    tower_location,
    tray,
    tray_cell,
    tent,
    tent_row,
    tower,
    observation,
    tower_row
    )
class GrowInstance(Entity):
    """Plant for storing data about a plant."""

    def __init__(
        self,
        name,
        unique_id,
        seed: seed.CommunifarmSeed,
        plant: plant.CommunifarmPlant,
        tray_cell: tray_cell.CommunifarmTrayCell | None,
        tent: tent.CommunifarmTent | None,
        tent_row: tent_row.CommunifarmTentRow | None,
        tower: tower.CommunifarmTower | None,
        tower_location: tower_location.CommunifarmTowerLocation | None,
        observations: list[observation.CommunifarmObservation] | None,
        tower_row: tower_row.CommunifarmTowerRow | None,
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
            "row_location": self._row_location,
            "germ_env": self._germ_env,
            "grow_env": self._grow_env,
            "light": self._light,
            "special_considerations": self._special_considerations,
        }

    async def async_update(self):
        """Update the state of the reservoir."""
        # Here you could aggregate the states of all sensors and pumps
