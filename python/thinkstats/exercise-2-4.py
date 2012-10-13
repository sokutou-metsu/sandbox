# -*- coding: utf-8-unix -*-
u"""演習問題 2-4 "Think Stats"

このプログラムの実行には http://thinkstats.com にて公開されている
以下のモジュールが必要：
 * Pmf.py
"""

import Pmf


def PmfRemainingLifeTime(pmf, age):
    """耐用年数のPmfと使用年数を取り、
    残りの耐用年数の分布を表す新しいPmfを返す
    """
    life = Pmf.Pmf()

    for x in [i for i in pmf.Values() if i > age]:
        life.Set(x - age, pmf.Prob(x))

    life.Normalize()
    return life


def PrintLife(pmf):
    """確率質量関数の質量分布を表示する
    """
    for x in pmf.Items():
        print '  (', x[0], ') ', x[1]


def main():
    pmf = Pmf.MakePmfFromList([3, 4, 1, 10, 6, 3, 5, 7, 3, 4])
    print '[Original]'
    PrintLife(pmf)

    life = PmfRemainingLifeTime(pmf, 3)
    print '[Remaining]'
    PrintLife(life)

    return 0


if __name__ == '__main__':
    main()
