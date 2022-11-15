from config import database as database_config
from databases.mysql import MysqlConnection

database = MysqlConnection()

print(database)

if not database.connection:
    config = database_config.get_database_config()
    database.init(host=config.get('host'),
                  port=config.get('port'),
                  user=config.get('user'),
                  password=config.get('password'),
                  database=config.get('database'))
