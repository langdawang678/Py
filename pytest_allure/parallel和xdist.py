
import time
def test_1():
    print("test_1")
    time.sleep(5)
    assert 1 == 1
def test_2():
    print("test_2")
    time.sleep(5)
    assert 2 != 2


'''
# pytest-parallel=2个线程+重试1次 +allure， 10秒，没有中间结果生成
python3 -m pytest /Users/chenxuanhuai/PycharmProjects/Py/pytest+allure+多线程/parallel和xdist.py 
--tests-per-worker=2 --reruns=1 --alluredir=./allure/results

# pytest-parallel=无多线程+重试1次 +allure， 15秒，有中间结果生成
python3 -m pytest /Users/chenxuanhuai/PycharmProjects/Py/pytest+allure+多线程/parallel和xdist.py
 --reruns=1 --alluredir=./allure/results

# pytest-xdist==2个线程+重试1次 +allure， 10秒，没有中间结果生成
python3 -m pytest /Users/chenxuanhuai/PycharmProjects/Py/pytest+allure+多线程/parallel和xdist.py -n=3 --reruns=1 --alluredir=./allure/results

生成报告
python3 -m pytest ./testcase/case_sellercenter/test_postage.py --workers=2 --reruns=3 --alluredir=./allure/results
'''
