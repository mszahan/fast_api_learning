class Temerature:
    def __init__(self, value, scale):
        self.value = value
        self.scale = scale
    
    def __repr__(self):
        return f'Temparature({self.value}, {self.scale})'
    
    def __str__(self):
        return f'Temprature is {self.value} °{self.scale}'
    


t = Temerature(25, 'C')
print(repr(t))
print(str(t))
print(t)