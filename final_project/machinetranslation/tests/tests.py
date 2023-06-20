import unittest

from translator import english_to_french, french_to_english

class TestEnglish_to_french(unittest.TestCase):

    def test1(self):
        self.assertEqual(english_to_french("Hello World"), "Bonjour le monde")
        self.assertEqual(english_to_french("Goodbye"), "Au revoir")
    
    

class TestFrench_to_english(unittest.TestCase):

    def test1(self):
        self.assertEqual(french_to_english("Bonjour le monde"), "Hello World")
        self.assertEqual(french_to_english("Au revoir"), "Goodbye")
    
if __name__ == '__main__':
    unittest.main()        