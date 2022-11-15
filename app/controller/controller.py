from abc import ABC, abstractmethod


class Controller(ABC):

    def response(self, route_name: str):
        pass
