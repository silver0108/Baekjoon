# 달팽이는 올라가고 싶다

import math

a, b, v = map(int, input().split())

# 총 높이에서 낮에 올라갈 수 있는 높이를 먼저 빼줌
x = v - a 

# a와 b의 차가 x만큼 올라가는데 최소 며칠 걸리는지 구한 다음,
# 다음날 낮에 올라가는 높이를 총 높이에서 미리 빼줬으니까 하루 만큼을 더해줌
print(math.ceil(x / (a - b)) + 1)  # math.ceil은 math 모듈의 소수점 올림 함수