import unittest
from ts import expand_text

class TestCommentTest(unittest.TestCase):
    
    def test_word(self):
        self.assertEqual(expand_text("hello"),"olleh")
    def test_word2(self):
        self.assertEqual(expand_text(1),"type Error")
    def test_word3(self):
        self.assertEqual(expand_text(True),"type Error")

if __name__ == '__main__':
    unittest.main()