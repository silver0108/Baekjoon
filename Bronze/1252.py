# 이진수 덧셈
n1, n2 = input().split()

print(bin(int(n1, 2)+int(n2, 2))[2:])  # 0b 제외 슬라이싱
