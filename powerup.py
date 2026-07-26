"""
Alien Invasion - Track 1
Author: Jeffrey Salmons
Purpose: Create powerups that will fall from the aliens
Starter Code: Professors Walters(RedBeard41) Alien_Invasion_starter
Date: 7/26/2026
"""
import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class PowerUp(Sprite):
    """Represents a powerup that can be obtained"""

    def __init__(self, game: 'AlienInvasion', x: int, y: int):
        """Initialize the powerup"""
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 0, 0), (15,15), 15)

        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
