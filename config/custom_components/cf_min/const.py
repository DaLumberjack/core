"""Const for Plant."""

from typing import Final

DOMAIN: Final = "cf_min"

DB_PATH = "communifarm.db"
READING_MOISTURE = "moisture"
READING_BATTERY = "battery"
READING_TEMPERATURE = "temperature"
READING_CONDUCTIVITY = "conductivity"
READING_BRIGHTNESS = "brightness"

CONF_MIN_BATTERY_LEVEL = f"min_{READING_BATTERY}"
CONF_MIN_TEMPERATURE = f"min_{READING_TEMPERATURE}"
CONF_MAX_TEMPERATURE = f"max_{READING_TEMPERATURE}"
CONF_MIN_MOISTURE = f"min_{READING_MOISTURE}"
CONF_MAX_MOISTURE = f"max_{READING_MOISTURE}"
CONF_MIN_CONDUCTIVITY = f"min_{READING_CONDUCTIVITY}"
CONF_MAX_CONDUCTIVITY = f"max_{READING_CONDUCTIVITY}"
CONF_MIN_BRIGHTNESS = f"min_{READING_BRIGHTNESS}"
CONF_MAX_BRIGHTNESS = f"max_{READING_BRIGHTNESS}"
CONF_CHECK_DAYS = "check_days"

DEFAULT_MIN_BATTERY_LEVEL = 20
DEFAULT_MIN_MOISTURE = 20
DEFAULT_MAX_MOISTURE = 60
DEFAULT_MIN_CONDUCTIVITY = 500
DEFAULT_MAX_CONDUCTIVITY = 3000
DEFAULT_CHECK_DAYS = 3

ATTR_PROBLEM = "problem"
ATTR_SENSORS = "sensors"
PROBLEM_NONE = "none"
ATTR_MAX_BRIGHTNESS_HISTORY = "max_brightness"

# we're not returning only one value, we're returning a dict here. So we need
# to have a separate literal for it to avoid confusion.
ATTR_DICT_OF_UNITS_OF_MEASUREMENT = "unit_of_measurement_dict"


DB_CREATOR_JSON = {
    "sale": {
        "creator": False,
        "command": """CREATE TABLE IF NOT EXISTS cf_sale (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        grow_cycle_id INTEGER,
                                        harvest_id INTEGER,
                                        recipient TEXT,
                                        charged FLOAT,
                                        tax FLOAT,
                                        discounted BOOLEAN,
                                        discount_amount FLOAT,
                                        discount_percent FLOAT,
                                        sale_date DATETIME,
                                        details TEXT,
                                        FOREIGN KEY (grow_cycle_id) REFERENCES cf_grow_cycle(id)
                                        FOREIGN KEY (harvest_id) REFERENCES cf_harvest(id)
                                    )""",
    },
    "grow_cycle": {
        "create": True,
        "command": """CREATE TABLE IF NOT EXISTS cf_grow_cycle (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        name TEXT NOT NULL,
                                        plant ENUM(Cilantro, Arugula, Lettuce, Spinach, Basil),
                                        tray TEXT,
                                        tray_cell TEXT,
                                        seed_ha_uid TEXT,
                                        tower_ha_uid TEXT,
                                        start_date DATETIME,
                                        end_date DATETIME,
                                        status TEXT
                                    )""",
        "columns": [
            "id",
            "name",
            "plant_id",
            "tray_id",
            "tray_cell_id",
            "seed_id",
            "start_date",
            "status",
        ],
    },
    "observation": {
        "create": True,
        "command": """CREATE TABLE IF NOT EXISTS cf_observation (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        grow_cycle_id INTEGER,
                                        observation_stage ENUM(Planting, Imbition, Germination, Emergence, Cotyledon, True Leaf, Transplant, Vegetative, Flower, Fruit, Ripen, Harvest, Storage, Sale, Transport, Misc),
                                        observation_location ENUM(Seed, Medium, Environment, Stem, Leaf, Root),
                                        observation_date DATETIME,
                                        room_odor_index INTEGER,
                                        tent_odor_index INTEGER,
                                        exterior_odor_index INTEGER,
                                        reservior_odor_index INTEGER,
                                        room_odor_text TEXT,
                                        tent_odor_text TEXT,
                                        exterior_odor_text TEXT,
                                        reservior_odor_text TEXT,
                                        details TEXT,
                                        FOREIGN KEY (grow_cycle_id) REFERENCES cf_grow_cycle(id)
                                    )""",
    },
    "quality_index": {
        "create": True,
        "command": """CREATE TABLE IF NOT EXISTS cf_quality_index (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                observation_id INTEGER,
                                area ENUM(root, stem, leaf, medium, env)
                                location ENUM(base, tip, body, vein)
                                age ENUM(new, old)
                                quality_type TEXT,
                                necrosis_index INTEGER,
                                necrosis_text TEXT,
                                chlorosis_index INTEGER,
                                chlorosis_text TEXT,
                                color_index INTEGER,
                                color_text TEXT,
                                shape_index INTEGER,
                                shape_text TEXT,
                                FOREIGN KEY (observation_id) REFERENCES cf_observation(id)
                                )""",
    },
    "order_index": {
        "create": True,
        "command": """CREATE TABLE IF NOT EXISTS cf_odor_index (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        observation_id INTEGER,
                                        location ENUM(interior, exterior)
                                        area ENUM(reservior, environment, germination, tower, root, leaves, tent)
                                        reservior_type ENUM(main, ro, mixing)
                                        odor_index INTEGER,
                                        odor_text TEXT,
                                        FOREIGN KEY (observation_id) REFERENCES cf_observation(id)
                                        )""",
    },
    "harvest": {
        "create": True,
        "command": """CREATE TABLE IF NOT EXISTS cf_harvest (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        grow_cycle_id INTEGER,
                                        harvest_date DATETIME,
                                        weight FLOAT(2),
                                        unit TEXT,
                                        details TEXT,
                                        FOREIGN KEY (grow_cycle_id) REFERENCES cf_grow_cycles(id)
                                    )""",
    },
}

NUTRIENT_MIXES = {
    "general_hydroponics": {
        "liquid": {
            "cal_mag": {
                "medium": {
                    "value": 15,
                    "min": 10,
                    "max": 20,
                    "unit": "mL/L",
                    "step": 0.1,
                },
                "target": {
                    "value": 15,
                    "min": 10,
                    "max": 20,
                    "unit": "mL/L",
                    "step": 0.1,
                },
            }
        }
    }
    # Add more nutrient mixes here
}
