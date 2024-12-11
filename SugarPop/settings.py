#############################################################
# Module Name: Sugar Pop Settings Module
# Project: Sugar Pop Program
# Date: Nov 17, 2024
# By: Brett W. Huffman
# Description: The settings implementation of the sugar pop game
#############################################################

import pygame as pg

# Window settings
RES = WIDTH, HEIGHT = 1024, 800
FPS = 60

# Scaling factor (Pixels per meter)
SCALE = 30  # Scale Factor: 30 pixels per meter
MAX_TIME_STEP = 1.0 / FPS  # Simulation step

# Define collision types
FLOOR_COLLISION_TYPE = 1
BOX_COLLISION_TYPE = 2


# Level Info
LEVEL_FILE_NAME = './levels/levelX.json'

# User Defined Events
START_FLOW = pg.USEREVENT + 1
FLOW_DELAY = pg.USEREVENT + 2
LOAD_NEW_LEVEL = pg.USEREVENT + 3
EXIT_APP = pg.USEREVENT + 4