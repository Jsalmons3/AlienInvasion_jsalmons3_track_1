"""
Alien Invasion - Track 1
Author: Jeffrey Salmons
Purpose: Removes the bullet from the screen and keeps the orignal amount of bullets
Starter Code: Professors Walters(RedBeard41) Alien_Invasion_starter
Date: 7/26/2026
"""
import pygame
from bullet import Bullet
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    

class Arsenal:
    def __init__(self, game: 'AlienInvasion'):
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()
        self.triple_shot = False
        self.piercing_shot = False
        self.explosion_shot = False

    def update_arsenal(self) -> None:
        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self) -> None:
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)

    def draw(self) -> None:
        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullet(self) -> bool:
        """Fire one or three lasers"""
        if len(self.arsenal) < self.settings.bullet_amount:

            if self.triple_shot:
                self._fire_triple_shot()
            else:
                new_bullet = Bullet(self.game)
                self.arsenal.add(new_bullet)
            return True
        return False

    def _fire_triple_shot(self):
        left_bullet = Bullet(self.game, -20)
        middle_bullet = Bullet(self.game)
        right_bullet = Bullet(self.game, 20)

        self.arsenal.add(left_bullet)
        self.arsenal.add(middle_bullet)
        self.arsenal.add(right_bullet)