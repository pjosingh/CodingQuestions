from abc import ABC, abstractmethod

class Computer(ABC):

    def __init__(self) -> None:
        super().__init__()
        
    @abstractmethod
    def process(self):
        pass

    def printSomething(self):
        print("I am a computer")

class Laptop(Computer):

    def process(self):
        print("Hello i am a laptop")
        self.printSomething()


lap = Laptop()
lap.process()