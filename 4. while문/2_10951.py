# A+B-4

while True:
    try:
        a ,b = map(int, input().split())
        print(a + b)
    # 예외처리(입력이 없을 경우)
    except: 
        break