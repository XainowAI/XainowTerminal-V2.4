import tkinter as tk
import random
import time


root = tk.Tk()
root.title("Snake bêta By Owner#2624 [Stable]")
size = (400, 400)

canvas = tk.Canvas(root, width=size[0], height=size[1], bg="black")
canvas.pack()

snake_pos = [size[0]//2, size[1]//2]
snake_body = [[size[0]//2, size[1]//2], [size[0]//2-10, size[1]//2], [size[0]//2-20, size[1]//2]]
snake_dir = "right"

food_pos = [random.randint(0, size[0]-10), random.randint(0, size[1]-10)]
score = 0
game_over = False

def cheat_code(event):
    global score
    cheat = entry.get()
    if cheat == "123":
        score = 145
        entry.delete(0, 'end')

entry = tk.Entry(root)
entry.pack()
root.bind("<Return>", cheat_code)



time.sleep(1.5)
def draw_snake():
    for pos in snake_body:
        canvas.create_rectangle(pos[0], pos[1], pos[0]+10, pos[1]+10, fill="orange")

def move_snake():
    global game_over, score
    new_head = [snake_body[0][0], snake_body[0][1]]
    if snake_dir == "right":
        new_head[0] += 10
    elif snake_dir == "left":
        new_head[0] -= 10
    elif snake_dir == "up":
        new_head[1] -= 10
    elif snake_dir == "down":
        new_head[1] += 10
    snake_body.insert(0, new_head)
    if new_head[0] < 0 or new_head[0] >= size[0] or new_head[1] < 0 or new_head[1] >= size[1]:
        game_over = True
    if snake_body[0] in snake_body[1:]:
        game_over = True
    if new_head[0] >= food_pos[0] and new_head[0] <= food_pos[0] + 10 and new_head[1] >= food_pos[1] and new_head[1] <= food_pos[1] + 10:
        food_pos[0] = random.randint(0, size[0]-10)
        food_pos[1] = random.randint(0, size[1]-10)
        canvas.delete(food)
        score += 1
    else:
        snake_body.pop()

def game_loop():
    global game_over
    if not game_over:
        canvas.delete("all")
        move_snake()
        food = canvas.create_rectangle(food_pos[0], food_pos[1], food_pos[0]+10, food_pos[1]+10, fill="red")
        draw_snake()
        canvas.create_text(20, 20, text="                        Score: " + str(score), font=("Arial", 14), fill="white")
        if score >= 150:
            canvas.create_text(size[0]//2, size[1]//2 + 50, text="Félicitations!", font=("Arial", 24), fill="white")
        canvas.update()
        root.after(100, game_loop)
    else:
        canvas.create_text(size[0]//2, size[1]//2, text="Game Over!", font=("Arial", 24), fill="red")



def move_left(event):
    global snake_dir
    snake_dir = "left"

def move_right(event):
    global snake_dir
    snake_dir = "right"

def move_up(event):
    global snake_dir
    snake_dir = "up"

def move_down(event):
    global snake_dir
    snake_dir = "down"



root.bind("<Left>", move_left)
root.bind("<Right>", move_right)
root.bind("<Up>", move_up)
root.bind("<Down>", move_down)

draw_snake()
food = canvas.create_rectangle(food_pos[0], food_pos[1], food_pos[0]+10, food_pos[1]+10, fill="red")


game_loop()
root.mainloop()
