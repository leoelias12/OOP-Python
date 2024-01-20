class Person:
    def __init__(self, name, age, eating=False, speaking=False):
        self.name = name
        self.age = age
        self.eating = eating
        self.speaking = speaking

    def eat(self, food):
        if self.eating:
            print(f'{self.name} is already eating.')
            return
        print(f'{self.name} is eating {food}.')
        self.eating = True
