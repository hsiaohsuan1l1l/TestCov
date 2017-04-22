from TestCov import triangle


class TestStatementCoverage:
    def test_normal(self):
        assert triangle.Triangle(100, 100, 100) == "Equilateral"
