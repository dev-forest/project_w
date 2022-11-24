from app.repository.send_welcome_repository import SendWelcomeRepository
from aiogram import types


class SendWelcomeModel:

    def get_wellcome_message(self, route_name: str):
        repository = SendWelcomeRepository(route_name)
        result = repository.find_buttons_and_text()
        buttons = self.dispatch_buttons(result[1:])
        text = result[0].get('message')
        return text, buttons

    def dispatch_buttons(self, buttons):
        result = []
        for button in buttons:
            result.append([types.KeyboardButton(button.get('message'))])
        return result
