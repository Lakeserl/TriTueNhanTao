def find_max_dust_location(grid):
    max_dust = -1
    max_location = (-1, -1)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] > max_dust:
                max_dust = grid[i][j]
                max_location = (i, j)

    return max_location

def move_to_location(x, y ):
    print(f"Di chuyển đén vị trí ({x}, {y})")

def vaccum_to_location(x, y):
    print(f"Di chuyển máy hút bụi đến vị trí chỉ định ({x}, {y})")

grid = [
    [1, 3, 7, 5, 2],
    [8, 5, 4, 3, 6],
    [6, 8, 9, 2, 7],
]

max_x, max_y = find_max_dust_location(grid)

move_to_location(max_x, max_y)
vaccum_to_location(max_x, max_y)