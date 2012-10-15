# -*- coding: utf-8-unix -*-
u"""演習問題 3-1 "Think Stats"

このプログラムの実行には http://thinkstats.com にて公開されている
以下のモジュールが必要：
 * Pmf.py
"""

import Pmf
import sys


def UnbiasPmf(observed):
    u"""観測値のPMFを取り、
    クラス規模の分布を見積もった新しいPmfオブジェクトを返す
    """
    # はて、どうやって見積もればよいのだ？
    return None


def MakeActualPmf():
    u"""学部長の観点から作成したPMFを返す
    """
    class_size = {
        7: 8,
        12: 8,
        17: 14,
        22: 4,
        27: 6,
        32: 12,
        37: 8,
        42: 3,
        47: 2
        }

    pmf = Pmf.MakePmfFromDict(class_size)

    pmf.Normalize()
    return pmf


def main(name):
    actual = MakeActualPmf()

    print "Mean: ", actual.Mean()
    print "Var:", actual.Var()

    return 0


if __name__ == '__main__':
    main(*sys.argv)
