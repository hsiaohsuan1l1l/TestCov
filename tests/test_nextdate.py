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


class TestMCDC:
    def test_statement(self):
        assert nextdate.NextDate(12, 31, 2000) == "1.1.2001"
        assert nextdate.NextDate(2, 29, 2000) == "3.1.2000"
        assert nextdate.NextDate(2, 15, 1994) == "2.16.1994"
        assert nextdate.NextDate(4, 15, 2000) == "4.16.2000"
        assert nextdate.NextDate(0, 15, 2000) == "InvalidInput"
        assert nextdate.NextDate(6, 31, 2000) == "InvalidInput"
        assert nextdate.NextDate(12, 31, 2012) == "InvalidInput"

    def test_boolean(self):
        # input valid/invalid
        assert nextdate.NextDate(1, 15, 2000) == "1.16.2000"
        assert nextdate.NextDate(0, 15, 2000) == "InvalidInput"

        # big month or small month
        assert nextdate.NextDate(1, 15, 2000) == "1.16.2000"
        assert nextdate.NextDate(4, 15, 2000) == "4.16.2000"

        # Feb. with leap year or Feb. with common year
        assert nextdate.NextDate(2, 29, 2000) == "3.1.2000"
        assert nextdate.NextDate(2, 28, 1994) == "3.1.1994"

        # day valid/invalid
        assert nextdate.NextDate(4, 30, 2000) == "5.1.2000"
        assert nextdate.NextDate(4, 31, 2000) == "InvalidInput"

        # path to change m/d/y
        assert nextdate.NextDate(12, 31, 2000) == "1.1.2001"
        # path to change m/d
        assert nextdate.NextDate(1, 31, 2000) == "2.1.2000"
        # path to change d
        assert nextdate.NextDate(1, 15, 2000) == "1.16.2000"

    def test_independent(self):
        # m in range or not
        assert nextdate.NextDate(6, 15, 2000) == "6.16.2000"
        assert nextdate.NextDate(0, 15, 2000) == "InvalidInput"
        # d in range or not
        assert nextdate.NextDate(6, 15, 2000) == "6.16.2000"
        assert nextdate.NextDate(6, 32, 2000) == "InvalidInput"
        # y in range or not
        assert nextdate.NextDate(6, 15, 2000) == "6.16.2000"
        assert nextdate.NextDate(6, 15, 2013) == "InvalidInput"

        # big month or not
        assert nextdate.NextDate(7, 30, 2000) == "7.31.2000"
        assert nextdate.NextDate(6, 30, 2000) == "7.1.2000"
        # Feb. with leap/common year
        assert nextdate.NextDate(2, 28, 2000) == "2.29.2000"
        assert nextdate.NextDate(2, 28, 1994) == "3.1.1994"

        # day valid or not
        assert nextdate.NextDate(6, 30, 2000) == "7.1.2000"
        assert nextdate.NextDate(6, 31, 2000) == "InvalidInput"

        # change y or not
        assert nextdate.NextDate(12, 31, 2000) == "1.1.2001"
        assert nextdate.NextDate(12, 30, 2000) == "12.31.2000"
        # change m or not
        assert nextdate.NextDate(1, 31, 2000) == "2.1.2000"
        assert nextdate.NextDate(1, 30, 2000) == "1.31.2000"
