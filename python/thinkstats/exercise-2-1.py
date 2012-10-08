# -*- coding: utf-8-unix -*-
u"""演習問題 2-1 "Think Stats"

このプログラムの実行には http://thinkstats.com にて公開されている
以下のモジュールが必要：
 * thinkstats.py
"""

from math import sqrt
from thinkstats import MeanVar


def Pumpkin(weights):
    (mean, variance) = MeanVar(weights)
    return {'mean': mean,
            'variance': variance,
            'std-deviation': sqrt(variance)}


def main():
    weights = [0.5, 0.5, 1.5, 1.5, 96]
    ret = Pumpkin(weights)

    print u'算術平均： ', ret['mean']
    print u'分散　　： ', ret['variance']
    print u'標準偏差： ', ret['std-deviation']

    return 0


if __name__ == '__main__':
    main()
