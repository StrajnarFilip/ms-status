import psycopg
import os

def _get_env(environment_variable: str, default: str):
    result = os.getenv(environment_variable)
    return result if result != None else default

def _pg_db():
    return _get_env("PG_DBNAME", "postgres")

def _pg_user():
    return _get_env("PG_USER", "postgres")

def _pg_password():
    return _get_env("PG_PASSWORD", "postgres")

def _pg_host():
    return _get_env("PG_HOST", "127.0.0.1")

def _pg_port():
    return _get_env("PG_PORT", "5432")

def get_connection() -> psycopg.Connection:
    return psycopg.connect(
            autocommit=True,
            dbname = _pg_db(),
            user = _pg_user(),
            password = _pg_password(),
            host = _pg_host(),
            port = _pg_port()
        )

def setup(connection: psycopg.Connection):
    cur = connection.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS status (
        id bigserial PRIMARY KEY,
        checked_at timestamp DEFAULT now(),
        server_online boolean,
        players int,
        latency int)
    """)
