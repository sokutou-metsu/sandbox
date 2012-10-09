# -*- coding: utf-8-unix -*-
u"""演習問題 1-3 "Think Stats"

このプログラムの実行には http://thinkstats.com にて公開されている
以下のモジュールが必要：
 * survey.py
"""

import math
import survey
import sys
from thinkstats import Mean, Var


def is_outcome(record):
    u"""レコードが生児出生のものかどうか"""
    return record.outcome == 1


def is_first_birth(record):
    u"""レコードが第一子のものかどうか"""
    return is_outcome(record) and record.birthord == 1


def is_not_first_birth(record):
    u"""レコードが第二子以降のものかどうか"""
    return is_outcome(record) and record.birthord != 1


def fetch_avg_prglength(table, cond=is_outcome):
    u"""条件に合うレコードの数と妊娠期間を求める"""
    match = survey.Pregnancies()
    match.ExtendRecords(filter(cond, table.records))
    prglength = map(lambda r: r.prglength, match.records)
    return (len(match), Mean(prglength), math.sqrt(Var(prglength)))


def main(name, data_dir='.'):
    table = survey.Pregnancies()
    table.ReadRecords(data_dir)
    print u'妊娠レコードの総数：', len(table.records)

    outcome = fetch_avg_prglength(table)
    print u'生児出生数： ', outcome[0]

    first_birth = fetch_avg_prglength(table, is_first_birth)
    print u'第一子： ', first_birth[1], first_birth[0], first_birth[2]

    the_other = fetch_avg_prglength(table, is_not_first_birth)
    print u'第二子以降： ', the_other[1], the_other[0], the_other[2]

    diff_mean = (first_birth[1] - the_other[1]) * 7
    diff_std_dev = first_birth[2] - the_other[2]
    print u'妊娠日数の差： ', diff_mean, diff_std_dev

    return 0


if __name__ == '__main__':
    main(*sys.argv)
