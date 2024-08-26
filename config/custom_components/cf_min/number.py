"""Demo platform that offers a fake Number entity."""

from __future__ import annotations

from homeassistant.components.number import NumberDeviceClass, NumberEntity, NumberMode
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import UnitOfTemperature
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN, NUTRIENT_MIXES


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the demo number platform."""
    communifarm_name = config_entry.data.get("name", "Communifarm")
    communifarm_id = (
        config_entry.data.get("name", "communifarm").replace(" ", "_").lower()
    )
    entities = []
    noots = NUTRIENT_MIXES.items()
    for brand, products in noots:
        for product_type, product_details in products.items():
            for nutrient, nutrient_details in product_details.items():
                for mix_type, details in nutrient_details.items():
                    name = f"{communifarm_name} {brand}_{product_type}_{nutrient}_{mix_type}"
                    unique_id = (
                        f"{communifarm_id}_{brand}_{product_type}_{nutrient}_{mix_type}"
                    )
                    entity = DemoNumber(
                        unique_id=unique_id,
                        device_name=name,
                        state=details["value"],
                        translation_key=nutrient,
                        assumed_state=False,
                        mode=NumberMode.SLIDER,
                        native_min_value=details["min"],
                        native_max_value=details["max"],
                        native_step=details["step"],
                        unit_of_measurement=details["unit"],
                    )
                    entities.append(entity)
    entities.append(
        DemoNumber(
            "volume1",
            "volume",
            42.0,
            "volume",
            False,
            mode=NumberMode.SLIDER,
        )
    )
    entities.append(
        DemoNumber(
            "pwm1",
            "PWM 1",
            0.42,
            "pwm",
            False,
            native_min_value=0.0,
            native_max_value=1.0,
            native_step=0.01,
            mode=NumberMode.BOX,
        )
    )
    entities.append(
        DemoNumber(
            "large_range",
            "Large Range",
            500,
            "range",
            False,
            native_min_value=1,
            native_max_value=1000,
            native_step=1,
        )
    )
    entities.append(
        DemoNumber(
            "small_range",
            "Small Range",
            128,
            "range",
            False,
            native_min_value=1,
            native_max_value=255,
            native_step=1,
        )
    )
    entities.append(
        DemoNumber(
            "temp1",
            "Temperature setting",
            22,
            None,
            False,
            device_class=NumberDeviceClass.TEMPERATURE,
            native_min_value=15.0,
            native_max_value=35.0,
            native_step=1,
            mode=NumberMode.BOX,
            unit_of_measurement=UnitOfTemperature.CELSIUS,
        )
    )

    async_add_entities(entities)


class DemoNumber(NumberEntity):
    """Representation of a demo Number entity."""

    _attr_has_entity_name = True
    _attr_name = None
    _attr_should_poll = False

    def __init__(
        self,
        unique_id: str,
        device_name: str,
        state: float,
        translation_key: str | None,
        assumed_state: bool,
        *,
        device_class: NumberDeviceClass | None = None,
        mode: NumberMode = NumberMode.AUTO,
        native_min_value: float | None = None,
        native_max_value: float | None = None,
        native_step: float | None = None,
        unit_of_measurement: str | None = None,
        device_info: DeviceInfo | None = None,
    ) -> None:
        """Initialize the Demo Number entity."""
        self._attr_assumed_state = assumed_state
        self._attr_device_class = device_class
        self._attr_translation_key = translation_key
        self._attr_mode = mode
        self._attr_native_unit_of_measurement = unit_of_measurement
        self._attr_native_value = state
        self._attr_unique_id = unique_id

        if native_min_value is not None:
            self._attr_native_min_value = native_min_value
        if native_max_value is not None:
            self._attr_native_max_value = native_max_value
        if native_step is not None:
            self._attr_native_step = native_step
        if device_info is not None:
            self._attr_device_info = device_info
        else:
            self._attr_device_info = DeviceInfo(
                identifiers={
                    # Serial numbers are unique identifiers within a specific domain
                    (DOMAIN, unique_id)
                },
                name=device_name,
            )

    async def async_set_native_value(self, value: float) -> None:
        """Update the current value."""
        self._attr_native_value = value
        self.async_write_ha_state()
