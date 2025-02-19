import unittest
import special_list

class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.list = special_list.SpecialList()

    def test_add(self):
        self.list.Add(1)
        self.assertEqual(self.list.my_list, [1])

    def test_access(self):
        self.assertEqual(self.list.Access(), None)
        self.list.Add(1)
        self.list.Add(2)
        self.assertEqual(self.list.Access(), 2)

if __name__ == "__main__":
    unittest.main()