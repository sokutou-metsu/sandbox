# -*- coding: utf-8-unix -*-
u"""演習問題 2-7 "Think Stats"

このプログラムの実行には http://thinkstats.com にて公開されている
以下のモジュールが必要：
 * Pmf.py
 * survey.py
 * thinkstats.py
"""

import first
import risk
import Pmf
import sys


def ConditionalPmf(pmf, condition):
    u"""Pmfオブジェクトから条件付きPMFを作成する
    """
    cond_pmf = pmf.Copy()

    for x in [v for v in pmf.Values() if not condition(v)]:
        cond_pmf.Remove(x)

    cond_pmf.Normalize()
    return cond_pmf


def ProbOnWeek(pmf, x):
    u"""X週までに赤ちゃんが生まれなかった時にX週で生まれる確率を求める
    """
    return ConditionalPmf(pmf, lambda v: v >= x).Prob(x)


def Task(table):
    u"""課題用
    """
    pmf = risk.MakePrgLengthPmf(table)
    return [(x, ProbOnWeek(pmf, x)) for x in range(35, 46)]


def PrintResult(result):
    u"""結果を表示する
    """
    for x, prob in result:
        print '[', x ,']', prob


def main(name, data_dir='.'):
    live_birth, first_birth, other_birth = first.MakeTables(data_dir)

    print u"[第一子]"
    PrintResult(Task(first_birth))

    print u"[第二子以降]"
    PrintResult(Task(other_birth))

    return 0


if __name__ == '__main__':
    main(*sys.argv)
