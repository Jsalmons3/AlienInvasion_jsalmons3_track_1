"""
Alien Invasion - Track 1
Author: Jeffrey Salmons
Purpose: manages all the powerups in the game
Starter Code: Professors Walters(RedBeard41) Alien_Invasion_starter
Date: 7/26/2026
"""

import pygame
from powerup import PowerUp
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class PowerUpDrops:
    """Manages all the active powerup drops"""

    def __init__(self, game: 'AlienInvasion'):
        """Initialize the powerup drops"""

        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.powerups = pygame.sprite.Group()

    def check_drop(self, collisions):
        """Check if a powerup should drop"""

        for alien in collisions:
            powerup = PowerUp(
                self.game,
                alien.rect.centerx,
                alien.rect.centery
            )

            self.powerups.add(powerup)

    def draw(self):
        """Draw all powerups"""

        self.powerups.draw(self.screen)