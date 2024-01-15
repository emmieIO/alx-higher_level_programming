#!/usr/bin/python3
"""
Script to list all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys


def list_states(username, password, db_name):
    """
    Connects to the MySQL server and retrieves a
    list of states from the specified database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        db_name (str): Database name.

    Returns:
        None
    """
    try:
        # Connect to MySQL server
        connection = MySQLdb.connect(host="localhost",
                                     port=3306,
                                     user=username,
                                     passwd=password,
                                     db=db_name)

        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Execute the SQL query to retrieve states
        cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

        # Fetch all rows from the result set
        rows = cursor.fetchall()

        # Display results
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()


if __name__ == "__main__":
    """
    Main entry point of the script.
    """
    # Check if correct number of command line arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username>\
              <mysql_password> <database_name>".format(sys.argv[0]))
        sys.exit(1)

    # Get command line arguments
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Call the function to list states
    list_states(username, password, db_name)
