from tkinter import *
import random
import time

rows = 10
cols = 10
size = 50

root = Tk()
root.title("Maze Project")

canvas = Canvas(root, width=500, height=500, bg="white")
canvas.pack()

# northWall stores top walls
northWall = []

# eastWall stores right walls
eastWall = []

# visited checks used cells
visited = []

for i in range(rows):
    northWall.append([])
    eastWall.append([])
    visited.append([])

    for j in range(cols):
        northWall[i].append(1)
        eastWall[i].append(1)
        visited[i].append(False)

def draw():

    canvas.delete("all")

    for i in range(rows):
        for j in range(cols):

            x = j * size
            y = i * size

            if northWall[i][j] == 1:
                canvas.create_line(x, y, x + size, y)

            if eastWall[i][j] == 1:
                canvas.create_line(x + size, y, x + size, y + size)

            if j == 0:
                canvas.create_line(x, y, x, y + size)

            if i == rows - 1:
                canvas.create_line(x, y + size, x + size, y + size)

    canvas.create_line(0, 0, 0, 50, fill="white", width=3)
    canvas.create_line(500, 450, 500, 500, fill="white", width=3)

    root.update()

def breakWall(r, c, nr, nc):

    if nr == r and nc == c + 1:
        eastWall[r][c] = 0

    if nr == r and nc == c - 1:
        eastWall[nr][nc] = 0

    if nr == r + 1 and nc == c:
        northWall[nr][nc] = 0

    if nr == r - 1 and nc == c:
        northWall[r][c] = 0

def makeMaze():

    stack = []
    stack.append((0, 0))
    visited[0][0] = True

    while len(stack) > 0:

        r, c = stack[-1]

        nextCells = []

        if r > 0 and visited[r - 1][c] == False:
            nextCells.append((r - 1, c))

        if r < rows - 1 and visited[r + 1][c] == False:
            nextCells.append((r + 1, c))

        if c > 0 and visited[r][c - 1] == False:
            nextCells.append((r, c - 1))

        if c < cols - 1 and visited[r][c + 1] == False:
            nextCells.append((r, c + 1))

        if len(nextCells) > 0:

            nr, nc = random.choice(nextCells)

            breakWall(r, c, nr, nc)

            visited[nr][nc] = True
            stack.append((nr, nc))

        else:
            stack.pop()

        draw()
        time.sleep(0.08)

def canMove(r, c, nr, nc):

    if nr == r and nc == c + 1:
        return eastWall[r][c] == 0

    if nr == r and nc == c - 1:
        return eastWall[nr][nc] == 0

    if nr == r + 1 and nc == c:
        return northWall[nr][nc] == 0

    if nr == r - 1 and nc == c:
        return northWall[r][c] == 0

def solveMaze():

    used = []

    for i in range(rows):
        used.append([])

        for j in range(cols):
            used[i].append(False)

    stack = []
    stack.append((0, 0))

    while len(stack) > 0:

        r, c = stack[-1]
        used[r][c] = True

        x = c * 50 + 25
        y = r * 50 + 25

        canvas.create_oval(x - 7, y - 7, x + 7, y + 7, fill="red")
        root.update()
        time.sleep(0.12)

        if r == 9 and c == 9:
            return

        move = False

        if r > 0 and used[r - 1][c] == False and canMove(r, c, r - 1, c):
            stack.append((r - 1, c))
            move = True

        elif r < 9 and used[r + 1][c] == False and canMove(r, c, r + 1, c):
            stack.append((r + 1, c))
            move = True

        elif c > 0 and used[r][c - 1] == False and canMove(r, c, r, c - 1):
            stack.append((r, c - 1))
            move = True

        elif c < 9 and used[r][c + 1] == False and canMove(r, c, r, c + 1):
            stack.append((r, c + 1))
            move = True

        if move == False:

            canvas.create_oval(x - 7, y - 7, x + 7, y + 7, fill="blue")
            root.update()
            time.sleep(0.12)

            stack.pop()

makeMaze()
solveMaze()

root.mainloop()