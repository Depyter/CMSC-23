from abc import ABC, abstractmethod

class Matter:
    def __init__(self,name:str):
        self.__name = name
        self.__state = LiquidState(self) #change this to the appropriate initial state (liquid)
    
    def changeState(self,newState):
        self.__state = newState
    def compress(self):
        self.__state.compress()
    def release(self):
        self.__state.release()
    def cool(self):
        self.__state.cool()
    def heat(self):
        self.__state.heat()
    def __str__(self):
        return "%s is currently a %s" % (self.__name,self.__state) #formatting strings just like you format strings in C
    
class State(ABC):
    @abstractmethod
    def compress(self):
        pass

    @abstractmethod
    def release(self):
        pass

    @abstractmethod
    def cool(self):
        pass

    @abstractmethod
    def heat(self):
        pass

class SolidState(State):
    def __init__(self, matter:Matter):
        self.__matter = matter
    
    def compress(self):
        pass
    def release(self):
        self.__matter.changeState(LiquidState(self.__matter))
    def cool(self):
        pass
    def heat(self):
        self.__matter.changeState(LiquidState(self.__matter))

class LiquidState(State):
    def __init__(self, matter:Matter):
        self.__matter = matter

    def compress(self):
        self.__matter.changeState(SolidState(self.__matter))
    def release(self):
        self.__matter.changeState(GasgeousState(self.__matter))
    def cool(self):
        self.__matter.changeState(SolidState(self.__matter))
    def heat(self):
        self.__matter.changeState(SolidState(self.__matter))

class GasgeousState(State):
    def __init__(self, matter:Matter):
        self.__matter = matter
        
    def compress(self):
        self.__matter.changeState(LiquidState(self.__matter))
    def release(self):
        pass
    def cool(self):
        self.__matter.changeState(LiquidState(self.__matter))
    def heat(self):
        pass
