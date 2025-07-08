"""Service actions for Communifarm integration."""

from datetime import datetime
import logging

from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.helpers import entity_registry as er

_LOGGER = logging.getLogger(__name__)

DOMAIN = "communifarm"


async def handle_plant_plant(hass: HomeAssistant, call: ServiceCall):
    """Handle the service call to plant a plant."""

    # Assume tray_id and plant_name are stored in input_text entities
    tray_id_entity = "input_text.tray_id"
    plant_name_entity = "input_text.plant_name"  # noqa: F841

    # tray_id = hass.states.get(tray_id_entity).state
    # plant_name = hass.states.get(plant_name_entity).state
    plant_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # noqa: F841

    # Get the entity registry to find the relevant tray cells
    ent_reg = er.async_get(hass)
    tray_cells = [
        entry.entity_id
        for entry in ent_reg.entities.values()
        if entry.entity_id.startswith(f"input_boolean.tray_{tray_id_entity}_")
    ]
    _LOGGER.info("Tray cells: %s", tray_cells)
