from dotenv import dotenv_values

config = dotenv_values('.env')

app_config = {'bot_token': config.get('TELEGRAM_API_KEY')}


def get_app_config() -> dict:
    return app_config
