class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imaginary * other.imaginary
        imaginary_part = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(real_part, imaginary_part)

    def __truediv__(self, other):
        denominator = other.real**2 + other.imaginary**2
        if denominator == 0:
            raise ValueError("Cannot divide by zero.")
        real_part = (self.real * other.real + self.imaginary * other.imaginary) / denominator
        imaginary_part = (self.imaginary * other.real - self.real * other.imaginary) / denominator
        return ComplexNumber(real_part, imaginary_part)

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

if __name__ == "__main__":
    c1 = ComplexNumber(4, 5)
    c2 = ComplexNumber(2, 3)

    print("Addition:", c1 + c2)
    print("Subtraction:", c1 - c2)
    print("Multiplication:", c1 * c2)
    print("Division:", c1 / c2)