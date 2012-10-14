# -*- coding: utf-8-unix -*-
u"""演習問題 2-5 "Think Stats"

このプログラムの実行には http://thinkstats.com にて公開されている
以下のモジュールが必要：
 * Pmf.py
"""

import Pmf
import unittest


def PmfMean(pmf):
    """Pmfオブジェクトを受け取り、算術平均を求める
    """
    return sum(map(lambda (v, p): p * v, pmf.Items()))


def PmfVar(pmf):
    """Pmfオブジェクトを受け取り、分散を求める
    """
    mean = PmfMean(pmf)
    return sum(map(lambda (v, p): p * ((v - mean) ** 2), pmf.Items()))


class TestSample(unittest.TestCase):

    def test_case1(self):
        pmf = Pmf.MakePmfFromList([1, 2, 2, 5])
        self.assertEquals(pmf.Mean(), PmfMean(pmf))
        self.assertEquals(pmf.Var(), PmfVar(pmf))
        return

    def test_case2(self):
        pmf = Pmf.MakePmfFromList([5, 5, 15, 15, 960])
        self.assertEquals(pmf.Mean(), PmfMean(pmf))
        self.assertEquals(pmf.Var(), PmfVar(pmf))
        return


def main():
    suiteFew = unittest.TestSuite()
    suiteFew.addTest(unittest.makeSuite(TestSample))
    unittest.TextTestRunner(verbosity=2).run(suiteFew)

    return 0


if __name__ == '__main__':
    main()
