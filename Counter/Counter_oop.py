# it is class based approach

class Counter:

    def __init__(self, start = 0):
        self.count = start

    def increment(self):
        self.count += 1
        return self.count
    
    def decrement(self):
        self.count -= 1
        return self.count
    
    def reset(self):
        self.count = 0
        return self.count
    
    def get_value(self):
        return self.count
    
c1 = Counter(5)
print(c1.increment())
print(c1.decrement())
print(c1.reset())
print(c1.get_value())