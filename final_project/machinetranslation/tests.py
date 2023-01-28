import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):

    def test_frenchToEnglish(self):
        self.assertEqual(french_to_english(None), None)
        self.assertEqual(french_to_english('Bonjour'), "Hello")
    def test_englishToFrench(self):
        self.assertEqual(english_to_french(None), None)
        self.assertEqual(english_to_french("Hello"), "Bonjour")
    
    
if __name__ == "__main__":
    unittest.main()