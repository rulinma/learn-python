import unittest

from base.cls.employee import Employee


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

    def test_count(self):
        emp1 = Employee("Zara", 2000)
        # "创建 Employee 类的第二个对象"
        emp2 = Employee("Manni", 5000)
        emp1.display_employee()
        emp2.display_employee()
        self.assertEqual(2, emp2.empCount)


if __name__ == '__main__':
    unittest.main()
