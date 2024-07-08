#!/usr/bin/python
# -*- coding: UTF-8 -*-

def display_count():
    print("Total Employee %d" % Employee.empCount)


class Employee:
    # '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def display_employee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


if __name__ == '__main__':
    # "创建 Employee 类的第一个对象"
    emp1 = Employee("Zara", 2000)
    # "创建 Employee 类的第二个对象"
    emp2 = Employee("Manni", 5000)
    emp1.display_employee()
    emp2.display_employee()
    print("Total Employee %d" % Employee.empCount)
