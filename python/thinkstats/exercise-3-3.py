# -*- coding: utf-8-unix -*-
u"""演習問題 3-3 "Think Stats"
"""

import sys
import unittest


def PercentileRank(scores, your_score):
    u"""パーセンタイル順位を計算する
    """
    count = 0
    for score in scores:
        if score <= your_score:
            count += 1

    percentile_rank = 100.0 * count / len(scores)
    return percentile_rank


def Percentile(scores, percentile_rank):
    u"""任意のパーセンタイル順位に対応する点数を返す
    """
    scores.sort()
    for score in scores:
        if PercentileRank(scores, score) >= percentile_rank:
            return score

    return None


class TestSample(unittest.TestCase):

    def test_case(self):
        scores = [55, 56, 77, 88, 99]
        self.assertEquals(Percentile(scores, 80), 88)
        return


def main(name):
    suiteFew = unittest.TestSuite()
    suiteFew.addTest(unittest.makeSuite(TestSample))
    unittest.TextTestRunner(verbosity=2).run(suiteFew)

    return 0


if __name__ == '__main__':
    main(*sys.argv)
