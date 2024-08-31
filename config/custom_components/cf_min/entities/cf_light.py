"""Light for communifarm component."""

from homeassistant.components.light import (
    ATTR_BRIGHTNESS,
    ATTR_RGB_COLOR,
    ColorMode,
    LightEntity,
)

SUPPORT_UV = 1  # Custom flag for UV support
SUPPORT_IR = 2  # Custom flag for IR support


class CommunifarmLight(LightEntity):
    """Representation of a Communifarm light with additional UV and IR control."""

    def __init__(self, name, unique_id, pwm_control) -> None:
        """Initialize the light."""
        self._name = name
        self._unique_id = unique_id
        self._pwm_control = pwm_control
        self._brightness = None
        self._rgb_color = None
        self._uv_intensity = 0
        self._ir_intensity = 0
        self._is_on = False

    @property
    def name(self):
        """Return the display name of this light."""
        return self._name

    @property
    def unique_id(self):
        """Return the unique ID of this light."""
        return self._unique_id

    @property
    def supported_color_modes(self):
        """Return the supported color modes."""
        return {ColorMode.BRIGHTNESS, ColorMode.RGB}

    @property
    def is_on(self):
        """Return true if light is on."""
        return self._is_on

    @property
    def brightness(self):
        """Return the brightness of this light between 0..255."""
        return self._brightness

    @property
    def rgb_color(self):
        """Return the RGB color value."""
        return self._rgb_color

    @property
    def extra_state_attributes(self):
        """Return the state attributes with UV and IR intensities."""
        return {
            "uv_intensity": self._uv_intensity,
            "ir_intensity": self._ir_intensity,
        }

    async def async_turn_on(self, **kwargs):
        """Turn on the light."""
        self._is_on = True
        if ATTR_BRIGHTNESS in kwargs:
            self._brightness = kwargs[ATTR_BRIGHTNESS]
            # Control PWM based on brightness
            self._pwm_control.set_brightness(self._brightness)

        if ATTR_RGB_COLOR in kwargs:
            self._rgb_color = kwargs[ATTR_RGB_COLOR]
            # Control PWM based on RGB color
            self._pwm_control.set_color(self._rgb_color)

        if "uv_intensity" in kwargs:
            self._uv_intensity = kwargs["uv_intensity"]
            # Control PWM or LEDC for UV intensity
            self._pwm_control.set_uv_intensity(self._uv_intensity)

        if "ir_intensity" in kwargs:
            self._ir_intensity = kwargs["ir_intensity"]
            # Control PWM or LEDC for IR intensity
            self._pwm_control.set_ir_intensity(self._ir_intensity)

        self.async_write_ha_state()

    async def async_turn_off(self, **kwargs):
        """Turn off the light."""
        self._is_on = False
        self._brightness = 0
        self._uv_intensity = 0
        self._ir_intensity = 0
        self._pwm_control.turn_off()
        self.async_write_ha_state()

    async def async_update(self):
        """Fetch state from the light."""
        # This can be used to poll the state if needed
