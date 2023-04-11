# 분해합

N = int(input())

for i in range(N):  # 자연수 N의 생성자는 N보다 클 순 없으므로 N까지
    sum = 0  # 분해합을 저장하는 변수
    sum += i  # 생성자 자기 자신을 더함

    for j in range(len(str(i))):  # 생성자가 몇 자리수인지만큼
        sum += int(str(i)[j])  # 생성자의 각 자리수를 더함

    if sum == N:  # 분해합이 N과 같으면
        print(i)  # 생성자 출력
        break

if sum != N:  # 반복문을 다 돌았는데도 분해합이 N과 같지 않으면
    print(0)  # 0 출력
