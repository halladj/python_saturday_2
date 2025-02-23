import unittest
import special_list

class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.list = special_list.SpecialList()

    # def test_add(self):
    #     self.list.Add(1)
    #     self.assertEqual(self.list.my_list, [1])

<<<<<<< HEAD
    def test_access(self):
        self.assertEqual(self.list.Access(), None)
        self.list.Add(1)
        self.list.Add(2)
        self.assertEqual(self.list.Access(), 2)
    def test_find(self):
        self.list.Add(1)
        self.assertEqual(self.list.Find(1),True )
        self.assertEqual(self.list.Find(2), False)
    def test_max(self):
        self.list.Add(-1)
        self.list.Add(-2)
        self.assertEqual(self.list.max(), -1)
    def test_min(self):
        self.list.Add(1)
        self.list.Add(2)
        self.assertEqual(self.list.min(), 1)


=======
    # def test_access(self):
    #     self.assertEqual(self.list.Access(), None)
    #     self.list.Add(1)
    #     self.list.Add(2)
    #     self.assertEqual(self.list.Access(), 2)

    def test_Find(self):
        self.list.Add(5)
        self.assertTrue(self.list.Find(5))
        self.assertFalse(self.list.Find(9))
>>>>>>> b52b05c716f9be3346d8eaf59cad0cfa3e69588f

if __name__ == "__main__":
    unittest.main()