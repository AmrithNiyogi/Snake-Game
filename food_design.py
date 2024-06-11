# Import Shape class from the turtle module
from turtle import Shape


# Define the FoodDesign class
class FoodDesign:
    def __init__(self, screen):
        # Store the screen object
        self.screen = screen
        # Call method to register the custom apple shape
        self.register_apple_shape()

    # Method to define and register the custom apple shape
    def register_apple_shape(self):
        # Create a compound shape for the apple
        apple_shape = Shape("compound")

        # Define the apple components
        # Define the coordinates for the apple body
        apple_body = [(-20, 0), (-10, -10), (0, -20), (10, -10), (20, 0), (10, 10), (0, 20), (-10, 10)]
        # Define the coordinates for the apple stem
        apple_stem = [(0, 20), (0, 30), (2, 30), (2, 20)]
        # Define the coordinates for the apple leaf
        apple_leaf = [(0, 30), (5, 40), (10, 30)]

        # Add components to the compound shape
        # Add the apple body component to the shape with red fill and outline
        apple_shape.addcomponent(apple_body, "red", "red")
        # Add the apple stem component to the shape with brown fill and outline
        apple_shape.addcomponent(apple_stem, "brown", "brown")
        # Add the apple leaf component to the shape with green fill and outline
        apple_shape.addcomponent(apple_leaf, "green", "green")

        # Register the custom apple shape with the screen
        self.screen.register_shape("apple", apple_shape)
