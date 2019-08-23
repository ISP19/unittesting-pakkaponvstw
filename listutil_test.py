import unittest
from listutil import unique


class ListUtiltest(unittest.TestCase):
    def test_average_singleon_list(self):  # extream Case
        self.assertEqual(['a', 'b', 'c', 'd', 'e'], unique(
            ['a', 'b', 'c', 'd', 'd', 'e', 'e']))

    def test_average_typical_list(self):  # Typical Case
        self.assertEqual(['Hello', 'Bye', 'Ok'], unique(
            ['Hello', 'Bye', 'Bye', 'Hello', 'Ok', 'Ok']))

    def test_average_listin_list(self):  # Test List in List
        self.assertEqual([1, 2, 3, [7, 8, 9]], unique([1, 2, 3, [7, 8, 9]]))

    def test_average_TypicalCase_list(self):  # Typical Case
        self.assertEqual([1], unique([1, 1, 1, 1, 1, 1]))

    def test_average_Impossibal_list(self):  # Imposible Case
        self.assertEqual([], unique([]))

    def test_average_BorderLine_list(self):
        self.assertEqual([9], unique([9]))


if __name__ == "__main__":
    unittest.main()
