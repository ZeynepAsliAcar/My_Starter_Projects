import numpy as np
import math

def solve_quadratic(a, b, c):
    delta = b**2 - 4*a*c
    print(f"Delta (Discriminant) = {delta}")

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("Two distinct real roots:")
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
    elif delta == 0:
        x = -b / (2 * a)
        print("One repeated real root:")
        print(f"x = {x}")
    else:
        real = -b / (2 * a)
        imag = math.sqrt(-delta) / (2 * a)
        print("Two complex roots:")
        print(f"x1 = {complex(real, imag)}")
        print(f"x2 = {complex(real, -imag)}")

def solve_polynomial(coeffs):
    degree = len(coeffs) - 1
    print(f"\nPolynomial degree: {degree}")

    if degree == 1:
        a, b = coeffs
        x = -b / a
        print(f"Linear equation. Root: x = {x}")
    elif degree == 2:
        a, b, c = coeffs
        solve_quadratic(a, b, c)
    else:
        roots = np.roots(coeffs)
        print(f"Found {len(roots)} roots:")
        for i, r in enumerate(roots, 1):
            kind = "real" if np.isreal(r) else "complex"
            print(f"Root {i} ({kind}): {r}")

def main():
    print("Enter the coefficients of your polynomial (highest degree first):")
    print("Example for x⁴ - 5x³ + 8x² - 4x + 1 ⇒ 1 -5 8 -4 1")
    coeffs = list(map(float, input("Coefficients: ").strip().split()))
    
    if len(coeffs) < 2:
        print("Please enter at least a degree-1 polynomial.")
        return

    solve_polynomial(coeffs)

main()
