class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Officer(Person):
    def __init__(self, name: "Jamal", age, rank):
        super().__init__(name, age)
        self.rank = rank

Tahseen = Officer("Tahseen", 44, "None")

print(Tahseen.name, Tahseen.age, Tahseen.rank)
