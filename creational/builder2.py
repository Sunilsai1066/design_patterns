"""
Builder Code Without Director
"""

from abc import ABC, abstractmethod


class Car:
    def __init__(self):
        self.seats = 0
        self.engine = None
        self.trip_computer = False
        self.gps = False

    def __str__(self):
        return f"Seats : {self.seats} Engine : {self.engine} Trip Computer : {self.trip_computer} GPS : {self.gps}"


class CarManual:
    def __init__(self):
        self.contents = []

    def __str__(self):
        return f"Contents : {self.contents}"


class Builder(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def setSeats(self, seats):
        pass

    @abstractmethod
    def setEngine(self, engine):
        pass

    @abstractmethod
    def setTripComputer(self):
        pass

    @abstractmethod
    def setGPS(self):
        pass

    @abstractmethod
    def getResult(self):
        pass


class CarBuilder(Builder):
    def __init__(self):
        self.car = None
        self.reset()

    def reset(self):
        self.car = Car()
        return self

    def setSeats(self, seats):
        self.car.seats = seats
        return self

    def setEngine(self, engine):
        self.car.engine = engine
        return self

    def setTripComputer(self):
        self.car.trip_computer = True
        return self

    def setGPS(self):
        self.car.gps = True
        return self

    def getResult(self):
        return self.car


class CarManualBuilder(Builder):
    def __init__(self):
        self.manual = None
        self.reset()

    def reset(self):
        self.manual = CarManual()
        return self

    def setSeats(self, seats):
        self.manual.contents.append(f"This Car Has {seats} Seats")
        return self

    def setEngine(self, engine):
        self.manual.contents.append(f"This Car Has {engine} Engine")
        return self

    def setTripComputer(self):
        self.manual.contents.append("This Car Has Trip Computer")
        return self

    def setGPS(self):
        self.manual.contents.append("This Car Has GPS")
        return self

    def getResult(self):
        return self.manual


if __name__ == '__main__':
    car_builder = CarBuilder()
    manual_builder = CarManualBuilder()

    my_car = car_builder.reset().setSeats(5).setEngine("V8").setGPS().setTripComputer().getResult()
    new_car = car_builder.reset().setSeats(4).setEngine("V4").setGPS().getResult()
    print(my_car)
    print(new_car)
