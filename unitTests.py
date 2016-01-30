import unittest
from case import Case
from field import Field


class SweeperTests(unittest.TestCase):
    # Cases tests
    def test_safe_case(self):
        test_case = Case(0)
        self.assertFalse(test_case.is_mine())

    def test_mined_case(self):
        test_case = Case(1)
        self.assertTrue(test_case.is_mine())

    def test_bad_case_init(self):
        self.assertRaises(Exception, Case("1"))

    def test_safe_case_proximity(self):
        safe_case = Case(0)
        self.assertEquals("0", safe_case.mine_proximity())
        safe_case.add_mine_proximity()
        self.assertEquals("1", safe_case.mine_proximity())

    def test_mine_case_proximity(self):
        mine_case = Case(1)
        self.assertEquals("*", mine_case.mine_proximity())

    # Field tests
    def test_add_safe_case(self):
        test_field = Field(".")
        self.assertEquals("0", test_field.resolve())

    def test_two_safe_cases(self):
        test_field = Field("..")
        self.assertEquals("00", test_field.resolve())

    def test_two_cells_with_one_bomb(self):
        test_field = Field(".*")
        self.assertEquals("1*", test_field.resolve())
