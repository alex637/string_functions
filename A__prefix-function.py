__author__ = 'student'

s = input()
n = len(s)
pi = [0] * n    # result of the prefix-function
for i in range(1, n):
    j = pi[i - 1]
    while j > 0 and s[i] != s[j]:
        j = pi[j - 1]
    if s[i] == s[j]:
        pi[i] = j + 1

print(" ".join(map(str, pi)))
