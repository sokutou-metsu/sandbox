# -*- coding: utf-8-unix -*-
u"""演習問題 1-3 "Think Stats"

このプログラムの実行には http://thinkstats.com にて公開されている
以下のモジュールが必要：
 * survey.py
 * thinkstats.py
"""

import math
import survey
import sys
from thinkstats import Mean, Var


def IsLiveBirth(record):
    u"""レコードが生児出生のものかどうか
    """
    return record.outcome == 1


def IsFirstBirth(record):
    u"""レコードが第一子のものかどうか
    """
    return IsLiveBirth(record) and record.birthord == 1


def IsOtherBirth(record):
    u"""レコードが第二子以降のものかどうか
    """
    return IsLiveBirth(record) and record.birthord != 1


def FilterTable(table, cond):
    u"""条件に合わせてデータを抽出する
    """
    match = survey.Pregnancies()
    match.ExtendRecords(filter(cond, table.records))
    return match


def MakeTables(data_dir):
    u"""データファイルから妊娠テーブルを読み込んで、
    生児出生すべて、第一子、第二子以降のグループに分類したものを返す
    """
    table = survey.Pregnancies()
    table.ReadRecords(data_dir)

    live_birth = FilterTable(table, IsLiveBirth)
    first_birth = FilterTable(table, IsFirstBirth)
    other_birth = FilterTable(table, IsOtherBirth)

    return live_birth, first_birth, other_birth


def FetchPrgLengthInfo(table):
    u"""妊娠期間についてレコード数、平均値、分散を求めて返す
    """
    info = {}

    prg_length = map(lambda r: r.prglength, table.records)

    info['length'] = len(table)
    info['mean'] = Mean(prg_length)
    info['var'] = Var(prg_length)

    return info


def Task(data_dir):
    u"""課題用
    """
    live_birth, first_birth, other_birth = MakeTables(data_dir)

    info = {}
    info['live_birth'] = FetchPrgLengthInfo(live_birth)
    info['first_birth'] = FetchPrgLengthInfo(first_birth)
    info['other_birth'] = FetchPrgLengthInfo(other_birth)

    return info


def main(name, data_dir='.'):
    info = Task(data_dir)

    print u'生児出生数： ', info['live_birth']['length']

    first_birth = info['first_birth']
    print u'第一子：',
    print first_birth['mean'],
    print first_birth['length'],
    print math.sqrt(first_birth['var'])

    other_birth = info['other_birth']
    print u'第二子以降：',
    print other_birth['mean'],
    print other_birth['length'],
    print math.sqrt(other_birth['var'])

    diff_mean = (first_birth['mean'] - other_birth['mean']) * 7
    diff_std_dev = math.sqrt(first_birth['var']) - math.sqrt(other_birth['var'])
    print u'妊娠日数の差： ', diff_mean, diff_std_dev

    return 0


if __name__ == '__main__':
    main(*sys.argv)
