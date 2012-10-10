# -*- coding: utf-8-unix -*-
u"""演習問題 2-3 "Think Stats"

このプログラムの実行には http://thinkstats.com にて公開されている
以下のモジュールが必要：
 * Pmf.py
"""

import Pmf
import unittest


def AllModes(hist):
    """頻度の降順で値と頻度の組からなるリストを返す"""
    return sorted(hist.Items(), key=lambda x: x[1], reverse=True)


def Mode(hist):
    """最頻度を求める"""
    items = AllModes(hist)
    return items[0][0]


class TestSample(unittest.TestCase):

    def test_case1(self):
        self.assertEquals(Mode(Pmf.MakeHistFromList([1, 2, 2, 5])), 2)
        return

    def test_case2(self):
        self.assertEquals(Mode(Pmf.MakeHistFromList([1, 2, 1, 5, 1, 8])), 1)
        return


def main():
    suiteFew = unittest.TestSuite()
    suiteFew.addTest(unittest.makeSuite(TestSample))
    unittest.TextTestRunner(verbosity=2).run(suiteFew)

    return 0


if __name__ == '__main__':
    main()
