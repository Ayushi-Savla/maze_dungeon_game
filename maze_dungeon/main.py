import math
import turtle
import random
from random import randint

#window setup
wn = turtle.Screen()
wn.bgcolor('black')
wn.title('Maze game')
wn.setup(700, 700)
wn.tracer(0)

images = ['wizard_right.gif', 'wizard_left.gif', 'treasure.gif', 'wall.gif', 'enemy_left.gif', 'enemy_right.gif']
for image in images:
    turtle.register_shape(image)

class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.color('white')
        self.penup()
        self.speed(0)

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('wizard_right.gif')
        self.color('blue')
        self.penup()
        self.speed(0)
        self.gold = 0

    def go_up(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor()

        self.shape('wizard_left.gif')

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor()

        self.shape('wizard_right.gif')

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def is_collision(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 5:
            return True
        else:
            return False

class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape('treasure.gif')
        self.color('gold')
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

class Enemy(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        self.shape('enemy_left.gif')
        self.color('red')
        self.penup()
        self.speed(0)
        self.gold = 25
        self.goto(x, y)
        self.direction = random.choice(['up', 'down', 'left', 'right'])

    def move(self):
        if self.direction == 'up':
            dx = 0
            dy = 24
        elif self.direction == 'down':
            dx = 0
            dy = -24
        elif self.direction == 'left':
            dx = -24
            dy = 0
            self.shape('enemy_left.gif')
        elif self.direction == 'right':
            dx = 24
            dy = 0
            self.shape('enemy_right.gif')
        else:
            dx = 0
            dy = 0

        move_to_x = self.xcor() + dx
        move_to_y = self.ycor() + dy

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            self.direction = random.choice(['up', 'down', 'left', 'right'])

        turtle.ontimer(self.move, t = randint(100, 300))

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

class HUD(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color('white')
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.goto(-280, 310)  # Position at the top of the screen
        self.timer = 60  # Countdown timer in seconds
        self.score = 0  # Current score
        self.level = 1  # Current level

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}   Level: {self.level}", font=("Arial", 16, "normal"))

    def decrement_timer(self):
        if self.timer > 0:
            self.timer -= 1
        self.update()

levels = [""]

level_1 = [
    "xxxxxxxxxxxxxxxxxxxxxxxxx",
    "xP xxxxxxx          xxxxx",
    "x  xxxxxxx  xxxxxx  xxxxx",
    "x       xx  xxxxxx  xxxxx",
    "x       xx  xxx        xx",
    "xxxxxx  xx  xxxE       xx",
    "xxxxxx  xx  xxxxxx  xxxxx",
    "xxxxxx  xx    xxxx  xxxxx",
    "x  xxx        xxxxT xxxxx",
    "x  xxx  xxxxxxxxxxxxxxxxx",
    "x         xxxxxxxxxxxxxxx",
    "x    T           xxxxxxxx",
    "xxxxxxxxxxxxT    xxxxx  x",
    "xxxxxxxxxxxxxxx  xxxxx  x",
    "xxx  xxxxxxxxxx         x",
    "xxx                     x",
    "xxxE       Txxxxxxxxxxxxx",
    "xxxxxxxxxx  xxxxxxxxxxxxx",
    "xxxxxxxxxx       E      x",
    "xx  xxxxxx              x",
    "xx  xxxxxxxxxxxxxx  xxxxx",
    "xxE  xxxxxxxxxxxxx  xxxxx",
    "xx          xxxx        x",
    "xxxx                    x",
    "xxxxxxxxxxxxxxxxxxxxxxxxx"
]

treasures = []
enemies = []

levels.append(level_1)

def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -288 + (x*24)
            screen_y = 288 - (y*24)

            if character == 'x':
                pen.goto(screen_x, screen_y)
                pen.shape('wall.gif')
                pen.stamp()
                #add coordinates to wall list
                walls.append((screen_x, screen_y))

            if character == 'P':
                player.goto(screen_x, screen_y)

            if character == 'T':
                treasures.append(Treasure(screen_x, screen_y))

            if character == 'E':
                enemies.append(Enemy(screen_x, screen_y))

pen = Pen()
player = Player()
hud = HUD()

hud.update()

#walls list
walls = []

#maze setup
setup_maze(levels[1])

#user interaction through keys
turtle.listen()
turtle.onkey(player.go_left, 'Left')
turtle.onkey(player.go_right, 'Right')
turtle.onkey(player.go_up, 'Up')
turtle.onkey(player.go_down, 'Down')

# Initialize timer
time_left = 60
# Timer display pen
timer_pen = turtle.Turtle()
timer_pen.hideturtle()
timer_pen.penup()
timer_pen.color("white")
timer_pen.goto(200, 310)  # Position the timer at the top of the screen

# Countdown function
def countdown():
    global time_left
    if time_left > 0:
        time_left -= 1
        timer_pen.clear()
        timer_pen.write(f"Time: {time_left}s", align="center", font=("Arial", 16, "bold"))
        turtle.ontimer(countdown, 1000)  # Call countdown every 1 second
    else:
        timer_pen.clear()
        timer_pen.write("Game Over!", align="center", font=("Arial", 24, "bold"))
        wn.update()
        turtle.ontimer(wn.bye, 3000)

countdown()

for enemy in enemies:
    turtle.ontimer(enemy.move, t = 250)

while True:
    for treasure in treasures:
        if player.is_collision(treasure):
            player.gold += treasure.gold
            hud.score += treasure.gold
            print("Player gold: {}".format(player.gold))
            treasure.destroy()
            treasures.remove(treasure)
            hud.update()
        # Check if all treasures are collected
        if not treasures:
            print("Mission Accomplished!")
            hud.clear()
            hud.goto(0, 0)
            hud.write("MISSION ACCOMPLISHED", align="center", font=("Arial", 24, "bold"))
            wn.update()
            turtle.bye()

    for enemy in enemies:
        if player.is_collision(enemy):
            print('Player dies!')
            hud.clear()
            hud.goto(0, 0)
            hud.write("GAME OVER", align="center", font=("Arial", 24, "bold"))
            wn.update()
            turtle.bye()
            break

    wn.update()