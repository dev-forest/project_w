from app.repository.send_welcome_repository import SendWelcomeRepository


class SendWelcomeModel:

    def get_wellcome_message(self, route_name: str) -> str:
        repository = SendWelcomeRepository(route_name)
        return repository.get_message()
