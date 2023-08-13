import unittest

import app 

class TestCounts(unittest.TestCase):

  def test_counts_with_equal_lists(self):
    teamA = [2, 10, 5, 4, 8]
    teamB = [2, 10, 5, 4, 8]
    expected_counts = [1, 5, 3, 2, 4]
    actual_counts = app.counts(teamA, teamB)
    self.assertEqual(expected_counts, actual_counts)

  def test_counts_with_different_lists(self):
    teamA = [2, 10, 5, 4, 8]
    teamB = [3, 1, 7, 8]
    expected_counts = [1, 0, 3, 4]
    actual_counts = app.counts(teamA, teamB)
    self.assertEqual(expected_counts, actual_counts)

if __name__ == "__main__":
  unittest.main()