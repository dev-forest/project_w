from abc import ABC, abstractmethod


class Controller(ABC):

    def request(self, data):
        pass

    def response(self):
        pass
