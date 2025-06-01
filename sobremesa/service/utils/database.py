from dataclasses import asdict, dataclass

import psycopg
from psycopg.rows import dict_row
from psycopg.types.composite import CompositeInfo, register_composite


@dataclass
class PostgresConnectionConfig:
    host: str
    port: int
    dbname: str
    user: str
    password: str


def create_connection(
    config: PostgresConnectionConfig, autocommit=False
) -> psycopg.Connection[psycopg.rows.DictRow]:
    conn = psycopg.connect(
        **asdict(config), row_factory=dict_row, autocommit=autocommit
    )

    register_composite(CompositeInfo.fetch(conn, "ingredient"), conn)
    register_composite(CompositeInfo.fetch(conn, "instruction"), conn)
    register_composite(CompositeInfo.fetch(conn, "timer"), conn)
    return conn


def with_connection(config, autocommit=False):
    def decorator(func):
        def call_func_with_connection(*args, **kwargs):
            conn = create_connection(config)

            try:
                rc = func(conn, *args, **kwargs)
            except Exception:
                conn.rollback()
                raise
            else:
                conn.commit()
            finally:
                conn.close()
            return rc

        return call_func_with_connection

    return decorator
