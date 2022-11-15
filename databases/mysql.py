import pymysql.cursors


class MysqlConnection:
    _instances = {}
    connection = None

    def __new__(class_, *args, **kwargs):
        if class_ not in class_._instances:
            class_._instances[class_] = super(MysqlConnection, class_).__new__(class_, *args, **kwargs)
        return class_._instances[class_]

    def init(self, host, port, user, password, database):
        self.connection = pymysql.connect(host=host,
                                          port=int(port),
                                          user=user,
                                          password=password,
                                          database=database,
                                          cursorclass=pymysql.cursors.DictCursor)

    def write(self, sql, *args):
        with self.connection:
            with self.connection.cursor() as cursor:
                cursor.execute(sql, args)
            self.connection.commit()

    def read(self, sql, *args):
        with self.connection:
            with self.connection.cursor() as cursor:
                cursor.execute(sql, args)
                result = cursor.fetchone()
                return result
