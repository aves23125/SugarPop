#############################################################
# Module Name: Sugar Pop Message Display Module
# Project: Sugar Pop Program
# Date: Nov 17, 2024
# By: Brett W. Huffman
# Description: The Message Display implementation of the sugar pop game
#############################################################
import pygame as pg
import time

class MessageDisplay:
    def __init__(self, font_name=None, font_size=36, color=(255, 255, 255)):
        """
        Initialize the MessageDisplay class.
        
        :param screen: The Pygame screen to display messages on.
        :param font_name: The name of the font (default is None, which uses the default font).
        :param font_size: The size of the font.
        :param color: The color of the text (default is white).
        """
        self.font = pg.font.SysFont(font_name, font_size)
        self.color = color
        self.message = None
        self.display_until = 0

    def show_message(self, text, duration):
        """
        Show a message on the screen for a given duration.
        
        :param text: The text to display.
        :param duration: The number of seconds to display the text.
        """
        self.message = text
        self.display_until = time.time() + duration

    def update(self):
        """
        Update the message display. If the timer expires, clear the message.
        """
        if self.message and time.time() > self.display_until:
            self.message = None

    def draw(self, screen):
        """
        Draw the message on the screen, if there is an active message.
        """
        if self.message and screen:
            text_surface = self.font.render(self.message, True, self.color)
            text_rect = text_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
            screen.blit(text_surface, text_rect)
