from abc import ABC, abstractmethod
class Sentence:
    def __init__(self,words:[str]):
        self.__words = words

    def __str__(self) -> str:
        sentenceString = ""
        for word in self.__words:
            sentenceString += word + " "
        return sentenceString[:-1]

class FormattedSentence(ABC):
    def __init__(self, sentence: Sentence):
        self._wrappedSentence = sentence

    @abstractmethod
    def __str__(self):
        return (f"{self._wrappedSentence}")

class BorderedSentence(FormattedSentence):
    def __str__(self):
        dashes = len(str(self._wrappedSentence)) + 2
        dash = "-" * dashes
        return (f"{dash}\n|{self._wrappedSentence}|\n{dash}")

class FancySentence(FormattedSentence):
    def __str__(self):
        return (f"-+{self._wrappedSentence}+-")

class UpperCaseSentence(FormattedSentence):
    def __str__(self):
        return (f"{self._wrappedSentence}").upper()
    
'--------\n|foo bar|\n--------'
'---------\n|foo bar|\n---------'