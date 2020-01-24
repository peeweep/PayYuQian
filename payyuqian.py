#!/usr/bin/env python3

import decimal

# 于老师的工资规则:
# * 初始底薪 50000 欧元
# * 表现良好上涨工资17%
# * 12月双薪
# * 年底红包金额为当年收入的 4.7%

# 我们约定:
# * 自第二个月开始，每月皆涨工资
# * 1月开始上班
# * 2月过年
# * 第一年的2月就发红包
# * 全年收入累积至1月
# * 双倍工资包含涨的工资

BASE = decimal.Decimal(50000)  # 初始月薪
YEARS = 10  # 10年
TOTAL_PAY = BASE  # 共计工资初始化
THIS_YEAR = BASE  # 全年收入初始化
TOTAL_MONTH = 12 * YEARS

for i in range(TOTAL_MONTH - 1):
    if (i+2) % 12 == 2:
        red_pack = THIS_YEAR * decimal.Decimal(float(0.047))  # 过年发红包
        up_pay = BASE * decimal.Decimal(float(0.17))  # 涨工资
        THIS_YEAR = BASE  # 全年收入初始化
        TOTAL_PAY += BASE + up_pay + red_pack
    if (i+2) % 12 == 0:
        up_pay = BASE * decimal.Decimal(float(0.17))  # 涨工资
        THIS_YEAR += (BASE + up_pay) * 2
        TOTAL_PAY += (BASE + up_pay) * 2
    else:
        up_pay = BASE * decimal.Decimal(float(0.17))  # 涨工资
        THIS_YEAR += BASE + up_pay
        TOTAL_PAY += BASE + up_pay

print(round(TOTAL_PAY, 0))
