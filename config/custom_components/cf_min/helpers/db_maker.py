"""SQLite Database table creator."""

import datetime
import sqlite3

from homeassistant.core import HomeAssistant


class CommunifarmDatabase:
    """Creates a class to maintain database entries for grow life cycles and observations."""

    def __init__(self, hass: HomeAssistant | None) -> None:
        """Initialize the database to hose grow cycles."""
        self.hass = hass
        self.db_path = hass.config.path("home-assistant_v2.db")
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()

    def setup_tables(self):
        """Create tables for storing Communifarm data if they don't exist."""
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS grow_cycle (
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
                              )""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS observation (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                grow_cycle_id INTEGER,
                                observation_stage ENUM(Planting, Imbition, Germination, Emergence, Cotyledon, True Leaf, Transplant, Vegetative, Flower, Fruit, Ripen, Harvest, Storage, Sale, Transport, Misc),
                                observation_location ENUM(Seed, Medium, Environment, Stem, Leaf, Root),
                                observation_date DATETIME,
                                room_odor_index INTEGER,
                                tent_odor_index INTEGER,
                                exterior_odor_index INTEGER,
                                reservior_odor_index INTEGER,
                                root_tip_new_quality_index INTEGER,
                                root_body_new_qualtiy_index INTEGER,
                                root_vein_new_qualtiy_index INTEGER,
                                root_necrosis_new_qualtiy_index INTEGER,
                                root_chlorosis_new_qualtiy_index INTEGER,
                                stem_tip_new_quality_index INTEGER,
                                stem_body_new_qualtiy_index INTEGER,
                                stem_vein_new_qualtiy_index INTEGER,
                                stem_necrosis_new_qualtiy_index INTEGER,
                                stem_chlorosis_new_qualtiy_index INTEGER,
                                leaf_tip_new_quality_index INTEGER,
                                leaf_body_new_qualtiy_index INTEGER,
                                leaf_vein_new_qualtiy_index INTEGER,
                                leaf_necrosis_new_qualtiy_index INTEGER,
                                leaf_chlorosis_new_qualtiy_index INTEGER,
                                root_tip_old_quality_index INTEGER,
                                root_body_old_qualtiy_index INTEGER,
                                root_vein_old_qualtiy_index INTEGER,
                                root_necrosis_old_qualtiy_index INTEGER,
                                root_chlorosis_old_qualtiy_index INTEGER,
                                stem_tip_old_quality_index INTEGER,
                                stem_body_old_qualtiy_index INTEGER,
                                stem_vein_old_qualtiy_index INTEGER,
                                stem_necrosis_old_qualtiy_index INTEGER,
                                stem_chlorosis_old_qualtiy_index INTEGER,
                                leaf_tip_old_quality_index INTEGER,
                                leaf_body_old_qualtiy_index INTEGER,
                                leaf_vein_old_qualtiy_index INTEGER,
                                leaf_necrosis_old_qualtiy_index INTEGER,
                                leaf_chlorosis_old_qualtiy_index INTEGER,
                                room_odor_text TEXT,
                                tent_odor_text TEXT,
                                exterior_odor_text TEXT,
                                reservior_odor_text TEXT,
                                details TEXT,
                                FOREIGN KEY (grow_cycle_id) REFERENCES grow_cycle(id)
                              )""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS harvest (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                grow_cycle_id INTEGER,
                                harvest_date DATETIME,
                                weight FLOAT(2),
                                unit TEXT,
                                details TEXT,
                                FOREIGN KEY (grow_cycle_id) REFERENCES grow_cycles(id)
                              )""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS sale (
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
                                FOREIGN KEY (grow_cycle_id) REFERENCES grow_cycle(id)
                                FOREIGN KEY (harvest_id) REFERENCES harvest(id)
                              )""")
        self.conn.commit()

    def insert_grow_cycle(self, name, start_date):
        """Insert a new grow cycle into the database."""
        self.cursor.execute(
            """INSERT INTO grow_cycles (name, start_date, status)
                               VALUES (?, ?, ?)""",
            (name, start_date, "ongoing"),
        )
        self.conn.commit()
        return self.cursor.lastrowid

    def insert_observation(self, grow_cycle_id, details):
        """Insert a new observation linked to a grow cycle."""
        self.cursor.execute(
            """INSERT INTO observations (grow_cycle_id, observation_date, details)
                               VALUES (?, ?, ?)""",
            (grow_cycle_id, datetime.now(), details),
        )
        self.conn.commit()

    def close(self):
        """Close the database connection."""
        self.conn.close()
