class Greetins:
    def __init__(self, default_name):
        self.default_name = default_name
    
    def greet(self, name=None):
        return f'Hello dear, {name if name else self.default_name}'


greet = Greetins('Jane')
print(greet.default_name)
print(greet.greet())
print(greet.greet('John'))