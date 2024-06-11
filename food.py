# Import Turtle class from the turtle module and random module as r
from turtle import Turtle
import random as r
# Import FoodDesign class from food_design module
from food_design import FoodDesign


# Define the Food class, inheriting from Turtle
class Food(Turtle):
    def __init__(self, screen):
        # Initialize the parent Turtle class
        super().__init__()
        # Apply custom design to the screen using FoodDesign
        FoodDesign(screen)
        # Set the shape of the food to "apple"
        self.shape("apple")
        # Lift the pen to avoid drawing when moving
        self.penup()
        # Resize the shape to be smaller
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        # Set the color of the food to red
        self.color("red")
        # Set the movement speed to the fastest
        self.speed("fastest")
        # Call the refresh method to place the food at a random position
        self.refresh()

    # Method to place the food at a random position
    def refresh(self):
        # Generate random x and y coordinates within the screen bounds
        random_x = r.randint(-280, 280)
        random_y = r.randint(-280, 280)
        # Move the food to the new random coordinates
        self.goto(random_x, random_y)
