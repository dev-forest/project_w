from app.repository.repository import Repository


class SendWelcomeRepository(Repository):

    def find_buttons_and_text(self):
        sql = "SELECT * FROM messages WHERE route = %s ORDER BY sort"
        result = self._database_connection.fetch(sql, (self._table))
        return result
