from random import randint

class Person:
    current_year = 2023

    def __init__(self, name, age, eating=False, speaking=False):
        self.name = name
        self.age = age
        self.eating = eating
        self.speaking = speaking

    def get_birth_year(self):
        birth_year = Person.current_year - self.age
        return birth_year

    def eat(self, food):
        if self.speaking:
            print(f'{self.name} can\'t eat while speaking.')
        else:
            if self.eating:
                print(f'{self.name} is already eating.')
            else:
                print(f'{self.name} is eating {food}')
                self.eating = True

    def stop_eating(self):
        if not self.eating:
            print(f'{self.name} is not eating.')
        else:
            self.eating = False
            print(f'{self.name} stopped eating.')

    def speak(self, subject='random things'):
        if self.speaking:
            print(f'{self.name} is already speaking.')
            return
        else:
            if self.eating:
                print(f'{self.name} can\'t speak while eating')
            else:
                print(f'{self.name} is speaking about {subject}')
                self.speaking = True

    def stop_speaking(self):
        if not self.speaking:
            print(f'{self.name} is not speaking.')
        else:
            self.speaking = False
            print(f'{self.name} stopped speaking.')

    @classmethod
    def by_birth_year(cls, name, birth_year):
        age = cls.current_year - birth_year
        return cls(name, age)

    @staticmethod
    def new_id():
        id = randint(1000, 9999)
        return id