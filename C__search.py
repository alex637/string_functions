__author__ = 'student'

substr = input()
string = input()
s = substr + '#' + string       # only small letters in string and substring

n = len(s)
n_sub = len(substr)
z = [0] * n
occurrences = []
left = right = 0
for i in range(1, n):
    x = min(z[i - left], right - i + 1) if i <= right else 0
    while i + x < n and s[x] == s[i + x]:
        x += 1
    z[i] = x
    if i > n_sub and z[i] == n_sub:
        occurrences.append(i - n_sub - 1)
    if i + x - 1 > right:
        left, right = i, i + x - 1

if not occurrences:
    print(-1)
else:
    print(" ".join(map(str, occurrences)))
