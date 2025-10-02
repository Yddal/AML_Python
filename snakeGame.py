import turtle # This module provides a way to draw graphics
import time   # This module provides time-related functions, like pausing
import random # This module generates random numbers, useful for food placement


# OBS! LAGET MED AI



# --- 1. Screen Setup ---
# Create the game window. Think of this as your canvas.
screen = turtle.Screen()
screen.setup(width=600, height=600)  # Set the size of the game window to 600x600 pixels
screen.bgcolor("black")              # Set the background color of the window to black
screen.title("Simple Snake Game")    # Set the title that appears on the window bar
screen.tracer(0)                     # Turn off screen updates. We'll update manually for smoother animation.

# --- 2. Snake Head ---
# Create the snake's head, which is a turtle object.
head = turtle.Turtle()
head.speed(0)       # Set the animation speed to the fastest (0 means no animation delay for creation)
head.shape("square") # The head will be a square shape
head.color("green") # The head will be green
head.penup()        # "Pen up" means it won't draw a line when it moves
head.goto(0, 0)     # Start the snake head at the center of the screen (x=0, y=0)
head.direction = "stop" # Initialize the snake's direction to "stop"

# --- 3. Snake Food ---
# Create the food object, also a turtle.
food = turtle.Turtle()
food.speed(0)       # Fastest animation speed
food.shape("circle") # Food will be a circle shape
food.color("red")   # Food will be red
food.penup()        # Don't draw lines
food.goto(0, 100)   # Place the initial food slightly above the center

# --- 4. Scoreboard ---
# Create a turtle to display the score.
score_pen = turtle.Turtle()
score_pen.speed(0)           # Fastest animation speed
score_pen.shape("square")    # Needs a shape, but we'll hide it
score_pen.color("white")     # Text color will be white
score_pen.penup()            # Don't draw lines
score_pen.hideturtle()       # Make the turtle icon itself invisible
score_pen.goto(0, 260)       # Position the score text near the top of the screen
score_pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# --- Game Variables ---
segments = [] # A list to store all the body segments of the snake
score = 0     # Current game score
high_score = 0 # Highest score achieved
delay = 0.1   # Initial game speed (smaller delay means faster game)

# --- 5. Movement Functions ---
# These functions change the direction of the snake's head based on key presses.
def go_up():
    # Only allow changing direction if not currently moving down (prevents 180-degree turns)
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

# This function updates the snake head's position based on its current direction.
def move():
    if head.direction == "up":
        y = head.ycor()      # Get the current Y-coordinate
        head.sety(y + 20)    # Move up by 20 pixels (one "square" unit)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)    # Move down by 20 pixels

    if head.direction == "left":
        x = head.xcor()      # Get the current X-coordinate
        head.setx(x - 20)    # Move left by 20 pixels

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)    # Move right by 20 pixels

# --- Game Over / Reset Function ---
# This function handles what happens when the game ends and resets it.
def game_over_reset():
    global score        # Declare that we are modifying the global 'score' variable
    global delay        # Declare that we are modifying the global 'delay' variable
    global high_score   # Declare that we are modifying the global 'high_score' variable

    time.sleep(1)       # Pause the game for 1 second to show the collision
    head.goto(0, 0)     # Move the snake head back to the center
    head.direction = "stop" # Stop the snake's movement

    # Hide all the snake body segments by moving them off-screen
    for segment in segments:
        segment.goto(1000, 1000) # Move to an invisible location far away
    segments.clear() # Clear the list of segments, effectively removing the snake's body

    # Update high score if current score is greater
    if score > high_score:
        high_score = score
    score = 0           # Reset current score to 0
    delay = 0.1         # Reset game speed to initial value

    score_pen.clear()   # Clear the old score text from the screen
    # Write the updated score and high score
    score_pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

# --- 6. Keyboard Bindings ---
screen.listen() # Tell the screen to start listening for keyboard events
# Bind arrow keys to our movement functions
screen.onkeypress(go_up, "Up")      # When 'Up' arrow key is pressed, call go_up()
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

# --- 7. Main Game Loop ---
# This loop runs continuously and is the heart of the game.
while True:
    screen.update() # Manually update the screen to show all changes made since the last update

    # Check for collision with the screen borders
    # The screen is 600x600, so from -300 to 300. We use 290 to give a small buffer.
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        game_over_reset() # If collision, reset the game

    # Check for collision with food
    # head.distance(food) calculates the distance between the head and the food.
    # If it's less than 20 pixels (the size of a square/circle), they've collided.
    if head.distance(food) < 20:
        # Move the food to a new random location, ensuring it aligns with the grid
        # We need coordinates that are multiples of 20.
        # The screen ranges from -290 to 290 (approx) for snake movement.
        # So, we can generate a random grid position from -14 to 14 (since 14 * 20 = 280).
        x = random.randint(-14, 14) * 20
        y = random.randint(-14, 14) * 20
        food.goto(x, y)

        # Add a new segment to the snake's body
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey") # Body segments are grey
        new_segment.penup()
        segments.append(new_segment) # Add the new segment to our list

        # Increase the score
        score += 10 # Each food eaten adds 10 points
        if score > high_score:
            high_score = score # Update high score if current score is better

        # Decrease the delay to make the game faster (increase difficulty)
        delay -= 0.001

        score_pen.clear() # Clear the old score display
        # Write the updated score and high score
        score_pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    # Move the snake body segments
    # This loop starts from the last segment and moves each segment to the position of the one in front of it.
    # This creates the "following" effect.
    for index in range(len(segments) - 1, 0, -1): # Iterate backwards
        x = segments[index-1].xcor() # Get X-coordinate of the segment in front
        y = segments[index-1].ycor() # Get Y-coordinate of the segment in front
        segments[index].goto(x, y)   # Move current segment to that position

    # Move segment 0 (the first body segment) to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move() # Call the move function to update the snake head's position

    # Check for head collision with its own body segments
    for segment in segments:
        if segment.distance(head) < 20: # If head is too close to any body segment
            game_over_reset() # Trigger game over

    time.sleep(delay) # Pause the game for a short duration, controlled by 'delay'

screen.mainloop() # Keep the window open until manually closed