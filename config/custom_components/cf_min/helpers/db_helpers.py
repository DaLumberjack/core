from homeassistant.core import HomeAssistant
DOMAIN = "cf_min"

"""Module for helping Database Communifarm."""
def updateTableRow(
    hass: HomeAssistant,
    table_name: str,
    columns: dict,
    where_command: str,
) -> str:
    try:
        db_connection = hass.data[DOMAIN]["db_connection"]
        cursor = db_connection.cursor()
        # Join column assignments with a comma and space
        col_assignments = ", ".join(f"{column} = '{value}'" for column, value in columns.items())
        
        # Insert the row
        cursor.execute(
            f"UPDATE {table_name} SET {col_assignments} WHERE {where_command};",
            tuple(columns.values())
        )
        
        # Commit the transaction
        db_connection.commit()
        
        
        return cursor.lastrowid
    
    except Exception as e:
        # _LOGGER.error(f"Failed to insert row into {table_name}: {e}")
        return None
    
def insertTableRow(
        hass: HomeAssistant,
        table_name: str,
        columns: dict
    ) -> str:
    """Inserts a row into the specified table and returns the primary key."""
    
    try:
        db_connection = hass.data[DOMAIN]["db_connection"]
        cursor = db_connection.cursor()
        # Create a dynamic query for insertion
        column_names = ", ".join(columns.keys())
        placeholders = ", ".join("?" for _ in columns.values())
        
        # Insert the row
        cursor.execute(
            f"INSERT INTO {table_name} ({column_names}) VALUES ({placeholders})",
            tuple(columns.values())
        )
        
        # Commit the transaction
        db_connection.commit()
        
        # Return the primary key of the inserted row
        return cursor.lastrowid
    
    except Exception as e:
        # _LOGGER.error(f"Failed to insert row into {table_name}: {e}")
        return None