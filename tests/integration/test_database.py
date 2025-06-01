import uuid

import pytest

import sobremesa.service.utils.database as database

PSQL_CONFIG = database.PostgresConnectionConfig(
    host="postgres", port=5432, dbname="sobremesadb", user="remy", password="password"
)


@pytest.fixture
def clean_db():
    conn = database.create_connection(PSQL_CONFIG, autocommit=True)
    try:
        conn.cursor().execute("DELETE FROM recipes")
        conn.cursor().execute("DELETE FROM users")
        yield conn
    finally:
        conn.cursor().execute("DELETE FROM recipes")
        conn.cursor().execute("DELETE FROM users")
        conn.close()


# @database.with_connection(PSQL_CONFIG)
# def test_connection(conn):
def test_connection(clean_db):
    cursor = clean_db.cursor()
    cursor.execute("SELECT * FROM users")
    assert cursor.fetchall() == []


@database.with_connection(config=PSQL_CONFIG, autocommit=True)
def test_database_insert(clean_db):
    cursor = clean_db.cursor()
    cursor.execute("SELECT * FROM users")
    assert len(cursor.fetchall()) == 0

    cursor.execute(
        "INSERT INTO users (id, email) VALUES (%(id)s, %(email)s)",
        {"id": uuid.uuid4(), "email": "someone@somewhere.com"},
    )
    cursor.execute("SELECT * FROM users")
    assert len(cursor.fetchall()) == 1


@database.with_connection(config=PSQL_CONFIG, autocommit=True)
def test_database_insert_with_connection(conn):
    try:
        conn.cursor().execute("DELETE FROM recipes")
        conn.cursor().execute("DELETE FROM users")

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        assert len(cursor.fetchall()) == 0

        cursor.execute(
            "INSERT INTO users (id, email) VALUES (%(id)s, %(email)s)",
            {"id": uuid.uuid4(), "email": "someone@somewhere.com"},
        )
        cursor.execute("SELECT * FROM users")
        assert len(cursor.fetchall()) == 1
    finally:
        conn.cursor().execute("DELETE FROM recipes")
        conn.cursor().execute("DELETE FROM users")
