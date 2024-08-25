"""Set up the demo environment that mimics interaction with devices."""

from __future__ import annotations

import asyncio
import logging

from homeassistant import config_entries, setup
from homeassistant.components import persistent_notification
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import EVENT_HOMEASSISTANT_START, Platform, UnitOfSoundPressure
import homeassistant.core as ha
from homeassistant.core import Event, HomeAssistant
from homeassistant.helpers import config_validation as cv

# from homeassistant.helpers.discovery import async_load_platform
# from homeassistant.helpers.entity import Entity
# from homeassistant.helpers.entity_component import EntityComponent
from homeassistant.helpers.typing import ConfigType

DOMAIN = "cf_min"

COMPONENTS_WITH_CONFIG_ENTRY_DEMO_PLATFORM = [
    Platform.NUMBER,
    Platform.SELECT,
]

_LOGGER = logging.getLogger(__name__)

CONFIG_SCHEMA = cv.empty_config_schema(DOMAIN)


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the demo environment."""
    hass.async_create_task(
        hass.config_entries.flow.async_init(
            DOMAIN, context={"source": config_entries.SOURCE_IMPORT}, data={}
        )
    )
    # component = EntityComponent(_LOGGER, DOMAIN, hass)
    # hass.data[DOMAIN] = {}

    if DOMAIN not in config:
        return True

    _LOGGER.info("Setting up cf_min from YAML configuration")

    config.setdefault(ha.DOMAIN, {})
    config.setdefault(DOMAIN, {})

    tasks = []
    tasks.append(
        setup.async_setup_component(
            hass,
            "input_select",
            {
                "input_select": {
                    "living_room_preset": {
                        "options": ["Visitors", "Visitors with kids", "Home Alone"]
                    },
                    "who_cooks": {
                        "icon": "mdi:panda",
                        "initial": "Anne Therese",
                        "name": "Cook today",
                        "options": ["Paulus", "Anne Therese"],
                    },
                }
            },
        )
    )

    # Set up input number
    tasks.append(
        setup.async_setup_component(
            hass,
            "input_number",
            {
                "input_number": {
                    "noise_allowance": {
                        "icon": "mdi:bell-ring",
                        "min": 0,
                        "max": 10,
                        "name": "Allowed Noise",
                        "unit_of_measurement": UnitOfSoundPressure.DECIBEL,
                    }
                }
            },
        )
    )

    results = await asyncio.gather(*tasks)

    if any(not result for result in results):
        return False

    # Set up example persistent notification
    persistent_notification.async_create(
        hass,
        "This is an example of a persistent notification that a number was created.",
        title="Created NUmber Notification",
    )

    async def demo_start_listener(_event: Event) -> None:
        """Finish set up."""
        await finish_setup(hass, config)

    hass.bus.async_listen(EVENT_HOMEASSISTANT_START, demo_start_listener)

    return True


async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool:
    """Set up cf_min from a config entry."""

    # this adds all the 'platforms' we have defined using magic
    await hass.config_entries.async_forward_entry_setups(
        config_entry, COMPONENTS_WITH_CONFIG_ENTRY_DEMO_PLATFORM
    )

    # Store the entry in hass.data for later use if needed
    hass.data.setdefault(DOMAIN, {})[config_entry.entry_id] = config_entry

    return True


async def async_unload_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    await hass.config_entries.async_unload_platforms(
        config_entry, COMPONENTS_WITH_CONFIG_ENTRY_DEMO_PLATFORM
    )
    return True


async def finish_setup(hass: HomeAssistant, config: ConfigType) -> None:
    """Finish set up once demo platforms are set up."""
    switches: list[str] | None = None
    lights: list[str] | None = None

    while not switches and not lights:
        # Not all platforms might be loaded.
        if switches is not None:
            await asyncio.sleep(0)
        switches = sorted(hass.states.async_entity_ids("switch"))
        lights = sorted(hass.states.async_entity_ids("light"))

    assert switches is not None
    assert lights is not None
