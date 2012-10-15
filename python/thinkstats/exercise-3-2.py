# -*- coding: utf-8-unix -*-
u"""演習問題 3-2 "Think Stats"

このプログラムの実行には http://thinkstats.com にて公開されている
以下のモジュールが必要：
 * Pmf.py
 * relay.py
"""

import Pmf
import relay
import sys


def BiasPmf(pmf, speed):
    u"""各ランナーのスピードの実際の分布を表すPmfオブジェクトと、
    任意のスピードを受け取り、その速さで走る観測車から見たランナーの
    スピードの分布を表す新しいPmfオブジェクトを返す
    """
    biased = pmf.Copy()

    for val, bias in [(v, abs(v - speed)) for v in pmf.Values()]:
        biased.Mult(val, bias)

    biased.Normalize()
    return biased


def main(name):
    results = relay.ReadResults()
    speeds = relay.GetSpeeds(results)
    pmf = Pmf.MakePmfFromList(speeds, 'speeds')

    biased = BiasPmf(pmf, 7.5)

    biased.Print()

    return 0


if __name__ == '__main__':
    main(*sys.argv)
