from bootstrap.database import database


class Repository:
    _database_connection = None
    _table = None

    def __init__(self, table: str) -> None:
        self._database_connection = database
        self._table = table
