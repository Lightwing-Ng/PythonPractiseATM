# -*- coding:utf-8 -*-
# Author: Lightwing Ng

def formatNum(num):  # 1234 -> 1,234
    num = str(num)
    result = ''
    count = 0
    for i in num[::-1]:
        count += 1
        result += i
        if count % 3 == 0:
            result += ','
    return result[::-1].strip(',')


def formatCardNum(num):
    num = str(num)
    result = ''
    count = 0
    for i in num[::-1]:
        count += 1
        result += i
        if count % 4 == 0:
            result += ' '
    return result[::-1].strip(' ')


def formatDate(str):
    DigMon = {
        '01': 'JAN',
        '02': 'FEB',
        '03': 'MAR',
        '04': 'APR',
        '05': 'MAY',
        '06': 'JUN',
        '07': 'JUL',
        '08': 'AUG',
        '09': 'SEP',
        '10': 'OCT',
        '11': 'NOV',
        '12': 'DEC',
    }
