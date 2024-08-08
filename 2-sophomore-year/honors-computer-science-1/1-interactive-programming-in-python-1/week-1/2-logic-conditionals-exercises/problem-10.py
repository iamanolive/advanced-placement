import math

def smaller_root (a, b, c):
    discriminant = (b ** 2) - (4 * a * c)
    # positive discriminant
    if discriminant > 0:
        solution1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        solution2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        if solution1 < solution2: return solution1
        else: return solution2
    # 0 discriminant
    elif discriminant == 0:
        solution1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        solution2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        if solution1 < solution2: return solution1
        else: return solution2
    # negative discriminant
    elif discriminant < 0:
        print("Error: No real solutions")