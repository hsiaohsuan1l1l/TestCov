from TestCov import triangle


class TestStatementCoverage:
    def test_normal(self):
        assert triangle.Triangle(100, 100, 100) == "Equilateral"
        assert triangle.Triangle(60, 60, 100) == "Isosceles"
        assert triangle.Triangle(30, 40, 50) == "Scalene"

    def test_robust(self):
        assert triangle.Triangle(0, 100, 100) == "NotATriangle"
        assert triangle.Triangle(50, 50, 100) == "NotATriangle"
