class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, degree):
        # to add new property you need to call super like this
        super().__init__(name=name, age=age)
        self.degree = degree

# When to use super()?
# Use it when:

# You override a method in a subclass but still want to reuse logic from the parent class.

# You want to make your code more maintainable and less tightly coupled to a specific superclass.