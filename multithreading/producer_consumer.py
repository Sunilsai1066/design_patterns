import threading


class CoffeeMachine:
    def __init__(self):
        self.isCoffeeReady = False
        self.condition = threading.Condition()

    def produceCoffee(self):
        while True:
            with self.condition:
                while self.isCoffeeReady:
                    self.condition.wait()

                print("Producing Coffee")
                self.isCoffeeReady = True
                self.condition.notify()

    def consumeCoffee(self):
        while True:
            with self.condition:
                while not self.isCoffeeReady:
                    self.condition.wait()

                print("Consuming Coffee")
                self.isCoffeeReady = False
                self.condition.notify()


CoffeeMachine = CoffeeMachine()

t1 = threading.Thread(target=CoffeeMachine.produceCoffee)
t2 = threading.Thread(target=CoffeeMachine.consumeCoffee)

t1.start()
t2.start()
