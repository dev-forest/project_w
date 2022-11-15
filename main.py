from bootstrap.app import app
from routes import bot as bot_router

if __name__ == '__main__':
    bot = app.get_bot()
    bot_router.dispatcher(bot)

