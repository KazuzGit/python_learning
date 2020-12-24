class ComplexNumber:
    def __init__(self, a, b):
        self.real_z = a
        self.imaginary_z = b

    def __str__(self):
        if self.imaginary_z < 0:
            sign = '-'
        else:
            sign = '+'

        self.imaginary_z = abs(self.imaginary_z)

        return f'{self.real_z} {sign} {self.imaginary_z}i'

    def __add__(self, other_complex):
        real = self.real_z + other_complex.real_z
        imaginary = self.imaginary_z + other_complex.imaginary_z
        return ComplexNumber(real, imaginary)

    def __mul__(self, other_complex):
        real = self.real_z * other_complex.real_z - self.imaginary_z * other_complex.imaginary_z
        imaginary = self.imaginary_z * other_complex.real_z + self.real_z * other_complex.imaginary_z
        return ComplexNumber(real, imaginary)


num1 = ComplexNumber(2, 4)
num2 = ComplexNumber(1, 5)
print(num1 + num2)
print(num1 * num2)