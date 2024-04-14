import os
from colorama import Fore, init, Style
import maze_generation

def print_maze(maze):
    for row in maze:
        for sym in row:
            color = {
                "p": Fore.GREEN,
                "X": Fore.YELLOW,
                "E": Fore.MAGENTA,
                "^": Fore.RED,
                "?": Fore.YELLOW
            }.get(sym, "")
            print(f"{color}{sym}{Style.RESET_ALL}", end=" ")
        print("")

def main():
    init()
    width = int(input("Width:"))
    height = int(input("Height:"))
    hp = 3
    maze, entr, exit = maze_generation.generate_maze(width, height)
    plr_x, plr_y = entr, 1
    maze[plr_y][plr_x] = "p"
    print_maze(maze)

    def play():
        nonlocal plr_x, plr_y, maze, hp
        direction = input("Next direction (r, l, u, d):").lower()

        def move(x_move, y_move):
            nonlocal plr_x, plr_y, maze, hp
            new_x, new_y = plr_x + x_move, plr_y + y_move
            cell = maze[new_y][new_x]

            if cell == " ":
                maze[plr_y][plr_x] = " "
                maze[new_y][new_x] = "p"
                plr_x, plr_y = new_x, new_y
            elif cell == "?":
                maze[plr_y][plr_x] = " "
                maze[new_y][new_x] = "p"
                plr_x, plr_y = new_x, new_y
                print("Congratulations! You pick up the treasure!")
            elif cell == "^":
                maze[plr_y][plr_x] = " "
                maze[new_y][new_x] = "p"
                plr_x, plr_y = new_x, new_y
                print("You step in trap. -1hp")
                nonlocal hp
                hp -= 1
                if hp <= 0:
                    print("You lost all your HP. Game end")
                    return
            elif cell == "X":
                print("You pass the maze")
                return
            else:
                print("Wall. Choose another direction")

            print("HP:", hp)
            print_maze(maze)
            play()

        if direction in ("r", "l", "u", "d"):
            if plr_y < height + 1:
                if direction == "u":
                    move(0, -1)
                elif direction == "d":
                    move(0, 1)
                elif direction == "r":
                    move(1, 0)
                elif direction == "l":
                    move(-1, 0)
        else:
            print("Wrong input")
            print("HP:", hp)
            print_maze(maze)
            play()

    play()
    input("exit")

if __name__ == "__main__":
    main()
