from app.controller.controller import Controller
from app.model.send_welcome_model import SendWelcomeModel


class SendWelcomeController(Controller):

    def response(self, route_name: str):
        model = SendWelcomeModel()
        return model.get_wellcome_message(route_name)
