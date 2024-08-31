"""Tray for the communifarm."""

from homeassistant.helpers.entity import Entity

from .seed import CommunifarmSeed


class CommunifarmTray(Entity):
    """Tray for germinating seeds."""

    def __init__(
        self,
        name,
        device_name,
        unique_id,
        seeds: list[CommunifarmSeed],
        tent,
        tray_type,
        rows,
        columns,
        media_type,
        tent_row,
    ) -> None:
        """Initialize the tray entity."""
        self._name = name
        self._device_name = device_name
        self._unique_id = unique_id
        self._tent = tent
        self._state = "operational"
        self._seeds = seeds
        self._tray_type = tray_type
        self._rows = rows
        self._columns = columns
        self._media_type = media_type
        self._tent_row = tent_row
        self.cells = [[False for _ in range(columns)] for _ in range(rows)]

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
    def extra_state_attributes(self):
        """Return the state attributes of the reservoir."""
        return {
            "tent": self._tent.name,
            "seeds": [seed.name for seed in self._seed],
        }

    async def async_update(self):
        """Update the state of the reservoir."""
        # Here you could aggregate the states of all sensors and pumps
        for reservoir in self._reservoirs:
            await reservoir.async_update()
        for pump in self._pumps:
            await pump.async_update()
