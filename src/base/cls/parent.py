class Parent:  # 定义父类
    parentAttr = 100

    def __init__(self):
        print("调用父类构造函数")

    def parent_method(self):
        print('调用父类方法')

    def set_attr(self, attr):
        Parent.parentAttr = attr

    def get_attr(self):
        print("父类属性 :", Parent.parentAttr)


class Child(Parent):  # 定义子类
    def __init__(self):
        print("调用子类构造方法")

    def child_method(self):
        print('调用子类方法')


if __name__ == '__main__':
    c = Child()  # 实例化子类
    c.child_method()  # 调用子类的方法
    c.parent_method()  # 调用父类方法
    c.set_attr(200)  # 再次调用父类的方法 - 设置属性值
    c.get_attr()  # 再次调用父类的方法 - 获取属性值