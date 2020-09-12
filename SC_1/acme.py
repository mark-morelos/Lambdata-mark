import unittest
import random
from random import randint


class Product():
    def __init__(self, name, price=10, weight=20, flammability=0.5, identifier=random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        self.stealability = self.price/self.weight
        if self.stealability < 0.5:
            print(f'Not so stealable...')
        elif 0.5 <= self.stealability < 1:
            print(f'Kinda stealable.')
        else:
            print(f'Very stealable!')

    def explode(self):
        self.explode = self.flammability * self.weight
        if self.explode < 10:
            print(f'...fizzle.')
        elif 10 <= self.explode < 50:
            print(f'...boom!')
        else:
            print(f'...BABOOM!!')

class BoxingGlove(Product):
    def __init__(self, name, price=10, weight=10, flammability=0.5, identifier=random.randint(1000000, 9999999)):
        self.name = name 
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def explode(self):
        print(f"...it's a glove.")
    
    def punch(self):
        if self.weight < 5:
            print(f'That tickles')
        elif 5 <= self.weight < 15:
            print('Hey that hurt!')
        else:
            print('OUCH!')