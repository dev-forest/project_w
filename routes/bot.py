from aiogram import Dispatcher, types, executor
from app.controller.send_welcome_controller import SendWelcomeController


def dispatcher(bot):
    dp = Dispatcher(bot)

    @dp.message_handler(commands=['start', 'help'])
    async def send_welcome(message: types.Message):
        controller = SendWelcomeController()
        text, buttons = controller.response(route_name=send_welcome.__name__)
        keyboard = types.ReplyKeyboardMarkup(keyboard=buttons)
        await message.reply(text, reply_markup=keyboard)

    @dp.message_handler()
    async def echo(message: types.Message):
        await message.answer('test')

    executor.start_polling(dp, skip_updates=True)
