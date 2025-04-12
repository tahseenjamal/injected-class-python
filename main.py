class CapitalizedClassNameMeta(type):
    def __init__(cls, name, bases, attrs):
        if not name[0].isupper():
            raise TypeError(f"Class name '{name}' must start with a capital letter")
        else:
            # Print details of the class name, bases, attributes
            print(name, bases, attrs)

        super().__init__(name, bases, attrs)


class Human(metaclass=CapitalizedClassNameMeta):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old, and is a {self.Profession}"

    def __repr__(self):
        return f"Person({self.name}, {self.age})"


class Profession:
    def __init__(self, job, salary):
        self.job = job
        self.salary = salary

    def __str__(self):
        return f"{self.job} earns {self.salary}"


tahseen = Person("Tahseen", 48)

tahseen.Profession = Profession("Software Engineer", 100000)

print(str(tahseen))
