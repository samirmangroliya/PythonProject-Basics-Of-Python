class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printPerson(self):
        print(self.name, self.age)


person = Person("John", 22)
person.printPerson()

print(f"check object type:: {isinstance(person, Person)}")

x = 200
print(isinstance(x, int))
