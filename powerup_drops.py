"""
Alien Invasion - Track 1
Author: Jeffrey Salmons
Purpose: manages all the powerups in the game
Starter Code: Professors Walters(RedBeard41) Alien_Invasion_starter
Date: 7/26/2026
"""

import pygame
import random
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

            power_type = random.choice(
                ["explosion", "triple", "piercing"]
            )

            powerup = PowerUp(
                self.game,
                alien.rect.centerx,
                alien.rect.centery,
                power_type
            )

            self.powerups.add(powerup)

    def draw(self):
        """Draw all powerups"""

        self.powerups.draw(self.screen)

    def update(self):
        """Updates all active powerups"""

        self.powerups.update()
        self._remove_powerups_offscreen()

    def _remove_powerups_offscreen(self):
        """Remove powerups that have fallen off the screen"""

        for powerup in self.powerups.copy():
            if powerup.rect.top >= self.screen.get_height():
                self.powerups.remove(powerup)

    def check_collisions(self):
        """Check if the ship collects a powerup"""

        powerup = pygame.sprite.spritecollideany(
            self.game.ship,
            self.powerups
        )

        if powerup:
            print(f"{powerup.power_type.capitalize()} Powerup Collected")
            self.powerups.remove(powerup)