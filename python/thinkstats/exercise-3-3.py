# -*- coding: utf-8-unix -*-
u"""演習問題 3-3、3-4 "Think Stats"
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
    index = int(percentile_rank * (len(scores) - 1) / 100)
    return scores[index]


def Partition(l, left, right, pivot_index):
    u"""リストをある値より小さい数のリストと
    それより大きい数のリストに分割する

    Wikipedia 『選択アルゴリズム』 より
    """
    def swap(i, j):
        tmp = l[i]
        l[i] = l[j]
        l[j] = tmp

    pivot_value = l[pivot_index]
    swap(pivot_index, right)
    store_index = left
    for i in range(left, right):
        if l[i] <= pivot_value:
            swap(store_index, i)
            store_index = store_index + 1
    swap(right, store_index)
    return store_index


def Select(target_list, k):
    u"""リストの要素の中でk番目に小さい値を求める

    Wikipedia 『選択アルゴリズム』 より
    """
    def Median(l):
        m = l[:]
        m.sort()
        return l.index(m[len(l) / 2])

    def SelecpPivot(l, left, right):
        size = len(l) / 5
        return Median([Median(l[i:i+size]) for i in range(0, len(l), size)])

    l = target_list[:]
    left = 0
    right = len(l) - 1

    while True:
        pivot_index = SelecpPivot(l, left, right)
        pivot_new_index = Partition(l, left, right, pivot_index)

        if k == pivot_new_index:
            return l[k]
        elif k < pivot_new_index:
            right = pivot_new_index - 1
        else:
            left = pivot_new_index + 1


def PercentileWithSelectAlgorithm(scores, percentile_rank):
    u"""選択アルゴリズムを使って
    任意のパーセンタイル順位に対応する点数を返す
    """
    index = 80 * (len(scores) - 1) / 100
    return Select(scores, index)


class TestSample(unittest.TestCase):

    def test_case1(self):
        scores = [55, 56, 77, 88, 99]
        percentile_rank = PercentileRank(scores, 88)
        self.assertEquals(Percentile(scores, percentile_rank), 88)
        return

    def test_case2(self):
        scores = [55, 56, 77, 88, 99]
        percentile_rank = PercentileRank(scores, 88)
        self.assertEquals(
            PercentileWithSelectAlgorithm(scores, percentile_rank), 88)
        return


def main(name):
    suiteFew = unittest.TestSuite()
    suiteFew.addTest(unittest.makeSuite(TestSample))
    unittest.TextTestRunner(verbosity=2).run(suiteFew)

    return 0


if __name__ == '__main__':
    main(*sys.argv)
