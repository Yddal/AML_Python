# Snake minigame using the standard library `turtle` module
# Run this file (not a file named `turtle.py`) to avoid shadowing the stdlib module.

import turtle
import random
import time

STEP = 20  # movement step size


def main():
    # Screen setup
    screen = turtle.Screen()
    screen.title("Snake - Minigame")
    screen.bgcolor("black")
    screen.setup(width=600, height=600)
    screen.tracer(0)  # turn off automatic animation

    # Snake head
    head = turtle.Turtle()
    head.shape("square")
    head.color("green")
    head.penup()
    head.goto(0, 0)
    head.direction = "stop"

    # Food
    food = turtle.Turtle()
    food.shape("circle")
    food.color("red")
    food.penup()
    food.goto(0, 100)

    segments = []

    # Score display
    score = 0
    high_score = 0
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.color("white")
    pen.goto(0, 260)
    pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 16, "normal"))

    # Movement functions
    def go_up():
        if head.direction != "down":
            head.direction = "up"

    def go_down():
        if head.direction != "up":
            head.direction = "down"

    def go_left():
        if head.direction != "right":
            head.direction = "left"

    def go_right():
        if head.direction != "left":
            head.direction = "right"

    def move():
        x = head.xcor()
        y = head.ycor()
        if head.direction == "up":
            head.sety(y + STEP)
        if head.direction == "down":
            head.sety(y - STEP)
        if head.direction == "left":
            head.setx(x - STEP)
        if head.direction == "right":
            head.setx(x + STEP)

    # Keyboard bindings
    screen.listen()
    screen.onkey(go_up, "Up")
    screen.onkey(go_down, "Down")
    screen.onkey(go_left, "Left")
    screen.onkey(go_right, "Right")
    # Also WASD
    screen.onkey(go_up, "w")
    screen.onkey(go_down, "s")
    screen.onkey(go_left, "a")
    screen.onkey(go_right, "d")

    # Game helpers
    def reset_game():
        nonlocal score, segments, high_score
        time.sleep(0.5)
        head.goto(0, 0)
        head.direction = "stop"
        # hide segments
        for seg in segments:
            seg.hideturtle()
        segments = []
        score = 0
        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 16, "normal"))

    # Main loop
    running = True
    while running:
        screen.update()

        # Check collision with border
        if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
            high_score = max(high_score, score)
            reset_game()

        # Check collision with food
        if head.distance(food) < 20:
            # Move food to random position on grid
            x = random.randint(-14, 14) * STEP
            y = random.randint(-14, 14) * STEP
            food.goto(x, y)

            # Add a segment
            new_seg = turtle.Turtle()
            new_seg.speed(0)
            new_seg.shape("square")
            new_seg.color("lightgreen")
            new_seg.penup()
            segments.append(new_seg)

            # Increase score
            score += 10
            if score > high_score:
                high_score = score
            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 16, "normal"))

        # Move the end segments first in reverse order
        for i in range(len(segments) - 1, 0, -1):
            x = segments[i - 1].xcor()
            y = segments[i - 1].ycor()
            segments[i].goto(x, y)

        # Move segment 0 to where the head is
        if len(segments) > 0:
            segments[0].goto(head.xcor(), head.ycor())

        move()

        # Check collision with body
        for seg in segments:
            if seg.distance(head) < 20:
                high_score = max(high_score, score)
                reset_game()
                break

        time.sleep(0.1)

    screen.mainloop()


if __name__ == "__main__":
    main()
