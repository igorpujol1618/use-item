from abc import ABC, abstractmethod

class Selector(ABC):
    """Abstract class that describes the flask"""
    @abstractmethod
    def createContent(self):pass

    @abstractmethod
    def accessContent(self):pass

class Content(ABC):
    """Abstract class that describes the flask content"""
    @abstractmethod
    def modHP(self):
        """Abstract class that describes the effects of the contents"""

class GreenFlask(Selector):
    """Concrete class that describes the Green flask"""
    def createContent(self) -> Content:
        return Poison()
    
    def accessContent(self):
        content = self.createContent()
        return content.modHP()
        
class RedFlask(Selector):
    """Concrete class that describes the Red flask"""
    def createContent(self)  -> Content:
        return Medicine()

    def accessContent(self):
        content = self.createContent()
        return content.modHP()

class Medicine(Content):
    """Concrete class that describes the green flask content"""
    def modHP(self):
        """Increase the health points variable"""
        print('Increasing health points.... Plim!')

class Poison(Content):
    """Concrete class that describes the green flask content"""
    def modHP(self):
        """Decrease the health points variable"""
        print('Decreasing health points.... Urg!')

def drink():
    flasks = {
        'Green flask' : GreenFlask(),
        'Red flask' : RedFlask()}
    while True:
        flask_color = input('What flask will you drink?(Red flask, Green flask)')
        if flask_color in flasks:
            return flasks[flask_color].accessContent()

def main():
    drink()

if __name__ == '__main__':
     main()