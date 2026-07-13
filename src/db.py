import mariadb
import os
from dotenv import load_dotenv
import sys

load_dotenv()
# https: // pypi.org/project/python-dotenv/
# Look for a .env file in the same directory as the Python script ( or higher up the directory tree).
# Read each key-value pair and add it to os.environ.
# Not override existing environment variables(override=False). Pass override = True to override existing variables.


def get_connection():
    required_vars = ["DB_HOST", "DB_USER", "DB_PASSWORD", "DB_NAME"]

    for var in required_vars:
        if not os.getenv(var):
            print(f"Missing environment variable: {var}")
            return None

    try:
        return mariadb.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            port=3306
        )

    except mariadb.Error as e:
        print(f"Database connection error: {e}")
        # exit program with error
        sys.exit(1)
        return None
