width = int(input())
height = int(input())


def search_island(island_map, x, y):
    visited = [[False] * width for _ in range(height)]
    queue = [(x, y)]
    area = 0

    while queue:
        cell_x, cell_y = queue.pop()
        if not visited[cell_y][cell_x] and island_map[cell_y][cell_x] == 'O':
            visited[cell_y][cell_x] = True
            area += 1

            neighbors = [(cell_x-1, cell_y), (cell_x+1, cell_y),
                    (cell_x, cell_y-1), (cell_x, cell_y+1)]
            for n_x, n_y in neighbors:
                if 0 <= n_x < width and 0 <= n_y < height and not visited[n_y][n_x] and island_map[n_y][n_x] == 'O':
                    queue.append((n_x, n_y))
    return area


island_map = []
for i in range(height):
    row = input()
    island_map.append(row)

num_queries = int(input())
for _ in range(num_queries):
    x, y = map(int, input().split())
    print(search_island(island_map, x, y))
