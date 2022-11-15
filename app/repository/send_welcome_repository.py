from app.repository.repository import Repository


class SendWelcomeRepository(Repository):

    def get_message(self):
        sql = "SELECT message FROM messages WHERE route = %s"
        result = self._database_connection.read(sql, (self._table))
        return result.get('message')
