from abc import ABC ,abstractmethod
class computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(computer):
    def process(self):
        print("Laptop is processing")

class WhiteBoard:
    def write(self):
        print("Its Writing")

class Programmer:
    def work(self,com):
        print("Solving problems")
        com.process()

comp1=Laptop()
comp1.process()

pr1=Programmer()
pr1.work(comp1)