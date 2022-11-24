"""
Insert message welcome
"""

from yoyo import step

__depends__ = {'20221115_01_BKRjS-create-messages-table'}


def apply_step(conn):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO messages(route,message,type,sort)"
        "VALUES"
        "('send_welcome' , 'Добро пожаловать!' , 'string', 0),"
        "('send_welcome' , 'Искать вакансии' , 'button', 1),"
        "('send_welcome' , 'Избранное' , 'button', 2)"
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
