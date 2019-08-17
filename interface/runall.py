import unittest
import time
import HTMLTestRunner

test_suite_dir = 'D:/python/test/interface/testcase/'
report_dir = 'D:/python/test/interface/report/'
now = time.strftime('%Y-%m-%d %H_%M_%S', time.localtime(time.time()))

def creatsuite():

    suiteunit = unittest.TestSuite()
    allcase = unittest.defaultTestLoader.discover(test_suite_dir, pattern='test_*.py')
    for case in allcase:
        suiteunit.addTest(case)
    return suiteunit







if __name__ == '__main__':
    filename = report_dir + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'接口测试',
        description=u'用例执行结果'
    )
    runner.run(creatsuite())
    fp.close()