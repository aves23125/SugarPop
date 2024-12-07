#############################################################
# Module Name: Sugar Pop level Module
# Project: Sugar Pop Program
# Date: Nov 17, 2024
# By: Brett W. Huffman
# Description: The level implementation of the sugar pop game
#############################################################

import json
import os

class Level:
    def __init__(self, level_file=None):
        """
        Initialize a Level object.
        
        :param level_file: Path to the JSON file for the level. If None, an empty level is created.
        """
        self.level_file = level_file
        self.data = {
            "number_sugar_grains": 0,
            "static_boxes": [],
            "buckets": [],
            "time_to_complete_level": 0,
        }
        
        if level_file and os.path.exists(level_file):
            self.load_level(level_file)
        else:
            print(f"Level file not found: {level_file}")
            self.data = {}

    def load_level(self, level_file):
        """
        Load a level from a JSON file.
        """
        try:
            with open(level_file, 'r') as f:
                self.data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading level: {e}")
            self.data = {}

    def save_level(self, level_file=None):
        """
        Save the current level to a JSON file.
        
        :param level_file: Path to save the level. If None, uses the current level_file.
        """
        if level_file:
            self.level_file = level_file

        if not self.level_file:
            raise ValueError("No file specified to save the level.")

        try:
            with open(self.level_file, 'w') as f:
                json.dump(self.data, f, indent=4)
        except Exception as e:
            print(f"Error saving level: {e}")

    def add_static_box(self, x, y, width, height):
        """
        Add a static box to the level.
        """
        self.data["static_boxes"].append({
            "x": x,
            "y": y,
            "width": width,
            "height": height
        })

    def add_bucket(self, x, y, width, height, number_sugar_grains):
        """
        Add a bucket to the level.
        """
        self.data["buckets"].append({
            "x": x,
            "y": y,
            "width": width,
            "height": height,
            "needed_sugar": needed_sugar
        })

    def set_number_sugar_grains(self, count):
        """
        Set the total number of sugar grains for the level.
        """
        self.data["number_sugar_grains"] = count

    def set_time_to_complete(self, time_in_seconds):
        """
        Set the time to complete the level.
        """
        self.data["time_to_complete_level"] = time_in_seconds
