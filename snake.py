# Import necessary modules from turtle
import turtle
from turtle import Turtle

# Constants for snake's starting positions, movement distance, and directions
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# Define the Snake class
class Snake:
    def __init__(self, screen):
        self.segments = []  # List to store snake segments
        self.screen = screen  # Reference to the screen object
        self.create_snake_shape()  # Create custom shapes for the snake
        self.create_snake()  # Create the initial snake
        self.head = self.segments[0]  # Set the head of the snake

    # Method to create custom shapes for the snake's head and body
    def create_snake_shape(self):
        # Define the compound shape for the snake's head
        snake_head_shape = turtle.Shape("compound")

        # Define the coordinates for the head body
        head_body = [
            (-10, 0), (-10, -5), (-5, -10), (5, -10),
            (10, -5), (10, 0), (10, 5), (5, 10),
            (-5, 10), (-10, 5), (-10, 0)
        ]
        # Add the head body component to the shape
        snake_head_shape.addcomponent(head_body, "white", "black")

        # Define the coordinates for the eyes
        left_eye = [(-5, 5), (-5, 7), (-3, 7), (-3, 5)]
        right_eye = [(5, 5), (5, 7), (3, 7), (3, 5)]

        # Add the eyes components to the shape
        snake_head_shape.addcomponent(left_eye, "black", "black")
        snake_head_shape.addcomponent(right_eye, "black", "black")

        # Register the head shape with the screen
        self.screen.register_shape("snake_head", snake_head_shape)

        # Define the compound shape for the snake's body
        snake_body_shape = turtle.Shape("compound")

        # Define the coordinates for the body (similar to head without eyes)
        body = [
            (-10, 0), (-10, -5), (-5, -10), (5, -10),
            (10, -5), (10, 0), (10, 5), (5, 10),
            (-5, 10), (-10, 5), (-10, 0)
        ]
        # Add the body component to the shape
        snake_body_shape.addcomponent(body, "white", "black")

        # Register the body shape with the screen
        self.screen.register_shape("snake_body", snake_body_shape)

    # Method to create the initial snake
    def create_snake(self):
        for index, position in enumerate(STARTING_POSITIONS):
            is_head = (index == 0)  # Determine if the segment is the head
            self.add_segment(position, is_head=is_head)  # Add the segment

    # Method to move the snake forward
    def move(self):
        # Move each segment to the position of the segment in front of it
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)
        # Move the head forward
        self.segments[0].forward(MOVE_DISTANCE)

    # Methods to change the snake's direction
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    # Method to add a new segment to the snake
    def add_segment(self, position, is_head=False):
        # Create a new turtle for the segment
        new_segment = Turtle("square")
        # Set the shape based on whether it is the head or a body segment
        new_segment.shape("snake_head" if is_head else "snake_body")
        # Set the color of the segment
        new_segment.color("green")
        # Lift the pen to avoid drawing when moving
        new_segment.penup()
        # Move the segment to the specified position
        new_segment.goto(position)
        # Add the segment to the segments list
        self.segments.append(new_segment)

    # Method to extend the snake by adding a new segment at the end
    def extend(self):
        # Add a new segment at the position of the last segment
        self.add_segment(self.segments[-1].position())

    def reset(self):
        # Move each segment of the snake to an off-screen position
        for seg in self.segments:
            seg.goto(1000, 1000)
        # Clear the list of segments
        self.segments.clear()
        # Recreate the snake from scratch
        self.create_snake()
        # Set the head of the snake to the first segment
        self.head = self.segments[0]
