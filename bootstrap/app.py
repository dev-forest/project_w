from app import App
from config import app as app_config

app = App()
app.run(app_config.get_app_config().get('bot_token'))