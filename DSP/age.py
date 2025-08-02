# birth_year=input('Birth year : ')#no matter what  a variable store only string valu
# print(type(birth_year))
# age=2024-int(birth_year)
# print(age)
import cmath


class Complex:
    def __init__(self, real, imaginary=0):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)

    def __mul__(self, other):
        return Complex(
            self.real * other.real - self.imaginary * other.imaginary,
            self.real * other.imaginary + self.imaginary * other.real
        )

    def __truediv__(self, other):
        denominator = other.real * other.real + other.imaginary * other.imaginary
        return Complex(
            (self.real * other.real + self.imaginary * other.imaginary) / denominator,
            (self.imaginary * other.real - self.real * other.imaginary) / denominator
        )

    def __abs__(self):
        return (self.real ** 2 + self.imaginary ** 2) ** 0.5

    def __pow__(self, exponent):
        if exponent == 0:
            return Complex(1)
        result = self
        for _ in range(1, exponent):
            result *= self
        return result

    def __str__(self):
        if self.imaginary >= 0:
            return f"{self.real} + {self.imaginary}i"
        else:
            return f"{self.real} - {abs(self.imaginary)}i"


def evaluate_polynomial(coefficients, x):
    result = Complex(0)
    degree = len(coefficients) - 1
    for i, coeff in enumerate(coefficients):
        result += Complex(coeff) * (x ** (degree - i))
    return result


def find_roots(coefficients):
    n = len(coefficients) - 1  # Degree of the polynomial
    roots = [Complex(cmath.cos(2 * cmath.pi * i / n), cmath.sin(2 * cmath.pi * i / n)) for i in range(n)]

    convergence = False
    max_iterations = 1000
    tolerance = 1e-10

    for _ in range(max_iterations):
        convergence = True
        new_roots = []
        for i in range(n):
            numerator = evaluate_polynomial(coefficients, roots[i])
            denominator = Complex(1)
            for j in range(n):
                if i != j:
                    denominator *= (roots[i] - roots[j])
            new_root = roots[i] - numerator / denominator
            if abs(new_root - roots[i]) > tolerance:
                convergence = False
            new_roots.append(new_root)
        roots = new_roots
        if convergence:
            break

    return roots


# User input
order = int(input("Enter the order of the polynomial: "))
coefficients = []
print("Enter the coefficients of the polynomial (from highest to lowest order):")
for i in range(order + 1):
    coeff = float(input(f"Coefficient of s^{order - i}: "))
    coefficients.append(coeff)

# Find and display the roots
roots = find_roots(coefficients)
print("\nRoots of the polynomial:")
for root in roots:
    print(root)
