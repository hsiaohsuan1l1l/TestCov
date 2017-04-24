from TestCov import commission


class TestStatementCoverage:
    def test_normal(self):
        assert commission.Commission(18, 18, 19) == "$225"
        assert commission.Commission(10, 10, 11) == "$103.75"
        assert commission.Commission(1, 1, 2) == "$12.5"

    def test_robust(self):
        assert commission.Commission(0, 40, 45) == "InvalidInput"
        assert commission.Commission(-1, 40, 45) == "ProgramTerminates"


class TestMCDC:
    def test_statement(self):
        assert commission.Commission(18, 18, 19) == "$225"
        assert commission.Commission(10, 10, 11) == "$103.75"
        assert commission.Commission(1, 1, 2) == "$12.5"
        assert commission.Commission(0, 40, 45) == "InvalidInput"
        assert commission.Commission(-1, 40, 45) == "ProgramTerminates"

    def test_boolean(self):
        # input valid or not
        assert commission.Commission(0, 40, 45) == "InvalidInput"
        assert commission.Commission(35, 40, 45) == "$640"

        # terminate or not
        assert commission.Commission(-1, 40, 45) == "ProgramTerminates"
        assert commission.Commission(35, 40, 45) == "$640"

        # sales > 1800 or > 1000 or <= 1000
        assert commission.Commission(18, 18, 19) == "$225"
        assert commission.Commission(10, 10, 11) == "$103.75"
        assert commission.Commission(1, 1, 2) == "$12.5"

    def test_independent(self):
        # l in range or not
        assert commission.Commission(35, 40, 45) == "$640"
        assert commission.Commission(0, 40, 45) == "InvalidInput"
        # s in range or not
        assert commission.Commission(35, 40, 45) == "$640"
        assert commission.Commission(35, 0, 45) == "InvalidInput"
        # b in range or not
        assert commission.Commission(35, 40, 45) == "$640"
        assert commission.Commission(35, 40, 0) == "InvalidInput"

        # l = -1 or not
        assert commission.Commission(-1, 40, 45) == "ProgramTerminates"
        assert commission.Commission(35, 40, 45) == "$640"

        # sales > 1800 or not
        assert commission.Commission(18, 18, 19) == "$225"
        assert commission.Commission(18, 18, 17) == "$216.25"
        # sales > 1000 or not
        assert commission.Commission(10, 10, 11) == "$103.75"
        assert commission.Commission(10, 10, 9) == "$97.5"
