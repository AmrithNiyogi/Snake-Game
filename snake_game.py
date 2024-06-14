"""
# TODO 1: Create a snake body
# TODO 2: Move the snake
# TODO 3: Control the snake
# TODO 4: Detect collision with food
# TODO 5: Create a scoreboard
# TODO 6: Detect collision with wall
# TODO 7: Detect collision with tail
"""
# Import necessary modules
import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


# Function to set up the screen and key bindings
def screen_setup(srcn, snk):
    # Set up the screen dimensions
    srcn.setup(width=600, height=600)
    # Set the background color to black
    srcn.bgcolor("black")
    # Turn off screen updates to manually control when updates occur
    srcn.tracer(0)
    # Set the title of the window
    srcn.title("Snake Game")
    # Allow the screen to listen for key presses
    srcn.listen()
    # Bind the arrow keys to control the snake's movement
    srcn.onkey(snk.up, "Up")
    srcn.onkey(snk.down, "Down")
    srcn.onkey(snk.left, "Left")
    srcn.onkey(snk.right, "Right")


# Main game code
if __name__ == '__main__':
    # Create a screen object
    screen = Screen()
    # Create a snake object
    snake = Snake(screen)
    # Create a food object
    food = Food(screen)
    # Create a scoreboard object
    scoreboard = Scoreboard()
    # Set up the screen with the screen and snake objects
    screen_setup(screen, snake)

    # Set the game loop flag to True
    game_is_on = True
    while game_is_on:
        # Update the screen with the latest changes
        screen.update()
        # Pause the game for a short duration to control the speed
        time.sleep(0.1)

        # Move the snake
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            # Refresh the food position if the snake eats it
            food.refresh()
            # Extend the snake's body
            snake.extend()
            # Increase the score
            scoreboard.increase_score()

        # Detect collision with wall
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            scoreboard.reset()
            snake.reset()

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.reset()
                snake.reset()

    # Close the game window when clicked
    screen.exitonclick()
