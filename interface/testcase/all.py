import unittest
import time
import HTMLTestRunner

test_suite_dir = 'D:/python/test/interface/testcase/'

report_dir = 'D:/python/test/interface/report/'

now = time.strftime('%Y-%m-%d %H_%M_%S', time.localtime(time.time()))

def createsuite():

    testunit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(test_suite_dir, pattern='test_*.py', top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTest(test_case)
            print(testunit)
    return testunit


if __name__ == '__main__':
    filename = report_dir+now+'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'接口测试报告',
        description=u'用例执行结果'
    )
    runner.run(createsuite())
    fp.close()