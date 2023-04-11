# 꿀벌

import sys

work = {"Re": 0, "Pt": 0, "Cc": 0, "Ea": 0, "Tb": 0, "Cm": 0, "Ex": 0}
cnt = 0
do_work_input = sys.stdin.readlines()

for line in do_work_input:
    do_work = list(line.split())

    for i in do_work:
        if i in work.keys():
            work[i] += 1
        cnt += 1


for key, value in work.items():
    print(key, value, "{:.2f}".format(value/cnt))

print("Total", cnt, "1.00")
