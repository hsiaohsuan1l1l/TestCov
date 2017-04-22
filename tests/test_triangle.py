from TestCov import testcov


class TestStatementCoverage:
    def test_normal(self):
        assert testcov.triangle(100, 100, 100) == "Equilateral"
