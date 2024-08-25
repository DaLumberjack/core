"""Devices to be used in communifarm."""

from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity import Entity

from .const import DOMAIN


class NutrientDeviceEntity(Entity):
    """Device specifics for a nutrient device or product."""

    def __init__(
        self,
        name,
        unique_id,
        liquid_or_dry,
        manufacturer,
        manufacture_date,
        model,
        purchase_date,
        storage_location,
        hw_version,
    ):
        """Initialize the entity."""
        self._name = name
        self._unique_id = unique_id
        self._liquid_or_dry = liquid_or_dry
        self._manufacture_date = manufacture_date
        self._manufacturer = manufacturer
        self._model = model
        self._purchase_date = purchase_date
        self._storage_location = storage_location
        self._hw_version = hw_version

    @property
    def name(self):
        """Return the name of the entity."""
        return self._name

    @property
    def unique_id(self):
        """Return a unique ID for this entity."""
        return self._unique_id

    @property
    def state(self):
        """Return the current state."""
        return "operational"

    @property
    def extra_state_attributes(self):
        """Return the state attributes."""
        return {
            "liquid_or_dry": self._liquid_or_dry,
            "manufacture_date": self._manufacture_date,
            "purchase_date": self._purchase_date,
            "storage_location": self._storage_location,
        }

    @property
    def device_info(self) -> DeviceInfo:
        """Return device information about this entity."""
        return DeviceInfo(
            identifiers={(DOMAIN, self._unique_id)},
            name=self._name,
            manufacturer=self._manufacturer,
            model=self._model,
            sw_version="1.0",
            hw_version=self._hw_version,
            configuration_url="http://homeassistant.local:8123/config/devices/dashboard?historyBack=1&domain=cf_min",
            suggested_area="Greenhouse",
        )
