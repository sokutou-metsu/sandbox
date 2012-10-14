# -*- coding: utf-8-unix -*-
u"""演習問題 2-6 "Think Stats"

このプログラムの実行には http://thinkstats.com にて公開されている
以下のモジュールが必要：
 * Pmf.py
 * survey.py
 * thinkstats.py
"""

import first
import Pmf
import sys


def ProbRange(pmf, bin):
    u"""Pmfオブジェクトとビンの範囲を取って、
    ビンに相当する出産の割合を返す
    """
    return sum(map(lambda x: pmf.Prob(x), bin))


def ProbEarly(pmf):
    u"""Pmfオブジェクトを取って、早産の割合を返す
    """
    return ProbRange(pmf, range(0, 38))


def ProbOnTime(pmf):
    u"""Pmfオブジェクトを取って、標準の割合を返す
    """
    return ProbRange(pmf, range(38, 41))


def ProbLate(pmf):
    u"""Pmfオブジェクトを取って、遅産の割合を返す
    """
    return ProbRange(pmf, range(41, 60))


def MakePrgLengthPmf(table):
    u"""妊娠期間のPmfオブジェクトを作成する
    """
    return Pmf.MakePmfFromList(map(lambda r: r.prglength, table.records))


def ComputeProb(table):
    u"""早産、標準、遅産の確率を計算する
    """
    pmf = MakePrgLengthPmf(table)

    prob = {}
    prob["early"] = ProbEarly(pmf)
    prob["on_time"] = ProbOnTime(pmf)
    prob["late"] = ProbLate(pmf)

    return prob


def PrintResult(result):
    u"""結果を表示する
    """
    print u"早産 ", result["early"]
    print u"標準 ", result["on_time"]
    print u"遅産 ", result["late"]


def ComputeRelativeRisk(prob1, prob2):
    u"""相対危険度を計算する
    """
    result = {}

    result["early"] = prob1["early"] / prob2["early"]
    result["on_time"] = prob1["on_time"] / prob2["on_time"]
    result["late"] = prob1["late"] / prob2["late"]

    return result


def main(name, data_dir='.'):
    live_birth, first_birth, other_birth = first.MakeTables(data_dir)

    prob = {}
    prob["live_birth"] = ComputeProb(live_birth)
    prob["first_birth"] = ComputeProb(first_birth)
    prob["other_birth"] = ComputeProb(other_birth)

    print u"[第一子]"
    PrintResult(prob["first_birth"])

    print u"[第二子以降]"
    PrintResult(prob["other_birth"])

    print u"[すべての生児出生]"
    PrintResult(prob["live_birth"])

    print u"[相対危険度]"
    PrintResult(ComputeRelativeRisk(prob["first_birth"], prob["other_birth"]))

    return 0


if __name__ == '__main__':
    main(*sys.argv)
