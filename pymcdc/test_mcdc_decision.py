import unittest

from mcdc_decision import classify_score


class ClassifyScoreTests(unittest.TestCase):
    def test_bonus_independently_changes_outcome(self):
        self.assertEqual(classify_score(80, True, False), "pass_with_credit")
        self.assertEqual(classify_score(80, False, False), "standard")

    def test_premium_independently_changes_outcome(self):
        self.assertEqual(classify_score(80, False, True), "pass_with_credit")
        self.assertEqual(classify_score(80, False, False), "standard")

    def test_score_independently_changes_outcome(self):
        self.assertEqual(classify_score(80, True, False), "pass_with_credit")
        self.assertEqual(classify_score(70, True, False), "standard")


if __name__ == "__main__":
    unittest.main()
