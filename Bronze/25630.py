# 팰린드롬 소떡소떡

def Palindrome(string, first, last, cnt):
    if last <= first:
        return cnt
    elif string[first] != string[last]:
        string[last] = string[first]
        cnt += 1
        return Palindrome(string, first+1, last-1, cnt)
    else:
        return Palindrome(string, first+1, last-1, cnt)


n = int(input())
string = list(input())
cnt = 0

print(Palindrome(string, 0, n-1, cnt))
