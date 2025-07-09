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

    def setSeats(self, seats):
        self.car.seats = seats

    def setEngine(self, engine):
        self.car.engine = engine

    def setTripComputer(self):
        self.car.trip_computer = True

    def setGPS(self):
        self.car.gps = True

    def getResult(self):
        return self.car


class CarManualBuilder(Builder):
    def __init__(self):
        self.manual = None
        self.reset()

    def reset(self):
        self.manual = CarManual()

    def setSeats(self, seats):
        self.manual.contents.append(f"This Car Has {seats} Seats")

    def setEngine(self, engine):
        self.manual.contents.append(f"This Car Has {engine} Engine")

    def setTripComputer(self):
        self.manual.contents.append("This Car Has Trip Computer")

    def setGPS(self):
        self.manual.contents.append("This Car Has GPS")

    def getResult(self):
        return self.manual


class Director:
    def __init__(self, base_builder):
        self.builder = base_builder

    def constructSportsCar(self):
        self.builder.reset()
        self.builder.setSeats(2)
        self.builder.setEngine("V8")
        self.builder.setTripComputer()
        self.builder.setGPS()

    def constructManualCar(self):
        self.builder.reset()
        self.builder.setSeats(4)
        self.builder.setEngine("V2")
        self.builder.setTripComputer()


if __name__ == '__main__':
    builder = CarBuilder()
    director = Director(builder)
    director.constructSportsCar()
    sportsCar = builder.getResult()

    manual_builder = CarManualBuilder()
    director = Director(manual_builder)
    director.constructManualCar()
    manualCarManual = manual_builder.getResult()

    print(sportsCar)
    print(manualCarManual)
