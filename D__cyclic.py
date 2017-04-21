__author__ = 'student'

a = input()
b = input()
n_a = len(a)            # len(a) = len(b)
s = b + '#' + a + a     # a, b consist of small latin letters

n = 3 * n_a + 1
z = [0] * n
left = right = 0
for i in range(1, n):
    x = min(z[i - left], right - i + 1) if i <= right else 0
    while i + x < n and s[x] == s[i + x]:
        x += 1
    z[i] = x
    if i > n_a and z[i] == n_a:
        print(i - n_a - 1)
        exit()
    if i + x - 1 > right:
        left, right = i, i + x - 1
else:
    print(-1)
