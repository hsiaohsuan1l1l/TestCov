def Triangle(a, b, c):
    if a not in range(1, 201) or b not in range(1, 201) or c not in range(1, 201):
        return "NotATriangle"

    if a + b <= c or a + c <= b or b + c <= a:
        return "NotATriangle"

    if a == b and a == c:
        return "Equilateral"
    elif a == b or a == c or b == c:
        return "Isosceles"
    else:
        return "Scalene"
