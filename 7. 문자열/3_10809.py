# 알파벳 찾기

import sys

s = sys.stdin.readline()
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in alphabet:
    print(s.find(i), end=' ')
