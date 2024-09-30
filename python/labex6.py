from abc import ABC, abstractmethod
from datetime import date,timedelta

def daysBetween(date1:date, date2:date) -> int:
    difference = date1 -  date2
    return difference.days

class Page:
    def __init__(self, sectionHeader:str, body: str):
        self.__sectionHeader = sectionHeader
        self.__body = body

class BorrowableItem(ABC):
    @abstractmethod
    def uniqueItemId(self) -> int:
        pass
    @abstractmethod
    def commonName(self) -> str:
        pass

class Book(BorrowableItem):
    def __init__(self, bookId:int, title:str, author:str, publishDate:date, pages: list[Page]):
        self.__bookId = bookId
        self.__title = title
        self.__publishDate = publishDate
        self.__author = author
        self.__pages = pages
    def coverInfo(self) -> str:
        return "Title: " + self.__title + "\nAuthor: " + self.__author
    def uniqueItemId(self) -> int:
        return self.__bookId
    def commonName(self) -> str:
        return "Borrowed Item:" + self.__title + " by " + self.__author

class Periodical(BorrowableItem):
    def __init__(self, periodical:int, title:str, author:str, publishDate:date, pages: list[Page]):
        self.__periodicalId = periodical
        self.__title = title
        self.__author = author
        self.__publishDate = publishDate
        self.__pages = pages
    
    def uniqueItemId(self) -> int:
        return self.__periodicalId
    
    def commonName(self) -> str:
        return f"{self.__title} issue: {self.__publishDate}"
    
class PC(BorrowableItem):
    def  __init__(self, pcID: int):
        self.__pcID = pcID
    
    def uniqueItemId(self) -> int:
        return self.__pcID
    
    def commonName(self) -> str:
        return f"PC{self.__pcID}"
    
class LibraryCard:
    def __init__(self, idNumber: int, name: str, borrowedItems: dict[BorrowableItem,date]):
        self.__idNumber = idNumber
        self.__name = name
        self.__borrowedItems = borrowedItems

    def borrowItem(self,book:BorrowableItem, date:date):
        self.__borrowedItems[book] = date

    def borrowerReport(self) -> str:
        r:str = self.__name + "\n"
        for borrowedItem in self.__borrowedItems:
            r = r + borrowedItem.commonName() + ", borrow date:" + str(self.__borrowedItems[borrowedItem]) + "\n"
        return r
    
    def returnItem(self, b:BorrowableItem):
        if self.__borrowedItems[b]:
            del self.__borrowedItems[b]

    def due_date(self, borrow_date:date, item:BorrowableItem) -> date:
            due_date = borrow_date
            if isinstance(item, Book):
                return due_date + timedelta(days=7)
            elif isinstance(item, Periodical):
                return due_date + timedelta(days=1)
            elif isinstance(item, PC):
                return due_date + timedelta(days=0)
            else:
                raise ValueError("Unknown Item")

    def itemsDue(self, today:date) -> list[BorrowableItem]:
        dueitems = []
        for item in self.__borrowedItems:
            item_due_date = self.due_date(self.__borrowedItems[item], item)
            if daysBetween(item_due_date, today) <= 0:
                dueitems.append(item)   
        return dueitems

    def penalty(self, b:BorrowableItem, today:date) -> float:
        item_due_date = self.due_date(self.__borrowedItems[b], b)
        days_overdue = daysBetween(item_due_date, today)
        if days_overdue > 0:
            return days_overdue * 3.5
        return 0.0
        
    def totalPenalty(self, today:date) -> float:
        due_items = self.itemsDue(today)
        total_penalty = 0.0
        for item in due_items:
            total_penalty += self.penalty(item,today)
        return total_penalty
    