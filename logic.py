class MatheMatics():
    def __init__(self):
        self.a = float(input("Enter the first number: "))
        self.b = float(input("Enter the second number: "))    
    
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def div(self):
        if self.b == 0:
            return "Error: Division by zero is not allowed"
        return self.a / self.b

