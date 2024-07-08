import unittest
import sys

# 假设你的测试文件都在tests目录下
# 你可以手动导入每个测试模块，然后添加到测试套件中
# 但更常见的是使用TestLoader来自动发现测试

if __name__ == '__main__':
    # sys.path.append('/Users/rulin/program/temp/learn-python/')
    # 使用TestLoader来自动发现测试
    # loader = unittest.TestLoader()
    # # 假设你的测试文件都在tests目录下，并且文件名以test_开头
    # suite = loader.discover('./', pattern='test_*.py')
    #
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)

    # 运行测试
    # python -m unittest
