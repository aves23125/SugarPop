#############################################################
# Module Name: Sugar Pop Static Item Module
# Project: Sugar Pop Program
# Date: Nov 17, 2024
# By: Brett W. Huffman
# Description: The static item implementation of the sugar pop game
#############################################################
import pygame as pg
import pymunk
from settings import SCALE, HEIGHT

class StaticItem:
    def __init__(self, space, x1, y1, x2, y2, color='gray', line_width=3, friction=0.3, elasticity=0.5):
        """
        Initialize a static line segment in Pymunk between two points (x1, y1) and (x2, y2).
        
        :param space: The Pymunk space to add the line segment to.
        :param x1, y1: Starting point of the line in Pygame coordinates.
        :param x2, y2: Ending point of the line in Pygame coordinates.
        :param color: Color of the line for rendering in Pygame.
        :param line_width: Width of the line for rendering in Pygame.
        :param friction: Friction coefficient of the line segment.
        :param elasticity: Elasticity (bounciness) of the line segment.
        """
        self.color = color
        self.line_width = line_width
        self.space = space

        # Convert Pygame coordinates to Pymunk coordinates
        # pymunk_x1, pymunk_y1 = x1 / SCALE, (HEIGHT - y1) / SCALE
        # pymunk_x2, pymunk_y2 = x2 / SCALE, (HEIGHT - y2) / SCALE
        pymunk_x1, pymunk_y1 = x1 / SCALE, y1 / SCALE
        pymunk_x2, pymunk_y2 = x2 / SCALE, y2 / SCALE

        # Create a static body for the space
        self.body = space.static_body

        # Create a segment shape between the two points
        self.segment = pymunk.Segment(self.body, (pymunk_x1, pymunk_y1), (pymunk_x2, pymunk_y2), 0.1)  # Thickness of 0.1
        self.segment.friction = friction
        self.segment.elasticity = elasticity

        # Add the segment to the Pymunk space
        self.space.add(self.segment)

    def draw(self, screen):
        """
        Draw the static line segment on the Pygame screen.
        
        :param screen: The Pygame screen to draw the line on.
        """
        # Convert Pymunk coordinates to Pygame screen coordinates for rendering
        start_x = self.segment.a[0] * SCALE
        start_y = HEIGHT - self.segment.a[1] * SCALE
        end_x = self.segment.b[0] * SCALE
        end_y = HEIGHT - self.segment.b[1] * SCALE
        start = (start_x, start_y)
        end = (end_x, end_y)

        # Draw the line
        pg.draw.line(screen, pg.Color(self.color), start, end, self.line_width)

    def delete(self):
        """
        Delete the static item by removing its segment from the Pymunk space.
        """
        if self.segment:
            self.space.remove(self.segment)  # Remove the segment from the Pymunk space
            self.segment = None  # Clear the reference to the segment
