"""Config flow to configure demo component."""

from __future__ import annotations

import logging
from typing import Any

import voluptuous as vol

from homeassistant.config_entries import (
    ConfigEntry,
    ConfigFlow,
    ConfigFlowResult,
    OptionsFlow,
)
from homeassistant.core import callback
import homeassistant.helpers.config_validation as cv

from .const import DOMAIN

CONF_NAME = "name"
CONF_STRING = "string"
CONF_BOOLEAN = "bool"
CONF_INT = "int"
CONF_SELECT = "select"
CONF_MULTISELECT = "multi"

_LOGGER = logging.getLogger(__name__)


class DemoConfigFlow(ConfigFlow, domain=DOMAIN):
    """Demo configuration flow."""

    VERSION = 1

    @staticmethod
    @callback
    def async_get_options_flow(
        config_entry: ConfigEntry,
    ) -> OptionsFlowHandler:
        """Get the options flow for this handler."""
        return OptionsFlowHandler(config_entry)

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle the initial step."""
        errors = {}

        if user_input is not None:
            # Check if a similar entry already exists based on some unique identifier
            # If you don't want to check for duplicates, simply remove this condition
            _LOGGER.debug("Creating config entry with data: %s", user_input)
            existing_entries = self._async_current_entries()
            if any(
                entry.data.get(CONF_STRING) == user_input[CONF_STRING]
                for entry in existing_entries
            ):
                errors["base"] = "already_configured"
            else:
                # Log the creation process
                _LOGGER.debug("Creating config entry with data: %s", user_input)
                entry_name = user_input.get(CONF_NAME, "Communifarm")
                return self.async_create_entry(title=entry_name, data=user_input)

        # Show the form to the user if no input is provided or if there are errors
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(
                        CONF_NAME, default="My Communifarm"
                    ): str,  # Add the name field
                    vol.Required(CONF_STRING, default="Default String"): str,
                    vol.Optional(CONF_BOOLEAN, default=False): bool,
                    vol.Optional(CONF_INT, default=10): int,
                }
            ),
            errors=errors,
        )

    async def async_step_import(self, import_info: dict[str, Any]) -> ConfigFlowResult:
        """Set the config entry up from yaml."""
        if self._async_current_entries():
            return self.async_abort(reason="single_instance_allowed")

        # Use the name provided in the import as the title
        entry_name = import_info.get(CONF_NAME, "Communifarm")
        return self.async_create_entry(title=entry_name, data=import_info)


class OptionsFlowHandler(OptionsFlow):
    """Handle options."""

    def __init__(self, config_entry: ConfigEntry) -> None:
        """Initialize options flow."""
        self.config_entry = config_entry
        self.options = dict(config_entry.options)

    async def async_step_init(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Manage the options."""
        return await self.async_step_options_1()

    async def async_step_options_1(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Manage the options."""
        if user_input is not None:
            self.options.update(user_input)
            return await self.async_step_options_2()

        return self.async_show_form(
            step_id="options_1",
            data_schema=vol.Schema(
                {
                    vol.Required("constant"): "Constant Value",
                    vol.Optional(
                        CONF_BOOLEAN,
                        default=self.config_entry.options.get(CONF_BOOLEAN, False),
                    ): bool,
                    vol.Optional(
                        CONF_INT,
                        default=self.config_entry.options.get(CONF_INT, 10),
                    ): int,
                }
            ),
        )

    async def async_step_options_2(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Manage the options 2."""
        if user_input is not None:
            self.options.update(user_input)
            return await self._update_options()

        return self.async_show_form(
            step_id="options_2",
            data_schema=vol.Schema(
                {
                    vol.Optional(
                        CONF_STRING,
                        default=self.config_entry.options.get(
                            CONF_STRING,
                            "Default",
                        ),
                    ): str,
                    vol.Optional(
                        CONF_SELECT,
                        default=self.config_entry.options.get(CONF_SELECT, "default"),
                    ): vol.In(["default", "other"]),
                    vol.Optional(
                        CONF_MULTISELECT,
                        default=self.config_entry.options.get(
                            CONF_MULTISELECT, ["default"]
                        ),
                    ): cv.multi_select({"default": "Default", "other": "Other"}),
                }
            ),
        )

    async def _update_options(self) -> ConfigFlowResult:
        """Update config entry options."""
        return self.async_create_entry(title="", data=self.options)
