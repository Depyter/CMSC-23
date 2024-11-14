from datetime import date,timedelta
from abc import ABC, abstractmethod

# First create an interface class
# Make it so that express delivery and standard delivery 
# are CONTRACTUALLY obligated to implement all methods in the interface
class Delivery(ABC):

    # Enforce subclasses to have an init method with location and delivery status
    #@abstractmethod
    #def __init__(self, location: str):
    #    self.__location = location
    #    self.__deliveryStatus = "Processing"

    @abstractmethod
    def estimatedDeliveryDate(self) -> date:
        pass

    @abstractmethod
    def deliveryFee(self) -> float:
        pass

    @abstractmethod
    def deliveryDetails(self) -> str:
        pass

    @abstractmethod
    def changeDeliveryStatus(self) -> None:
        pass

class Order:
    def __init__(self,productName:str, productPrice:float):
        self.__productName = productName
        self.__productPrice = productPrice
    def orderString(self) -> str:
        return "%s P%.2f" % (self.__productName,self.__productPrice)
    def price(self) -> float:
        return self.__productPrice

class ExpressDelivery(Delivery):
    def __init__(self,location:str):
        # Call the parent class implementation 
        super().__init__(location)

    def deliveryDetails(self) -> str:
        r = "EXPRESS DELIVERY\nDELIVER TO:%s\nDELIVERY STATUS: %s\nDELIVERY FEE: P%.2f" % (self.__location,self.__deliveryStatus,self.deliveryFee())
        return r
    def deliveryFee(self) -> float:
        return 1000
    def estimatedDeliveryDate(self,processDate:date) -> float:
        return processDate + timedelta(days = 1)
    def changeDeliveryStatus(self,newStatus:str):
        self.__deliveryStatus = newStatus

class StandardDelivery(Delivery):
    def __init__(self,location:str):
        super().__init__(location)

    def deliveryDetails(self) -> str:
        r = "STANDARD DELIVERY\nDELIVER TO:%s\nDELIVERY STATUS: %s\nDELIVERY FEE: P%.2f" % (self.__location,self.__deliveryStatus,self.deliveryFee())
        return r
    def deliveryFee(self) -> float:
        return 500
    def estimatedDeliveryDate(self,processDate:date) -> float:
        return processDate + timedelta(days = 7)
    def changeDeliveryStatus(self,newStatus:str):
        self.__deliveryStatus = newStatus

class Shipment:
    def __init__(self, orderList:list[Order], processDate: date, location):
        self._orderList = orderList
        self._processDate = processDate
        self._delivery = self.newDelivery(location)

    @abstractmethod
    def newDelivery(self, location):
        return StandardDelivery(location)

    def totalPrice(self) -> str:
        t = 0.0
        for order in self._orderList:
            t+=order.price()
        return t

    def shipmentDetails(self) -> str:
        r = "ORDERS:" + str(self._processDate) + "\n"
        for order in self._orderList:
            r += order.orderString() + "\n"
        r += "\n"
        r += "TOTAL PRICE OF ORDERS: P"  + str(self.totalPrice()) + "\n"
        r += self._delivery.deliveryDetails() + "\n\n"
        r += "PRICE WITH DELIVERY FEE : P" + str(self.totalPrice()+self._delivery.deliveryFee()) + "\n"
        r += "ESTIMATED DELIVERY DATE: " + str(self._delivery.estimatedDeliveryDate(self._processDate))
        return r

class ExpressShipment(Shipment):

    def newDelivery(self, location):
        return ExpressDelivery(location)
     
o = [Order("Surface Pro 7",40000),Order("Zzzquil",900)]
s = ExpressShipment(o,date(2019,11,1),"Cebu City")
print(s.shipmentDetails())