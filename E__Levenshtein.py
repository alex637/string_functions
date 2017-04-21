__author__ = 'student'

s1 = input()
s2 = input()


def levenshtein(a, b):
    n = len(a)
    m = len(b)
    matrix = [[None for j in range(m)] for i in range(n)]
    matrix[0] = [i for i in range(m)]
    for i in range(1, n):
        matrix[i][0] = i
    for i in range(1, n):
        for j in range(1, m):
            if a[i] == b[j]:
                matrix[i][j] = matrix[i - 1][j - 1]
            else:
                matrix[i][j] = 1 + min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1])
    return matrix[n - 1][m - 1]

print(levenshtein(s1, s2))
