"""
Insert message welcome
"""

from yoyo import step

__depends__ = {'20221115_01_BKRjS-create-messages-table'}


def apply_step(conn):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO messages(route,message) "
        "VALUES ('send_welcome' , 'Welcome to bot')"
    )


def rollback_step(conn):
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM messages "
        "WHERE route = 'send_welcome';"
    )


steps = [
    step(apply_step, rollback_step)
]
