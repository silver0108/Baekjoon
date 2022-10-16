# 손익분기점

a, b, c = map(int, input().split())

if b >= c:
    print(-1)

else:
    print(a // (c - b) + 1)

    # 수입과 비용이 같아지는 경우

    # a + b * x = c * x
    # (c - b) * x = a
    # x = a / (c - b)
    # x + 1 일 경우 손익분기점 발생
