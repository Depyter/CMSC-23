from abc import ABC, abstractmethod


class SearchAlgorithm(ABC):
    def __init__(self, target:int, searchSpace:[int]):
        self._searchSpace = searchSpace
        self._currentIndex = 0
        self._solutions = []
        self._target = target

    def bruteForceSolution(self):
        candidate = self.first()
        while(self.isSearching()):
            if self.isValid(candidate):
                self.updateSolution(candidate)
            candidate = self.next()
        return self._solutions

    def first(self) -> int:
        return self._searchSpace[0]

    def next(self) -> int:
        self._currentIndex += 1
        if self.isSearching():
            return self._searchSpace[self._currentIndex]

    def isSearching(self) -> bool:
        return self._currentIndex < len(self._searchSpace)

    @abstractmethod
    def isValid(self, candidate) -> bool:
        pass

    @abstractmethod
    def updateSolution(self, candidate):
        pass

class EqualitySearchAlgorithm(SearchAlgorithm):
    def isValid(self, candidate) -> bool:
        return candidate == self._target

    def updateSolution(self, candidate):
        self._solutions.append(candidate)

class DivisibilitySearchAlgorithm(SearchAlgorithm):
    
    def isValid(self, candidate):
        return candidate % self._target == 0
    
    def updateSolution(self, candidate):
        self._solutions.append(candidate)

class MinimumSearchAlgorithm(SearchAlgorithm):
    
    def isValid(self, candidate):
        return True if not self._solutions else True if candidate < self._solutions[0] else False
    
    def updateSolution(self, candidate):
        if not self._solutions:
            self._solutions.append(candidate)
        else:
            self._solutions[0] = candidate

s1 = MinimumSearchAlgorithm(None, [1,2,-1,4,5])
print(s1.bruteForceSolution())