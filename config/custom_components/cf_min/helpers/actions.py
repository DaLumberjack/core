import logging
from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.helpers import entity_registry
from datetime import datetime

_LOGGER = logging.getLogger(__name__)

DOMAIN = "communifarm"
async def handle_plant_plant(hass: HomeAssistant, call: ServiceCall):
    """Handle the service call to plant a plant."""

    # Assume tray_id and plant_name are stored in input_text entities
    tray_id_entity = "input_text.tray_id"
    plant_name_entity = "input_text.plant_name"

    tray_id = hass.states.get(tray_id_entity).state
    plant_name = hass.states.get(plant_name_entity).state
    plant_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Get the entity registry to find the relevant tray cells
    ent_reg = entity_registry.async_get(hass)
    tray_cells = [
        entry.entity_id for entry in ent_reg.entities.values()
        if entry.entity_id.startswith(f"input_boolean.tray_{tray_id}_")
    ]

    selected_cells = [
        cell for cell in tray_cells
        if hass.states.get(cell).state == "on"
    ]

    if not selected_cells:
        _LOGGER.warning("No tray cells selected for planting.")
        return

    # Insert selected cells into the CF_plant_life_cycle table
    try:
        conn = hass.data[DOMAIN]["db_connection"]
        cursor = conn.cursor()

        for cell in selected_cells:
            # Assume the tray cell name includes row and column (e.g., tray_1_row_1_col_2)
            row_col = cell.split("_")[-2:]
            row = int(row_col[0].replace("row", ""))
            col = int(row_col[1].replace("col", ""))

            cursor.execute(
                """INSERT INTO CF_plant_life_cycle (plant_name, plant_date, location, tray_id, row, col)
                    VALUES (?, ?, ?, ?, ?, ?)""",
                (plant_name, plant_date, f"Row {row} Col {col}", tray_id, row, col)
            )

        conn.commit()
        _LOGGER.info(f"Planted {len(selected_cells)} cells with {plant_name}.")
    except Exception as e:
        _LOGGER.error(f"Error planting cells: {e}")