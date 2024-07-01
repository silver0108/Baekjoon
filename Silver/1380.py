# 귀걸이
case = 1

while(1):
  n = int(input())
  if(n == 0):
    break
  
  name_list = []
  for i in range(n):
    name_list.append(input())
  
  array = []
  for i in range(2*n-1):
    num, alpha = input().split()
    array.append(int(num))

  for i in range(1, n+1):
    if(array.count(i) == 1):
      print(case, name_list[i-1])

  case += 1