import unittest

from word_count import count, count_file

class TestWordCount(unittest.TestCase):

	def test_empty_string(self):
		self.assertEqual(count(""), {})

	def test_one_word(self):
		self.assertEqual(count('word'), {'word': 1})

	def test_two_words(self):
		self.assertEqual(count('word word test'), {'word': 2, 'test': 1})

	def test_case_insensitive(self):
		self.assertEqual(count('word Word'), {'word': 2})

	def test_containing_words(self):
		self.assertEqual(count('test tested'), {'test': 1, 'tested': 1})

	def test_spaces(self):
		self.assertEqual(count('  '), {})

	def test_multi_spaces(self):
		self.assertEqual(count('word  test'), {'word': 1, 'test': 1})

	def test_newline(self):
		self.assertEqual(count('word\ntest'), {'word': 1, 'test': 1})

	def test_non_letters(self):
		self.assertEqual(count('word,test, word'), {'word': 2, 'test': 1})

	def test_double_barrelled(self):
		self.assertEqual(count('word-count'), {'word-count': 1})

	def test_triple_barrelled(self):
		self.assertEqual(count('over-the-top'), {'over-the-top': 1})


class TestCountFile(unittest.TestCase):
	def test_open_file(self):
		self.assertEqual(
			count_file('test_file.txt'),
			{'test': 1, 'world': 1})
