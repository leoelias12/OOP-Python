from person import Person

p1 = Person('Leonardo', 26)

p1.eat('apple')
p1.eat('Banana')
p1.speak()
p1.stop_eating()
p1.speak('python')
p1.eat('meat')
p1.stop_speaking()
p1.eat('chicken')
p1.eat('pasta')
print()
p2 = Person.by_birth_year('Rafa', 1991)
print(p2.name, p2.age)
print(f'ID: {Person.new_id()}')