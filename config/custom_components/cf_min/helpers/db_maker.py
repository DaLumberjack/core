"""SQLite Database table creator."""

import datetime

import aiosqlite
import const

from homeassistant.core import HomeAssistant


class CommunifarmDatabase:
    """Creates a class to maintain database entries for grow life cycles and observations."""

    def __init__(self, hass: HomeAssistant) -> None:
        """Initialize the database to hose grow cycles."""
        self.hass = hass
        self.db_path = hass.config.path(const.DB_PATH)
        self.conn: aiosqlite.Connection | None = None

    async def async_init(self) -> None:
        """Initialize the database with async."""
        self.conn = await aiosqlite.connect(self.db_path)
        await self.async_setup_tables_from_const()

    async def async_setup_tables_from_const(self) -> None:
        """Create tables for storing Communifarm data if they don't exist."""
        async with self.conn.cursor() as cursor:
            for db in const.DB_CREATOR_JSON:
                if const.DB_CREATOR_JSON[db]["create"]:
                    await cursor.execute(const.DB_CREATOR_JSON[db]["command"])
        await self.conn.commit()

    async def async_close(self) -> None:
        """Close the database connection."""
        if self.conn:
            await self.conn.close()

    async def updateTableRow(
        self,
        hass: HomeAssistant,
        table_name: str,
        columns: dict,
        where_command: str,
    ) -> str:
        """For updating a row in any table. Must use the lookup command dictionary."""
        # where_dict = {
        #     "table_name": table_name,
        #     "columns": columns,
        #     "where_command": where_command,
        # }
        try:
            db_connection = hass.data[const.DOMAIN]["db_connection"]
            cursor = db_connection.cursor()
            # Join column assignments with a comma and space, use parameter placeholders
            col_assignments = ", ".join(f"{column} = ?" for column in columns)

            # Prepare the SQL statement with parameter placeholders for WHERE clause
            sql = f"UPDATE {table_name} SET {col_assignments} WHERE {where_command};"  # noqa: S608

            # Note: For full safety, the where_command should also use parameters.
            # If where_command contains user input, refactor to accept a dict of where parameters and use placeholders.

            cursor.execute(
                sql,
                tuple(columns.values()),
            )

            # Commit the transaction
            await db_connection.commit()

        except db_connection.DatabaseError:
            # _LOGGER.error(f"Failed to insert row into {table_name}: {e}")
            return "None"
        else:
            return cursor.lastrowid

    async def getTableRow(
        self, hass: HomeAssistant, table_name: str, where_command: str, where_id: str
    ) -> dict:
        """Fetches a row from the specified table based on the where command."""
        # Keep a bad return for when we fail to get the row
        bad_return = {"reason": "Initialized empty dictionary"}
        whr_cmd = {
            "table_name": table_name,
            "where_command": where_command,
            "where_id": where_id,
        }
        try:
            db_connection = hass.data[const.DOMAIN]["db_connection"]
            cursor = db_connection.cursor()
            # whr_srt = str(where_command).strip()
            # Execute the query to fetch the row
            query = f"SELECT * FROM {whr_cmd['table_name']} WHERE {whr_cmd['where_command']};"  # noqa: S608
            cursor.execute(query, (where_id,))
            row = cursor.fetchone()

            if row is None:
                bad_return["reason"] = f"Failed to row from {table_name}"
                bad_return["command"] = f"{where_command}"
                return bad_return

            # Get column names from the cursor description
            column_names = [description[0] for description in cursor.description]

            # Create a dictionary with column names as keys and row values as values
            result = dict(zip(column_names, row, strict=False))

        except db_connection.DatabaseError as e:
            # _LOGGER.error(f"Failed to fetch row from {table_name}: {e}")
            bad_return["reason"] = f"Failed to fetch row from {table_name}: {e}"
            return bad_return
        else:
            # Return the primary key of the inserted row
            return result

    async def insertTableRow(
        self, hass: HomeAssistant, table_name: str, columns: dict
    ) -> str:
        """Inserts a row into the specified table and returns the primary key."""

        try:
            db_connection = hass.data[const.DOMAIN]["db_connection"]
            cursor = db_connection.cursor()
            # Validate table and column names to prevent SQL injection
            allowed_tables = []
            for i in const.DB_CREATOR_JSON:
                allowed_tables.append[i]
            if table_name not in allowed_tables:
                raise ValueError(f"Invalid table name: {table_name}")

            allowed_columns = {
                "col1",
                "col2",
                "col3",
            }
            if not set(columns.keys()).issubset(allowed_columns):
                raise ValueError(
                    f"Invalid column(s): {set(columns.keys()) - allowed_columns}"
                )

            column_names = ", ".join(columns.keys())
            placeholders = ", ".join("?" for _ in columns.values())

            # Insert the row using parameterized query for values only
            sql = f"INSERT INTO {table_name} ({column_names}) VALUES ({placeholders})"  # noqa: S608
            cursor.execute(
                sql,
                tuple(columns.values()),
            )
            sql_rsp = cursor.lastrowid
            # Commit the transaction
            db_connection.commit()
        except db_connection.DatabaseError:
            # _LOGGER.error(f"Failed to insert row into {table_name}: {e}")
            return "None"
        else:
            # Return the primary key of the inserted row
            return sql_rsp

    async def insert_grow_cycle(self, name, start_date):
        """Insert a new grow cycle into the database."""
        self.cursor.execute(
            """INSERT INTO grow_cycles (name, start_date, status)
                                VALUES (?, ?, ?)""",
            (name, start_date, "ongoing"),
        )
        self.conn.commit()
        return self.cursor.lastrowid

    async def insert_observation(self, grow_cycle_id, details):
        """Insert a new observation linked to a grow cycle."""
        self.cursor.execute(
            """INSERT INTO observations (grow_cycle_id, observation_date, details)
                                VALUES (?, ?, ?)""",
            (grow_cycle_id, datetime.time, details),
        )
        self.conn.commit()
