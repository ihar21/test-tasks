import random


def generate_maze(width, height):
    if height % 2 != 0: height += 1
    maze = [["#" for _ in range(width + 1)] for _ in range(height + 1)]

    def recursive_backtracker(x, y):
        maze[y][x] = " "
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + 2 * dx, y + 2 * dy
            if 1 <= nx < width and 0 < ny < height + 1 and maze[ny][nx] == "#":
                maze[y + dy][x + dx] = " "
                recursive_backtracker(nx, ny)


    entry_position = random.randint(2, width - 1)
    maze[0][entry_position] = "E"

    exit_position = random.randint(2, width - 1)
    maze[height][exit_position] = "X"

    recursive_backtracker(entry_position, 1)
    maze[height - 1][exit_position] = " "

    def place_object(count, symbl):
        x = random.randint(1, width)
        y = random.randint(1, height)
        if count != 0:
            if maze[y][x] == " ":
                maze[y][x] = symbl
                count -= 1
            else:
                place_object(count, symbl)


    traps = random.randint(0, 5)
    place_object(traps, "^")

    treasure = random.randint(0, 1)
    place_object(treasure, "?")

    return maze, entry_position, exit_position