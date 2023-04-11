# 상근날드

sd = int(input())
jd = int(input())
hd = int(input())
coke = int(input())
cider = int(input())

buger = min(sd, jd, hd)
beverage = min(coke, cider)

print(buger + beverage - 50)
