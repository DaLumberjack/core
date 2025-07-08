"""Helpers for accessing database tables in Communifarm."""

import logging

from homeassistant.core import HomeAssistant

DOMAIN = "cf_min"
_LOGGER = logging.getLogger(__name__)

"""Module for helping Database Communifarm."""


def updateTableRow(
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
        db_connection = hass.data[DOMAIN]["db_connection"]
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
        db_connection.commit()

    except db_connection.DatabaseError:
        # _LOGGER.error(f"Failed to insert row into {table_name}: {e}")
        return "None"
    else:
        return cursor.lastrowid


def getTableRow(
    hass: HomeAssistant, table_name: str, where_command: str, where_id: str
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
        db_connection = hass.data[DOMAIN]["db_connection"]
        cursor = db_connection.cursor()
        # whr_srt = str(where_command).strip()
        # Execute the query to fetch the row
        query = (
            f"SELECT * FROM {whr_cmd['table_name']} WHERE {whr_cmd['where_command']};"  # noqa: S608
        )
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


def insertTableRow(hass: HomeAssistant, table_name: str, columns: dict) -> str:
    """Inserts a row into the specified table and returns the primary key."""

    try:
        db_connection = hass.data[DOMAIN]["db_connection"]
        cursor = db_connection.cursor()
        # Validate table and column names to prevent SQL injection
        allowed_tables = {
            "your_table1",
            "your_table2",
        }
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
