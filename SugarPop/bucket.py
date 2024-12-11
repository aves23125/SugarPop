#############################################################
# Module Name: Sugar Pop Bucket Module
# Project: Sugar Pop Program
# Date: Nov 17, 2024
# By: Brett W. Huffman
# Description: The bucket implementation of the sugar pop game
#############################################################

import pygame as pg
import pymunk
from settings import SCALE, HEIGHT, WIDTH
from math import sqrt

class Bucket:
    def __init__(self, space, x, y, width, height, needed_sugar):
        """
        Initialize the bucket with an open top by creating three static segments 
        for each wall (left, right, bottom).
        
        :param space: The Pymunk space.
        :param x: X position of the bucket's center in Pygame coordinates.
        :param y: Y position of the bucket's top in Pygame coordinates.
        :param width: Width of the bucket in pixels.
        :param height: Height of the bucket in pixels.
        """
        self.space = space
        self.width = width / SCALE
        self.height = height / SCALE
        self.count = 0  # Counter for collected sugar grains
        self.needed_sugar = needed_sugar

        wall_thickness = 0.2  # Thickness of the walls in physics units

        # Convert Pygame coordinates to Pymunk coordinates
        x_pymunk = x / SCALE
        y_pymunk = y / SCALE # (HEIGHT - y) / SCALE  # Adjust y-coordinate for Pymunk's coordinate system

        # Left wall
        left_wall_start = (x_pymunk - self.width / 2, y_pymunk - self.height / 2)
        left_wall_end = (x_pymunk - self.width / 2, y_pymunk + self.height / 2)
        self.left_wall = pymunk.Segment(space.static_body, left_wall_start, left_wall_end, wall_thickness)
        self.left_wall.friction = 0.5
        self.left_wall.elasticity = 0.5
        space.add(self.left_wall)

        # Right wall
        right_wall_start = (x_pymunk + self.width / 2, y_pymunk - self.height / 2)
        right_wall_end = (x_pymunk + self.width / 2, y_pymunk + self.height / 2)
        self.right_wall = pymunk.Segment(space.static_body, right_wall_start, right_wall_end, wall_thickness)
        self.right_wall.friction = 0.5
        self.right_wall.elasticity = 0.5
        space.add(self.right_wall)

        # Bottom wall
        bottom_wall_start = (x_pymunk - self.width / 2, y_pymunk - self.height / 2)
        bottom_wall_end = (x_pymunk + self.width / 2, y_pymunk - self.height / 2)
        self.bottom_wall = pymunk.Segment(space.static_body, bottom_wall_start, bottom_wall_end, wall_thickness)
        self.bottom_wall.friction = 0.5
        self.bottom_wall.elasticity = 0.5
        space.add(self.bottom_wall)
        
        self.exploded = False  # Track if the bucket has exploded

    def explode(self, grains):
        """
        Apply a radial force to all grains near the bucket and remove the bucket walls.
        
        :param grains: List of sugar grain objects in the game.
        """
        if self.exploded:
            return  # Prevent multiple explosions

        # Get the bucket's center position
        bucket_center_x = (self.left_wall.a[0] + self.right_wall.a[0]) / 2
        bucket_center_y = (self.left_wall.a[1] + self.left_wall.b[1]) / 2

        # Apply radial force to each grain
        for grain in grains:
            grain_pos = grain.body.position

            # Calculate the vector from the bucket center to the grain
            dx = grain_pos.x - bucket_center_x
            dy = grain_pos.y - bucket_center_y
            distance = sqrt(dx**2 + dy**2)

            if distance < 2:  # Only affect grains within a certain radius
                # Normalize the vector
                if distance > 0:
                    dx /= distance
                    dy /= distance

                # Apply a radial impulse (adjust magnitude as needed)
                impulse_magnitude = 20 / (distance + 0.1)  # Reduce force with distance
                impulse = (dx * impulse_magnitude, dy * impulse_magnitude)
                grain.body.apply_impulse_at_world_point(impulse, grain.body.position)

        # Remove the bucket walls
        self.space.remove(self.left_wall, self.right_wall, self.bottom_wall)

        self.exploded = True  # Mark the bucket as exploded
        
    def draw(self, screen):
        """
        Draw the bucket with an open top on the Pygame screen.
        """
        if self.exploded:
            return  # Don't draw if the bucket has exploded

        color = (144, 238, 144)  # Light green color

        # Helper function to convert Pymunk coordinates to Pygame coordinates
        def to_pygame(p):
            return int(p[0] * SCALE), int(HEIGHT - p[1] * SCALE)

        # Draw the bucket edges
        pg.draw.line(screen, color, to_pygame(self.left_wall.a), to_pygame(self.left_wall.b), 2)
        pg.draw.line(screen, color, to_pygame(self.right_wall.a), to_pygame(self.right_wall.b), 2)
        pg.draw.line(screen, color, to_pygame(self.bottom_wall.a), to_pygame(self.bottom_wall.b), 2)

    def count_reset(self):
        if not self.exploded:
            self.count = 0
        
    def collect(self, sugar_grain):
        """
        Check if a sugar grain is within the bucket bounds and, if so, increase the bucket's count.
        
        :param sugar_grain: The sugar grain to check.
        """
        if self.exploded:
            return  # Don't count grains if the bucket has exploded

        grain_pos = sugar_grain.body.position

        # Get bucket boundaries
        left = self.left_wall.a[0]
        right = self.right_wall.a[0]
        bottom = self.bottom_wall.a[1]
        top = self.left_wall.b[1]

        # Check if the grain's position is within the bucket's bounding box
        if left <= grain_pos.x <= right and bottom <= grain_pos.y <= top:
            self.count += 1
            return True  # Indicate that the grain was collected

        return False  # Grain not collected

    def delete(self):
        if not self.exploded:
            # Remove the bucket walls
            self.space.remove(self.left_wall, self.right_wall, self.bottom_wall)
            self.exploded = True
