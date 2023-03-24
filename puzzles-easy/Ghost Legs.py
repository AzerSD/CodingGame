w, h = map(int, input().split())
grid = [input() for _ in range(h)]

top_labels = [grid[0][i] for i in range(0, w, 3)]
bottom_labels = [grid[h-1][i] for i in range(0, w, 3)]

for i, label in enumerate(top_labels):
    x = i * 3
    y = 1
    while y < h-1:
        if x >= 0 and grid[y][x-1] == '-':
            x -= 3
        elif x < w-1 and grid[y][x+1] == '-':
            x += 3
        y += 1
    print(f"{label}{bottom_labels[x // 3]}")

