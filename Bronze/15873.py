# 공백 없는 A+B

num = input()

if len(num) == 4:
  print(int(num[:2]) + int(num[1:]))
elif len(num) == 3:
  if num[1] == "0":
    print(int(num[:2]) + int(num[2:]))
  else:
    print(int(num[:1]) + int(num[1:]))
else:
  print(int(num[0]) + int(num[1]))
 