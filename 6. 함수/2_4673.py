# 셀프 넘버

lst = []
for i in range(1, 10001):
  sum = i
  for j in range(len(str(i))): # 숫자 길이만큼
    sum += int(str(i)[j]) # ex) sum = sum + sum[0] + sum[1]
  lst.append(sum)

for i in range(1, 10001):
  if i not in lst:
    print(i) 
