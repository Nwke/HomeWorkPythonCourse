class Animal:
    hungry = 100

    def __init__(self, name):
        self.name = name

    def eat(self, value):
        self.hungry += int(value)


class FruitOfEggs:
    amount_eggs = 5

    def get_eggs(self):
        if self.amount_eggs >= 0:
            self.amount_eggs -= 1
            return 1


class Goose(Animal):

    @staticmethod
    def vote():
        return 'Goose vote'


class Cow(Animal):
    amount_milk = 100

    def get_milk(self):
        if self.amount_milk >= 10:
            self.amount_milk -= 10
            return 10

    @staticmethod
    def vote():
        return 'Cow vote'


class Sheep(Animal):
    trimmed = False

    def shave(self):
        if not self.trimmed:
            self.trimmed = True
            return 'Шерсть'

    @staticmethod
    def vote():
        return 'Sheep Vote'


class Chicken(Animal, FruitOfEggs):

    @staticmethod
    def vote():
        return 'Chicken vote!'


class Goat(Animal, FruitOfEggs):

    @staticmethod
    def vote():
        return 'Goat vote'


class Duck(Animal, FruitOfEggs):

    @staticmethod
    def vote():
        return 'Duck vote'


goose_gray = Goose('Gray')
goose_white = Goose('White')
cow_manyka = Cow('Manyka')
sheep_barash = Sheep('Barash')
sheep_kudr = Sheep('Kudr')
chicken_koko = Chicken('Koko')
chiken_kukareku = Chicken('Kukareku')
goat_roga = Goat('Roga')
goat_kopito = Goat('Kopito')
duck_kryakva = Duck('Kryakva')

