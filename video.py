class Triangle:
    def __init__(self, a, b, c):
    
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

t1 = Triangle(3, 4, 5)
print("Perimeter of the triangle:", t1.perimeter())
