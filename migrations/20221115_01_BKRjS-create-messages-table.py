"""
Create messages table
"""

from yoyo import step

__depends__ = {}


def apply_step(conn):
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE messages("
        "id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,"
        "route VARCHAR(55) NOT NULL,"
        "message TEXT NOT NULL"
        ");"
    )


def rollback_step(conn):
    cursor = conn.cursor()
    cursor.execute(
        "DROP TABLE IF EXISTS messages;"
    )


steps = [
    step(apply_step, rollback_step)
]
