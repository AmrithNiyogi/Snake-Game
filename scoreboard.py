# Import Turtle class from the turtle module
from turtle import Turtle

# Constants for text alignment and font settings
ALIGNMENT = "center"
FONT_SIZE = 20
FONT_NAME = "Montserrat"
FONT_STYLE = "bold"

# Define the Scoreboard class, inheriting from Turtle
class Scoreboard(Turtle):
    def __init__(self):
        # Initialize the parent Turtle class
        super().__init__()
        # Initialize the score attribute to 0
        self.score = 0
        # Set the color of the turtle (pen) to white
        self.color("white")
        # Hide the turtle icon
        self.hideturtle()
        # Lift the pen to avoid drawing when moving
        self.penup()
        # Move the turtle to the top-center of the screen
        self.goto(0, 270)
        # Write the initial score on the screen
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=(FONT_NAME, FONT_SIZE, FONT_STYLE))

    # Method to update the scoreboard display
    def update_scoreboard(self):
        # Clear the previous score
        self.clear()
        # Write the updated score on the screen
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=(FONT_NAME, FONT_SIZE, FONT_STYLE))

    # Method to increase the score
    def increase_score(self):
        # Increment the score by 1
        self.score += 1
        # Update the scoreboard to reflect the new score
        self.update_scoreboard()

    # Method to display the "Game Over" message
    def game_over(self):
        # Move the turtle to the center of the screen
        self.goto(0, 0)
        # Write "GAME OVER" on the screen
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=(FONT_NAME, FONT_SIZE, FONT_STYLE))
