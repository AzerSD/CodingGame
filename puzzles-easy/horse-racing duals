n = int(input())
pi = []
for i in range(n):
    pi.append(int(input()))

pi.sort()

min_diff = abs(pi[0] - pi[1])

for i in range(1, n - 1):
    diff = abs(pi[i] - pi[i+1])
    if diff < min_diff:
        min_diff = diff

print(min_diff)

