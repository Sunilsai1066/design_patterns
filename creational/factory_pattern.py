# Factory Pattern
from abc import ABC, abstractmethod


class Logistics(ABC):
    @abstractmethod
    def send(self):
        pass


class Air(Logistics):
    def send(self):
        print("Sending By Air")


class Water(Logistics):
    def send(self):
        print("Sending By Water")


class Road(Logistics):
    def send(self):
        print("Sending By Road")


class LogisticsFactory:
    @staticmethod
    def createLogistics(mode):
        if mode == "Air":
            return Air()
        elif mode == "Water":
            return Water()
        else:
            return Road()


class LogisticsService:
    @staticmethod
    def send(mode):
        transport_mode = LogisticsFactory.createLogistics(mode)
        return transport_mode.send()


if __name__ == "__main__":
    logistics = LogisticsService()
    logistics.send("Road")
