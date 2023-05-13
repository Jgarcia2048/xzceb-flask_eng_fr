from tests.translator import english_to_french, french_to_english
import unittest

class TestMyModule(unittest.TestCase):

    def test_englishToFrench(self):
        assert self is not None
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

    def test_frenchToEnglish(self):
        assert self is not None
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main()