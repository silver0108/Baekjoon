# 크냐?

while(1):
    n1, n2 = map(int, input().split())
    if n1 == n2 == 0:
        break
    if(n1 > n2):
        print("Yes")
    else:
        print("No")
