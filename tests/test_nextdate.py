from TestCov import nextdate


class TestStatementCoverage:
    def test_normal(self):
        assert nextdate.NextDate(12, 31, 2000) == "1.1.2001"
        assert nextdate.NextDate(2, 29, 2000) == "3.1.2000"
        assert nextdate.NextDate(2, 15, 1994) == "2.16.1994"
        assert nextdate.NextDate(4, 15, 2000) == "4.16.2000"

    def test_robust(self):
        assert nextdate.NextDate(0, 15, 2000) == "InvalidInput"
        assert nextdate.NextDate(6, 31, 2000) == "InvalidInput"
        assert nextdate.NextDate(12, 31, 2012) == "InvalidInput"
