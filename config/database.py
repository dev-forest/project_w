from dotenv import dotenv_values

config = dotenv_values('.env')

database_config = {
    "host": config.get('DATABASE_HOST'),
    "port": config.get('DATABASE_PORT'),
    "user": config.get('DATABASE_USER'),
    "password": config.get('DATABASE_PASSWORD'),
    "database": config.get('DATABASE_NAME'),
}


def get_database_config() -> dict:
    return database_config
