# -*- coding: utf-8-unix -*-
u"""演習問題 1-3 "Think Stats"

このプログラムの実行には http://thinkstats.com にて公開されている
以下のモジュールが必要：
 * survey.py
"""

import survey
import sys


def is_outcome(record):
    u"""レコードが生児出生のものかどうか"""
    return record.outcome == 1


def is_first_birth(record):
    u"""レコードが第一子のものかどうか"""
    return is_outcome(record) and record.birthord == 1


def is_not_first_birth(record):
    u"""レコードが第二子以降のものかどうか"""
    return is_outcome(record) and record.birthord != 1


def mean(data):
    u"""算術平均を求める"""
    return float(reduce(lambda s, x: s + x, data, 0)) / len(data)


def fetch_avg_prglength(table, cond=is_outcome):
    u"""条件に合うレコードの数と妊娠期間を求める"""
    match = filter(cond, table.records)
    avg_prglength = mean(map(lambda r: r.prglength, match))
    return (len(match), avg_prglength)


def main(name, data_dir='.'):
    table = survey.Pregnancies()
    table.ReadRecords(data_dir)
    print u'妊娠レコードの総数：', len(table.records)

    outcome = fetch_avg_prglength(table)
    print u'生児出生数： ', outcome[0]

    first_birth = fetch_avg_prglength(table, is_first_birth)
    print u'第一子： ', first_birth[1], first_birth[0]

    the_other = fetch_avg_prglength(table, is_not_first_birth)
    print u'第二子以降： ', the_other[1], the_other[0]

    print u'妊娠日数の差： ', (first_birth[1] - the_other[1]) * 7

    return 0


if __name__ == '__main__':
    main(*sys.argv)
