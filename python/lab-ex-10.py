from abc import ABC, abstractmethod

class Fraction:
    def __init__(self,num:int,denom:int):
        self.__num = num
        self.__denom = denom
    def num(self):
        return self.__num
    def denom(self):
        return self.__denom
    def __str__(self) -> str:
        return str(self.__num) + "/" + str(self.__denom)
    
class Operation(ABC):
    @abstractmethod
    def execute(self, left:Fraction, right:Fraction) -> Fraction:
        pass

    @abstractmethod
    def __str__(self):
        return super().__str__()
    
class Addition(Operation):
    def execute(self, left, right):
        return Fraction(num=left.num * right.denom + right.num * left.denom, denom=left.denom * right.denom)

    def __str__(self):
        return super().__str__()
    
class Subtraction(Operation):
    def execute(self, left, right):
        return Fraction(num=left.num * right.denom - right.num * left.denom, denom=left.denom * right.denom)

    def __str__(self):
        return super().__str__()

class Multiplication(Operation):
    def execute(self, left, right):
        return Fraction(num=left.num * right.num, denom=left.denom * right.denom)

    def __str__(self):
        return super().__str__()

class Division(Operation):
    def execute(self, left, right):
        return Fraction(num=left.num * right.denom, denom=left.denom * right.num)

    def __str__(self):
        return super().__str__()

class Calculation:
    def __init__(self,left:Fraction,right:Fraction,operation:Operation):
        self.__left = left
        self.__right = right
        self.__operation = operation #the parameter that represents the operation
        self.__answer = operation.execute(left, right) #the answer should be calculated here

    def __str__(self):
        return str(self.__left) + " " + str(self.__operation) + " " + str(self.__right) + " = " + str(self.__answer)

f:Fraction = Fraction(1,4)
print(f)
