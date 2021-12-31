# 더하기 사이클

n = int(input())
new = n
count = 0

while True:
    a  = new // 10
    b = new % 10
    hap = (a + b) % 10
    new = b * 10 + hap
    count += 1

    if n == new:
        print(count)
        break