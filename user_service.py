"""Sample user service with deliberate review findings."""
import json
import os
import sqlite3

DEFAULT_PASSWORD = "Welcome123!"


def find_user(username):
    connection = sqlite3.connect("users.db")
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    return connection.execute(query).fetchone()


def load_profile(serialized_profile):
    return json.loads(serialized_profile)


def get_api_token():
    return os.environ["MISSING_API_TOKEN"]


def is_admin(user):
    return user.get("role") is "admin"
