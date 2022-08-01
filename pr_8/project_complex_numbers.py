class Complex_number:
    def __init__(self, real_part: int, imaginary_part: int):
        self.real_part = real_part
        self.imaginary_part = imaginary_part

    def __str__(self):
        return f'{self.real_part} + {self.imaginary_part}j'

    def __mul__(self, other):
        return Complex_number((self.real_part * other.real_part - self.imaginary_part * other.imaginary_part),
                              (self.imaginary_part * other.real_part + self.real_part * other.imaginary_part))

    def __add__(self, other):
        return Complex_number(self.real_part + other.real_part, self.imaginary_part + other.imaginary_part)


compelx_1 = Complex_number(7, 9)
compelx_2 = Complex_number(10, 10)
print(compelx_1 + compelx_2)
print(compelx_1 * compelx_2)
