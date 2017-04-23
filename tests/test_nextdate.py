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


class TestDDPathCoverage:
    def test_normal(self):
        # edgeday = 31 and path to change m/d/y
        assert nextdate.NextDate(12, 31, 2000) == "1.1.2001"
        assert nextdate.NextDate(1, 31, 2000) == "2.1.2000"
        assert nextdate.NextDate(1, 15, 2000) == "1.16.2000"

        # edgeday = 29 and path to change m/d
        assert nextdate.NextDate(2, 29, 2000) == "3.1.2000"
        assert nextdate.NextDate(2, 15, 2000) == "2.16.2000"

        # edgeday = 28 and path to change m/d
        assert nextdate.NextDate(2, 28, 1994) == "3.1.1994"
        assert nextdate.NextDate(2, 15, 1994) == "2.16.1994"

        # edgeday = 30 and path to change m/d
        assert nextdate.NextDate(4, 30, 2000) == "5.1.2000"
        assert nextdate.NextDate(4, 15, 2000) == "4.16.2000"

    def test_robust(self):
        # invalid input
        assert nextdate.NextDate(0, 31, 2000) == "InvalidInput"
        # path to d > edgeday
        assert nextdate.NextDate(2, 30, 2000) == "InvalidInput"
        assert nextdate.NextDate(2, 29, 1994) == "InvalidInput"
        assert nextdate.NextDate(4, 31, 2000) == "InvalidInput"
        # path to y + 1 > 2012
        assert nextdate.NextDate(12, 31, 2012) == "InvalidInput"
