import pymysql.cursors


class MysqlConnection:
    _instances = {}
    __host: str = '127.0.0.1'
    __port: int = '3306'
    __user: str = 'root'
    __password: str = 'root'
    __database: str = 'database'
    __cur = None
    connection = None

    def __new__(class_, *args, **kwargs):
        if class_ not in class_._instances:
            class_._instances[class_] = super(MysqlConnection, class_).__new__(class_, *args, **kwargs)
        return class_._instances[class_]

    def init(self, host, port, user, password, database):
        self.__host = host
        self.__port = int(port)
        self.__user = user
        self.__password = password
        self.__database = database

    def __connect__(self):
        self.connection = pymysql.connect(host=self.__host,
                                          port=self.__port,
                                          user=self.__user,
                                          password=self.__password,
                                          database=self.__database,
                                          cursorclass=pymysql.cursors.DictCursor)
        self.__cur = self.connection.cursor()

    def __disconnect__(self):
        self.connection.close()

    def fetch(self, sql, args):
        self.__connect__()
        self.__cur.execute(sql, args=args)
        result = self.__cur.fetchall()
        self.__disconnect__()
        return result

    def execute(self, sql):
        self.__connect__()
        self.__cur.execute(sql)
        self.__disconnect__()
