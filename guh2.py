class Base:
    def __init__(self, a=2):
        self.a = a

class Derived(Base):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b


d = Derived(3, 4)
print(d.a, d.b)