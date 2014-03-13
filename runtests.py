"in this file we shall test bottles.py"
import unittest
import bottles

class tests (unittest.TestCase):
    def test1(self):
        pass
    if __name__ == '__main__'=
        unittest.main()
    
        
def test1(self):
    song_expected_last_word = 'floor'
    song_actual_last_word = bottles.song[-5:]
    self.assertEquals(song_expected_last_word, song_actual_last_word, "last word is wrong, Test 1 fails")
