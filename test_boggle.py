import unittest
from boggle import *
from string import ascii_uppercase

class test_boggle(unittest.TestCase):

    def test_can_create_an_empty_grid(self):
        grid = make_grid(0, 0)
        self.assertEqual(len(grid), 0)

    def test_grid_size_equals_width_times_height(self):
        grid = make_grid(2, 3)
        self.assertEqual(len(grid), 6)

    def test_grid_contains_letters(self):
        grid = make_grid(2, 2)
        self.assertIn(grid[(0,0)], ascii_uppercase)
        self.assertIn(grid[(0,1)], ascii_uppercase)
        self.assertIn(grid[(1,0)], ascii_uppercase)
        self.assertIn(grid[(1,1)], ascii_uppercase)

    def test_neighbours_of_position(self):
        coords = (1, 2)
        neighbours = neighbours_of_position(coords)
        self.assertIn((0, 1), neighbours)
        self.assertIn((0, 2), neighbours)
        self.assertIn((0, 3), neighbours)
        self.assertIn((1, 1), neighbours)
        self.assertIn((1, 3), neighbours)
        self.assertIn((2, 1), neighbours)
        self.assertIn((2, 2), neighbours)
        self.assertIn((2, 3), neighbours)

    def test_all_grid_neighbours(self):
        grid = make_grid(2, 2)
        real_neighbours = real_grid_neighbours(grid)

        expected_real_neighbours = {
            (0, 0): [(0,1), (1,0), (1,1)],
            (0, 1): [(0,0), (1,0), (1,1)],
            (1, 0): [(0,0), (0,1), (1,1)],
            (1, 1): [(0,0), (0,1), (1,0)],
        }

        self.assertDictEqual(expected_real_neighbours, real_neighbours)

    def test_converting_a_path_to_a_word(self):
        grid = {
            (0,0): 'A',
            (0,1): 'B',
            (1,0): 'C',
            (1,1): 'D',
        }

        oneLetterWord = path_to_word(grid, [(0,0)])
        self.assertEqual(oneLetterWord, "A")
        twoLetterWord = path_to_word(grid, [(0, 0), (1, 1)])
        self.assertEqual(twoLetterWord, "AD")
        threeLetterWord = path_to_word(grid, [(0, 0), (0, 1), (1, 0)])
        self.assertEqual(threeLetterWord, "ABC")
        fourLetterWord = path_to_word(grid, [(1, 1), (1, 0), (0, 0), (0, 1)])
        self.assertEqual(fourLetterWord, "DCAB")

    def test_load_wordlist(self):
        words = load_wordlist("words.txt")
        self.assertGreater(len(words), 0)
        self.assertIn("WORD", words)
        self.assertIn("ELEPHANT", words)

    def test_search_grid_for_words(self):
        grid = {(0, 0): 'A', (0, 1): 'B', (1, 0): 'C', (1, 1): 'D'}
        twoLetterWord = "AB"
        threeLetterWord = "ABC"
        notThereWord = "EEE"
        wordlist = set([twoLetterWord, threeLetterWord, notThereWord])
        foundWords = search(grid, wordlist)
        self.assertIn(twoLetterWord, foundWords)
        self.assertIn(threeLetterWord, foundWords)
        self.assertNotIn(notThereWord, foundWords)