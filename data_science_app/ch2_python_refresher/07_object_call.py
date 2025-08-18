class Counter:
    def __init__(self):
        self.value = 0
    
    def __call__(self, inc=1):
        self.value += inc
    

c = Counter()
print(c.value)
c() # that call method allowed it to call like function
print(c.value)
c(10)
print(c.value)