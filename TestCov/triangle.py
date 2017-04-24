def Triangle(a, b, c):
    # Restrict sides in range 1 to 200
    if a not in range(1, 201) or b not in range(1, 201) or c not in range(1, 201):
        return "NotATriangle"

    # Triangle formula
    if a + b <= c or a + c <= b or b + c <= a:
        return "NotATriangle"

    # Classify triangle
    if a == b and a == c:
        return "Equilateral"
    elif a == b or a == c or b == c:
        return "Isosceles"
    else:
        return "Scalene"
