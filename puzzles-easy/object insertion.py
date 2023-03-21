def count_fits(object_lines, grid_lines):
    grid_height = len(grid_lines)
    grid_width = len(grid_lines[0])

    object_height = len(object_lines)
    object_width = len(object_lines[0])

    fit_count = 0
    for i in range(grid_height - object_height + 1):
        for j in range(grid_width - object_width + 1):
            fits = True
            for k in range(object_height):
                for l in range(object_width):
                    if grid_lines[i + k][j + l] != "." and object_lines[k][l] != ".":
                        fits = False
                        break
                if not fits:
                    break
            if fits:
                fit_count += 1

    return fit_count


def place_object(object_lines, grid_lines):
    fit_count = count_fits(object_lines, grid_lines)

    if fit_count == 1:
        for i in range(len(grid_lines) - len(object_lines) + 1):
            for j in range(len(grid_lines[0]) - len(object_lines[0]) + 1):
                fits = True
                for k in range(len(object_lines)):
                    for l in range(len(object_lines[0])):
                        if grid_lines[i + k][j + l] != "." and object_lines[k][l] != ".":
                            fits = False
                            break
                    if not fits:
                        break
                if fits:
                    print(fit_count)
                    for k in range(len(object_lines)):
                        for l in range(len(object_lines[0])):
                            if object_lines[k][l] == "*":
                                grid_lines[i + k] = grid_lines[i + k][:j + l] + "*" + grid_lines[i + k][j + l + 1:]
                    break
            if fits:
                break
        for line in grid_lines:
            print(line)
    else:
        print(fit_count)


if __name__ == "__main__":
    a, b = map(int, input().split())
    object_lines = [input().strip() for _ in range(a)]
    object_str = '\n'.join(object_lines)

    c, d = map(int, input().split())
    grid_lines = [input().strip() for _ in range(c)]
    grid_str = '\n'.join(grid_lines)

    place_object(object_lines, grid_lines)

