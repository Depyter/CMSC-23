from random import randint
from abc import ABC, abstractmethod

class Monster(ABC):
    @abstractmethod
    def announce(self):
        pass

    @abstractmethod
    def move(self):
        pass

class Bokoblin(Monster, ABC):
    @abstractmethod
    def bludgeon(self):
        pass

    @abstractmethod
    def defend(self):
        pass

class Moblin(Monster, ABC):
    @abstractmethod
    def stab(self):
        pass

    @abstractmethod
    def kick(self):
        pass

class Lizalflos(Monster, ABC):
    @abstractmethod
    def throwBoomerang(self):
        pass

    @abstractmethod
    def hide(self):
        pass

class NormalBokoblin(Bokoblin):
    def bludgeon(self):
        print("Bokoblin bludgeons you with a boko club for 1 damage")
    def defend(self):
        print("Bokoblin defends itself with a boko shield")
    def announce(self):
        print("A bokoblin appeared")
    def move(self):
        if randint(1,3) > 1:
            self.bludgeon()
        else:
            self.defend()

class NormalMoblin(Moblin):
    def stab(self):
        print("Moblin stabs you with a spear for 3 damage")
    def kick(self):
        print("Moblin kicks you for 1 damage")
    def announce(self):
        print("A moblin appeared")
    def move(self):
        if randint(1,3) > 1:
            self.stab()
        else:
            self.kick()

class NormalLizalflos(Lizalflos):
    def throwBoomerang(self):
        print("Lizalflos throws its lizal boomerang at you for 2 damage")
    def hide(self):
        print("Lizalflos camouflages itself")
    def announce(self):
        print("A lizalflos appeared")
    def move(self):
        if randint(1,3) > 1:
            self.throwBoomerang()
        else:
            self.hide()

class BlueBokoblin(Bokoblin):
    def bludgeon(self):
        print("Blue bokoblin bludgeons you with a spiked boko club for 2 damage")
    def defend(self):
        print("Blue bokoblin defends itself with a spiked boko shield")
    def announce(self):
        print("A blue bokoblin appeared")
    def move(self):
        if randint(1,3) > 1:
            self.bludgeon()
        else:
            self.defend()

class BlueMoblin(Moblin):
    def stab(self):
        print("Blue moblin stabs you with a rusty halberd for 5 damage")
    def kick(self):
        print("Blue moblin kicks you for 2 damage")
    def announce(self):
        print("A blue moblin appeared")
    def move(self):
        if randint(1,3) > 1:
            self.stab()
        else:
            self.kick()

class BlueLizalflos(Lizalflos):
    def throwBoomerang(self):
        print("Blue lizalflos throws its forked boomerang at you for 3 damage")
    def hide(self):
        print("Blue lizalflos camouflages itself")
    def announce(self):
        print("A blue lizalflos appeared")
    def move(self):
        if randint(1,3) > 1:
            self.throwBoomerang()
        else:
            self.hide()

class SilverBokoblin(Bokoblin):
    def bludgeon(self):
        print("Silver bokoblin bludgeons you with a dragonbone boko club for 5 damage")
    def defend(self):
        print("Silver bokoblin defends itself with a dragonbone boko shield")
    def announce(self):
        print("A silver bokoblin appeared")
    def move(self):
        if randint(1,3) > 1:
            self.bludgeon()
        else:
            self.defend()
    
class SilverMoblin(Moblin):
    def stab(self):
        print("Silver moblin stabs you with a knight's halberd for 10 damage")
    def kick(self):
        print("Silver moblin kicks you for 3 damage")
    def announce(self):
        print("A silver moblin appeared")
    def move(self):
        if randint(1,3) > 1:
            self.stab()
        else:
            self.kick()

class SilverLizalflos(Lizalflos):
    def throwBoomerang(self):
        print("Silver lizalflos throws its forked tri-boomerang at you for 7 damage")
    def hide(self):
        print("Silver lizalflos camouflages itself")
    def announce(self):
        print("A silver lizalflos appeared")
    def move(self):
        if randint(1,3) > 1:
            self.throwBoomerang()
        else:
            self.hide()

# Create an interface to force each dungeon to have
# these three methods
class Dungeon(ABC):

    @abstractmethod
    def newBokoblin(self):
        pass

    @abstractmethod
    def newMoblin(self):
        pass

    @abstractmethod
    def newLizalflos(self):
        pass

class EasyDungeon(Dungeon):
    
    def newBokoblin(self):
        return NormalBokoblin()
    
    def newMoblin(self):
        return NormalMoblin()
    
    def newLizalflos(self):
        return NormalLizalflos()

class MediumDungeon(Dungeon):

    def newBokoblin(self):
        return BlueBokoblin()

    def newMoblin(self):
        return BlueMoblin()

    def newLizalflos(self):
        return BlueLizalflos()

class HardDungeon(Dungeon):

    def newBokoblin(self):
        return SilverBokoblin()

    def newMoblin(self):
        return SilverMoblin()

    def newLizalflos(self):
        return SilverLizalflos()

class Encounter:
    def __init__(self):
        self.dungeon = randint(1,3)

        if self.dungeon == 1:
            self.dungeon = EasyDungeon()
        elif self.dungeon == 2:
            self.dungeon = MediumDungeon()
        elif self.dungeon == 3:
            self.dungeon = HardDungeon()

        self.__enemies = []
        for i in range(randint(0,8)):
            r = randint(1,3)
            if r == 1:
                self.__enemies.append(self.dungeon.newBokoblin())
            elif r==2:
                self.__enemies.append(self.dungeon.newMoblin())
            else:
                self.__enemies.append(self.dungeon.newLizalflos())

    def announceEnemies(self):
        print("%d monsters appeared" % len(self.__enemies))
        for enemy in self.__enemies:
            enemy.announce()

    def moveEnemies(self):
        for enemy in self.__enemies:
            enemy.move()



encounter = Encounter()
encounter.announceEnemies()
print()
encounter.moveEnemies()