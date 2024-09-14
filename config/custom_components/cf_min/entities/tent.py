"""Tray for the communifarm."""

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
        columns,
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
            tent=tent,
            state="operational",
            flood_trays=flood_trays,
            rows=rows,
            columns=columns,
            media_type=media_type,
            tent_row=tent_row,
        )

    async def async_update(self):
        """Update the state of the reservoir."""
        # Here you could aggregate the states of all sensors and pumps
