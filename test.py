from base.cls.employee import Employee
from base.color.green import green
from base.color.red import red

if __name__ == '__main__':
    print("hello world")

    # 测试model和package
    red = red()
    green = green()

    print(red)
    print(green)

    # 测试class功能
    # "创建 Employee 类的第一个对象"
    emp1 = Employee("Zara", 2000)
    # "创建 Employee 类的第二个对象"
    emp2 = Employee("Manni", 5000)
    emp1.display_employee()
    emp2.display_employee()
    print("Total Employee %d" % Employee.empCount)