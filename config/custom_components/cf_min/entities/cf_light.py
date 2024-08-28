"""Light for communifarm component."""

from homeassistant.helpers.entity import Entity


class CommunifarmLight(Entity):
    """Light for sending nutrients and ."""

    def __init__(
        self,
        name,
        device_name,
        unique_id,
        switch,
        is_toggle: bool,
        has_adjustable_intensity: bool,
        has_adjustable_wavelengths: bool,
    ) -> None:
        """Initialize the reservoir entity."""
        self._name = name
        self._device_name = device_name
        self._unique_id = unique_id
        self._state = "operational"

    @property
    def name(self) -> any:
        """Name of the reservior."""
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
        return {}

    async def async_update(self):
        """Update the state of the reservoir."""
        # Here you could aggregate the states of all sensors and pumps
        for reservoir in self._reservoirs:
            await reservoir.async_update()
        for pump in self._pumps:
            await pump.async_update()
