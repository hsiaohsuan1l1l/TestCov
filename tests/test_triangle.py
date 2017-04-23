from TestCov import triangle


class TestStatementCoverage:
    def test_normal(self):
        assert triangle.Triangle(100, 100, 100) == "Equilateral"
        assert triangle.Triangle(60, 60, 100) == "Isosceles"
        assert triangle.Triangle(30, 40, 50) == "Scalene"

    def test_robust(self):
        assert triangle.Triangle(0, 100, 100) == "NotATriangle"
        assert triangle.Triangle(50, 50, 100) == "NotATriangle"


class TestMCDC:
    def test_statement(self):
        assert triangle.Triangle(100, 100, 100) == "Equilateral"
        assert triangle.Triangle(60, 60, 100) == "Isosceles"
        assert triangle.Triangle(30, 40, 50) == "Scalene"
        assert triangle.Triangle(0, 100, 100) == "NotATriangle"
        assert triangle.Triangle(50, 50, 100) == "NotATriangle"

    def test_boolean(self):
        assert triangle.Triangle(0, 100, 100) == "NotATriangle"
        assert triangle.Triangle(100, 100, 100) == "Equilateral"

        assert triangle.Triangle(50, 50, 100) == "NotATriangle"
        assert triangle.Triangle(60, 60, 100) == "Isosceles"

        assert triangle.Triangle(100, 100, 100) == "Equilateral"
        assert triangle.Triangle(60, 60, 100) == "Isosceles"

        assert triangle.Triangle(60, 60, 100) == "Isosceles"
        assert triangle.Triangle(30, 40, 50) == "Scalene"

    def test_independent(self):
        # a not in range(1, 201)
        assert triangle.Triangle(0, 100, 100) == "NotATriangle"
        assert triangle.Triangle(100, 100, 100) == "Equilateral"
        # b not in range(1, 201)
        assert triangle.Triangle(100, 0, 100) == "NotATriangle"
        assert triangle.Triangle(100, 100, 100) == "Equilateral"
        # c not in range(1, 201)
        assert triangle.Triangle(100, 100, 0) == "NotATriangle"
        assert triangle.Triangle(100, 100, 100) == "Equilateral"

        # a + b <= c
        assert triangle.Triangle(50, 50, 100) == "NotATriangle"
        assert triangle.Triangle(60, 50, 100) == "Scalene"
        # a + c <= b
        assert triangle.Triangle(50, 100, 50) == "NotATriangle"
        assert triangle.Triangle(60, 100, 50) == "Scalene"
        # b + c <= a
        assert triangle.Triangle(100, 50, 50) == "NotATriangle"
        assert triangle.Triangle(100, 60, 50) == "Scalene"

        # a == b
        assert triangle.Triangle(100, 100, 100) == "Equilateral"
        assert triangle.Triangle(100, 50, 100) == "Isosceles"
        assert triangle.Triangle(60, 50, 100) == "Scalene"
        # a == c
        assert triangle.Triangle(100, 100, 100) == "Equilateral"
        assert triangle.Triangle(100, 100, 50) == "Isosceles"
        assert triangle.Triangle(60, 100, 50) == "Scalene"
        # b == c
        assert triangle.Triangle(100, 100, 100) == "Equilateral"
        assert triangle.Triangle(100, 50, 100) == "Isosceles"
        assert triangle.Triangle(100, 50, 60) == "Scalene"
