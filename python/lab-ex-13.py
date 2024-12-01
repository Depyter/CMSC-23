from abc import ABC, abstractmethod

class Subscriber(ABC):
    @abstractmethod
    def update():
        pass  

class Headline:
    def __init__(self, headline:str, details:str, source:str):
        self.__headline = headline
        self.__details = details
        self.__source = source

    def __str__(self) -> str:
        return "%s(%s)\n%s" % (self.__headline, self.__source, self.__source)

class Weather:
    def __init__(self, temp:float, humidity:float, outlook:str):
        self.__temp = temp
        self.__humidity = humidity
        self.__outlook = outlook

    def __str__(self) -> str:
        return "%s: %.1fC %.1f" % (self.__outlook, self.__temp, self.__humidity)
        
class PushNotifier:
    def __init__(self, headline:Headline, weather:Headline):
        self.__subscribers = []
        self.__currentHeadline = headline
        self.__currentWeather = weather
        self.notifySubscribers()
    
    def updateHeadline(self, newHeadline: Headline):
        self.__currentHeadline = newHeadline
        self.notifySubscribers()
    
    def updateWeather(self, newWeather: Weather):
        self.__currentWeather = newWeather
        self.notifySubscribers()
    
    def subscribe(self, newSubscriber: Subscriber):
        self.__subscribers.append(newSubscriber)
        self.notifySubscribers()
    
    def unsubscribe(self, exSubscriber: Subscriber):
        self.__subscribers.remove(exSubscriber)
        self.notifySubscribers()
        
    # For each subscriber in the list, all their update method
    def notifySubscribers(self):
        for subscriber in self.__subscribers:
            subscriber.update(self.__currentHeadline, self.__currentWeather)
        

class EmailSubscriber(Subscriber):
    def __init__(self, emailAddress):
        self.__emailAddress = emailAddress

    def update(self, newHeadline: Headline, newWeather: Weather):
        print(newHeadline)
        print(newWeather)
        
class FileLogger(Subscriber):
    def __init__(self, filename):
        self.__filename = filename
    
    # Write to the log file using append mode
    def update(self, newHeadline: Headline, newWeather: Weather):
        f = open(self.__filename, "a")
        f.write(str(newHeadline))
        f.write(str(newWeather))
        f.close()

h = Headline("Dalai Lama Triumphantly Names Successor After Discovering Woman With ‘The Purpose Of Our Lives Is To Be Happy’ Twitter Bio","Details","The Onion")
w = Weather(25.0,0.7,"Cloudy")
print(h)
print(w)
