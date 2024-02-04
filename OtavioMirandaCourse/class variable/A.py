class A:
    cv = 123

    def __init__(self):
        self.cv = 456

a1 = A()
a2 = A()

print(a1.cv)
print(a2.cv)
print(A.cv)

A.cv = 'new CV'
print()
print(A.cv)