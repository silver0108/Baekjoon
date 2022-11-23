# 팰린드롬수

def Palindrome(n, first, last):
    if last <= first:
        print("yes")
    elif n[first] != n[last]:
        print("no")
    else:
        return Palindrome(n, first+1, last-1)


while(True):
    n = input()
    size = len(n)

    if n == "0":
        break
    else:
        Palindrome(n, 0, size-1)
