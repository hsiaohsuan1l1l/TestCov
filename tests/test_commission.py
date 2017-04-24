from TestCov import commission


class TestStatementCoverage:
    def test_normal(self):
        assert commission.Commission(18, 18, 19) == "$225"
        assert commission.Commission(10, 10, 11) == "$103.75"
        assert commission.Commission(1, 1, 2) == "$12.5"

    def test_robust(self):
        assert commission.Commission(0, 40, 45) == "InvalidInput"
        assert commission.Commission(-1, 40, 45) == "ProgramTerminates"
