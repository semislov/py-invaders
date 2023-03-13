import pygame, sys

def events():
    """event processing"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()