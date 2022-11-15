from aiogram import Bot


class App:
    __bot: Bot = None
    _instances = {}

    def __new__(class_, *args, **kwargs):
        if class_ not in class_._instances:
            class_._instances[class_] = super(App, class_).__new__(class_, *args, **kwargs)
        return class_._instances[class_]

    def run(self, token: str):
        try:
            bot = Bot(token=token)
            self.__bot = bot
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            raise

    def get_bot(self) -> Bot:
        return self.__bot
