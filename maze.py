from tkinter import *
import random
import time

rows = 10
cols = 10
size = 50

root = Tk()

canvas = Canvas(root, width=500, height=500, bg="white")
canvas.pack()
# northWall stores top walls of each cell
north = []
# eastWall stores right walls of each cell
east = []
# visited checks if cell was already used
visit = []

for i in range(rows):

    north.append([])
    east.append([])
    visit.append([])

    for j in range(cols):

        north[i].append(1)
        east[i].append(1)
        visit[i].append(False)

def draw():
    canvas.delete("all")

    for i in range(rows):
        for j in range(cols):

            x = j * size
            y = i * size

            if north[i][j] == 1:
                canvas.create_line(x, y, x + size, y)

            if east[i][j] == 1:
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
        east[r][c] = 0

    if nr == r and nc == c - 1:
        east[nr][nc] = 0

    if nr == r + 1 and nc == c:
        north[nr][nc] = 0

    if nr == r - 1 and nc == c:
        north[r][c] = 0

def make():

    stack = []
    stack.append((0, 0))
    visit[0][0] = True

    while len(stack) > 0:

        r, c = stack[-1]

        next = []

        if r > 0 and visit[r - 1][c] == False:
            next.append((r - 1, c))

        if r < 9 and visit[r + 1][c] == False:
            next.append((r + 1, c))

        if c > 0 and visit[r][c - 1] == False:
            next.append((r, c - 1))

        if c < 9 and visit[r][c + 1] == False:
            next.append((r, c + 1))

        if len(next) > 0:

            nr, nc = random.choice(next)

            breakWall(r, c, nr, nc)

            visit[nr][nc] = True
            stack.append((nr, nc))

        else:
            stack.pop()

        draw()
        time.sleep(0.02)

def openWay(r, c, nr, nc):

    if nr == r and nc == c + 1:
        return east[r][c] == 0

    if nr == r and nc == c - 1:
        return east[nr][nc] == 0

    if nr == r + 1 and nc == c:
        return north[nr][nc] == 0

    if nr == r - 1 and nc == c:
        return north[r][c] == 0

def solve():

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
        time.sleep(0.05)

        if r == 9 and c == 9:
            return

        move = False

        if r > 0 and used[r - 1][c] == False and openWay(r, c, r - 1, c):
            stack.append((r - 1, c))
            move = True

        elif r < 9 and used[r + 1][c] == False and openWay(r, c, r + 1, c):
            stack.append((r + 1, c))
            move = True

        elif c > 0 and used[r][c - 1] == False and openWay(r, c, r, c - 1):
            stack.append((r, c - 1))
            move = True

        elif c < 9 and used[r][c + 1] == False and openWay(r, c, r, c + 1):
            stack.append((r, c + 1))
            move = True

        if move == False:

            canvas.create_oval(x - 7, y - 7, x + 7, y + 7, fill="blue")
            root.update()
            time.sleep(0.05)

            stack.pop()

make()
solve()

root.mainloop()