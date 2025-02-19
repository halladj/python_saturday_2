import unittest
from special_list import SpecialList


class TestSpecialList(unittest.TestCase):
    def setUp(self):
        self.sl = SpecialList()

    def test_add_and_access(self):
        self.sl.Add(1)
        self.assertEqual(self.sl.Access(), 1)

        self.sl.Add(2)
        self.sl.Add(3)
        self.assertEqual(self.sl.Access(), 3)

    def test_find(self):
        self.sl.Add(1)
        self.sl.Add(2)
        self.sl.Add(3)
        self.assertTrue(self.sl.Find(1))
        self.assertTrue(self.sl.Find(3))

        self.assertFalse(self.sl.Find(33))

    def test_concat(self):
        self.sl.Add(3)
        self.sl.Add(2)
        self.sl.Add(1)

        temp = SpecialList()
        temp.Add(7)

        self.assertEqual(self.sl + temp, [1,2,3,7])

    def test_length(self):
        self.sl.Add(1)
        self.sl.Add(2)
        self.sl.Add(3)

        self.assertEqual(len(self.sl), 3)

    def test_max_min(self):
        self.sl.Add(1)
        self.sl.Add(2)
        self.sl.Add(3)

        self.sl.Add(100)
        self.sl.Add(-100)

        self.assertEqual(self.sl.max(), 100)
        self.assertEqual(self.sl.min(), -100)
        

    
if __name__ == "__main__":
    unittest.main()