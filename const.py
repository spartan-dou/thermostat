"""Constants for the Custom Generic Thermostat helper."""

from homeassistant.components.climate import (
    PRESET_ACTIVITY,
    PRESET_AWAY,
    PRESET_COMFORT,
    PRESET_ECO,
    PRESET_HOME,
    PRESET_SLEEP,
)
from homeassistant.const import Platform

DOMAIN = "custom_generic_thermostat"

PLATFORMS = [Platform.CLIMATE]

CONF_AC_MODE = "ac_mode"
CONF_COLD_TOLERANCE = "cold_tolerance"
CONF_HEATER = "heater"
CONF_HOT_TOLERANCE = "hot_tolerance"
CONF_MAX_TEMP = "max_temp"
CONF_MIN_TEMP = "min_temp"
CONF_TARGET_TEMP = "default_target_temp"
ATTR_TARGET_TEMP_PRESET_NONE = "target_temp_preset_none"
CONF_PRESETS = {
    p: f"{p}_temp"
    for p in (
        PRESET_AWAY,
        PRESET_COMFORT,
        PRESET_ECO,
        PRESET_HOME,
        PRESET_SLEEP,
        PRESET_ACTIVITY,
    )
}
CONF_SENSOR = "target_sensor"
DEFAULT_TOLERANCE = 0.3
DEFAULT_TARGET_TEMP = 19