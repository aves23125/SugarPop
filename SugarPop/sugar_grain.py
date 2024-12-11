#############################################################
# Module Name: Sugar Pop Sugar 'Grain' Module
# Project: Sugar Pop Program
# Date: Nov 17, 2024
# By: Brett W. Huffman
# Description: The sugar grain implementation of the sugar pop game
#############################################################
import pygame as pg
import pymunk
from settings import SCALE, HEIGHT

class sugar_grain:
    def __init__(self, space, x, y, friction=0.3):
        """
        Initialize a sugar grain as a small dynamic body in Pymunk.
        
        :param space: The Pymunk space where the grain will be created.
        :param x: Initial x position in Pygame coordinates.
        :param y: Initial y position in Pygame coordinates.
        """
        self.space = space

        # Convert Pygame coordinates to Pymunk coordinates (Pymunk's Y-axis points upwards)
        pos_x = x / SCALE
        pos_y = y / SCALE #(HEIGHT - y) / SCALE  # Adjust Y-axis

        # Create a dynamic body with mass and moment of inertia
        mass = 1.0
        size = 2 / SCALE  # Size of the square in physics units
        moment = pymunk.moment_for_box(mass, (size, size))

        self.body = pymunk.Body(mass, moment)
        self.body.position = pos_x, pos_y

        # Define a small square shape attached to the body
        s = size / 2  # Half the size for vertex calculations
        vertices = [(-s, -s), (-s, s), (s, s), (s, -s)]
        self.shape = pymunk.Poly(self.body, vertices)
        self.shape.friction = friction
        self.shape.elasticity = 0.5  # Adjust as needed

        # Add the body and shape to the space
        self.space.add(self.body, self.shape)
        
    def update(self):
        """
        Update method for sugar_grain.
        In this case, Pymunk handles the physics, so nothing is needed here.
        """
        pass

    def draw(self, screen):
        """
        Draw the sugar grain on the Pygame screen.
        
        :param screen: The Pygame surface to draw the grain on.
        """
        # Get the position of the grain in Pygame coordinates
        pos = self.body.position
        screen_x = pos.x * SCALE
        screen_y = HEIGHT - pos.y * SCALE

        # Draw a small square at this position
        pg.draw.rect(screen, pg.Color('white'), (screen_x - 1, screen_y - 1, 2, 2))

    def delete(self):
        """
        Remove the sugar grain from the Pymunk space.
        """
        self.space.remove(self.body, self.shape)
