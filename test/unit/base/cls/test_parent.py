import unittest

from base.cls.parent import Child


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

    def test_one(self):
        print("test one")
        c = Child()
        c.set_attr(200)
        c.get_attr()
        print("get attr", c.get_attr())
        self.assertEqual(c.get_attr(), 200)
        self.assertTrue(c.get_attr() == 200)


if __name__ == '__main__':
    unittest.main()
