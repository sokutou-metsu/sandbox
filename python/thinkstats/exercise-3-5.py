# -*- coding: utf-8-unix -*-
u"""演習問題 3-5 "Think Stats"

このプログラムの実行には http://thinkstats.com にて公開されている
以下のモジュールが必要：
 * Cdf.py
 * myplot.py
 * Pmf.py
 * relay.py
"""

import Cdf
import myplot
import Pmf
import relay
import sys


def main(name):
    results = relay.ReadResults()
    speeds = relay.GetSpeeds(results)

    cdf = Cdf.MakeCdfFromList(speeds, 'speeds')
    myplot.Cdf(cdf)
    myplot.Show(title='Cdf of running speed',
                xlabel='speed (mph)',
                ylabel='probability')
    
    pmf = Pmf.MakePmfFromList(speeds, 'speeds')
    myplot.Pmf(pmf)
    myplot.Show(title='PMF of running speed',
                xlabel='speed (mph)',
                ylabel='probability')

    return 0


if __name__ == '__main__':
    main(*sys.argv)
