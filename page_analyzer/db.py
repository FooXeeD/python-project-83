import os
from contextlib import contextmanager

import psycopg2
from psycopg2.extras import NamedTupleCursor
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgresql://fooxeed:4QNoKsp1i1ifqaJa3rLYLwZKUBM4T25K@dpg-cq0kpsiju9rs73auptc0-a/db_twcf'

engine = create_engine(DATABASE_URL, echo=True)

Session = sessionmaker(bind=engine)


@contextmanager
def db_session():
    session = Session()
    try:
        yield session
        session.commit()
    except:  # noqa: E722
        session.rollback()
        raise
    finally:
        session.close()


class DatabaseException(Exception):
    def __init__(self, message):
        self.message = message


def get_connect(config):
    return psycopg2.connect(config)


def add_url_checks(config, data):
    with get_connect(config) as connect:
        with connect.cursor(cursor_factory=NamedTupleCursor) as cursor:
            cursor.execute(
                '''
                INSERT INTO urls_checks (url_id, status_code,
                h1, title, description)
                VALUES (%(url_id)s, %(status_code)s, %(h1)s,
                %(title)s, %(description)s)
                ''', data
            )
            connect.commit()


def get_url_checks_by_id(config, id):
    with get_connect(config) as connect:
        with connect.cursor(cursor_factory=NamedTupleCursor) as cursor:
            cursor.execute(
                'SELECT * FROM urls_checks \
                WHERE url_id = (%s) ORDER BY id DESC',
                (id,)
            )
            result = cursor.fetchall()
            return result


def get_all_urls(config):
    with get_connect(config) as connect:
        with connect.cursor(cursor_factory=NamedTupleCursor) as cursor:
            cursor.execute('SELECT urls.id, urls.name, urls.created_at, \
            urls_checks.status_code, urls_checks.created_at AS \
            urls_checks_created_at , MAX(urls_checks.url_id) \
            FROM urls LEFT JOIN urls_checks ON \
            urls.id=urls_checks.url_id GROUP BY \
            urls.id, urls.name, urls.created_at, urls_checks.status_code, \
            urls_checks.created_at ORDER BY urls.id DESC')
            result = cursor.fetchall()
            return result


def add_url(config, url):
    with get_connect(config) as connect:
        with connect.cursor(cursor_factory=NamedTupleCursor) as cursor:
            cursor.execute(
                'INSERT INTO urls (name) VALUES (%s) RETURNING id',
                (str(url),)
            )
            result = cursor.fetchone()
            connect.commit()
            return result


def get_url_by_id(config, id):
    with get_connect(config) as connect:
        with connect.cursor(cursor_factory=NamedTupleCursor) as cursor:
            cursor = connect.cursor(cursor_factory=NamedTupleCursor)
            cursor.execute(
                'SELECT * FROM urls WHERE id = (%s)',
                (id,)
            )
            result = cursor.fetchone()
            return result


def get_url_by_name(config, name):
    with get_connect(config) as connect:
        with connect.cursor(cursor_factory=NamedTupleCursor) as cursor:
            cursor.execute(
                'SELECT * FROM urls WHERE name = (%s)',
                (name,)
            )
            result = cursor.fetchone()
            return result
