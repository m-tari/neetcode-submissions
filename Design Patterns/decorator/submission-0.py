class Coffee(ABC):
    @abstractmethod
    def getCost(self):
        pass

class SimpleCoffee(Coffee):
    def getCost(self):
        return 1.1

class CoffeeDecorator(Coffee):
    def __init__(self, decoratedCoffee):
        self.decoratedCoffee = decoratedCoffee

    def getCost(self):
        return self.decoratedCoffee.getCost()

class MilkDecorator(CoffeeDecorator):
    def __init__(self, decoratedCoffee):
        self.decoratedCoffee = decoratedCoffee

    def getCost(self):
        return 0.5 + self.decoratedCoffee.getCost()

class SugarDecorator(CoffeeDecorator):
    def __init__(self, decoratedCoffee):
        self.decoratedCoffee = decoratedCoffee

    def getCost(self):
        return 0.2 + self.decoratedCoffee.getCost()

class CreamDecorator(CoffeeDecorator):
    def __init__(self, decoratedCoffee):
        self.decoratedCoffee = decoratedCoffee

    def getCost(self):
        return 0.7 + self.decoratedCoffee.getCost()
