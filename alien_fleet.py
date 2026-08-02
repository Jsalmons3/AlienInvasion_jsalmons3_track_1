"""
Alien Invasion - Track 1
Author: Jeffrey Salmons
Purpose: Makes the alien fleet size and movement
Starter Code: Professors Walters(RedBeard41) Alien_Invasion_starter
Date: 7/26/2026
"""
import pygame
from alien import Alien
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    

class AlienFleet:
    """Manages the alien fleet movement, creation, and collisions"""

    def __init__(self, game: 'AlienInvasion'):
        """Initialize the alien fleet and create the starting formation"""

        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed

        self.create_fleet()

    def create_fleet(self):
        """Create the intiial alien fleet formation"""

        alien_w = self.settings.alien_w
        alien_h = self.settings.alien_h
        screen_w = self.settings.screen_w
        screen_h = self.settings.screen_h

        fleet_w, fleet_h = self.calculate_fleet_size(alien_w, screen_w, alien_h, screen_h)
        x_offset, y_offset = self.calculate_offsets(alien_w, alien_h, screen_w, fleet_w, fleet_h)

        self._create_rectangle_fleet(alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset)

        for col in range(fleet_w):
            current_x = alien_w * col + x_offset
            if col % 2 == 0:
                continue
            self._create_alien(current_x, 10)

    def _create_rectangle_fleet(self, alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset):
        """Create the main rectangular formation of the aliens"""

        for row in range(fleet_h):
            for col in range(fleet_w):
                current_x = alien_w * col + x_offset
                current_y = alien_h * row + y_offset
                if col % 2 == 0 or row % 2 == 0:
                    continue
                self._create_alien(current_x, current_y)

    def calculate_offsets(self, alien_w, alien_h, screen_w, fleet_w, fleet_h):
        """Calculate the starting x and y offsets for centering the fleet"""

        half_screen = self.settings.screen_h//2
        fleet_horizontal_space = fleet_w * alien_w
        fleet_vertical_space = fleet_h * alien_h
        x_offset = int((screen_w-fleet_horizontal_space)//2)
        y_offset = int((half_screen-fleet_vertical_space)//2)
        return x_offset,y_offset


    def calculate_fleet_size(self, alien_w, screen_w, alien_h, screen_h):
        """Calculate how many aliens fit on the screen"""

        fleet_w = (screen_w//alien_w)
        fleet_h = ((screen_h /2)//alien_h)

        if fleet_w % 2 == 0:
            fleet_w -= 1
        else:
            fleet_w -= 2

        if fleet_h % 2 == 0:
            fleet_h -= 1
        else:
            fleet_h -= 2

        return int(fleet_w), int(fleet_h)
    
    def _create_alien(self, current_x: int, current_y: int):
        """Creates a single alien and adds it to the fleet"""

        new_alien = Alien(self, current_x, current_y)

        self.fleet.add(new_alien)

    def _check_fleet_edges(self):
        """Check whether the fleet has reached either edge of the screen"""

        alien: Alien
        for alien in self.fleet:
            if alien.check_edges():
                self._drop_alien_fleet()
                self.fleet_direction *= -1
                break

    def _drop_alien_fleet(self):
        """Move the fleet downward and reverse its direction"""
        for alien in self.fleet:
            alien.y += self.fleet_drop_speed

    def update_fleet(self):
        """Update the position of the fleet"""
        self._check_fleet_edges()
        self.fleet.update()

    def draw(self):
        """Draw every alien in the fleet"""
        alien: 'Alien'
        for alien in self.fleet:
            alien.draw_alien()

    def check_collisions(self, other_group, remove_bullets: bool = True):
        """Check for collisions between aliens and another sprite group"""

        return pygame.sprite.groupcollide(self.fleet, other_group, True, remove_bullets)

    def explode_at(self, center):
        """Destroy aliens near an explosion"""

        explosion_radius = 150
        explosion_x, explosion_y = center
        for alien in self.fleet.copy():
            alien_x, alien_y = alien.rect.center
            x_distance = alien_x - explosion_x
            y_distance = alien_y - explosion_y

            if (x_distance ** 2 + y_distance ** 2) <= explosion_radius ** 2:
                self.fleet.remove(alien)

    
    def check_fleet_bottom(self):
        """Check whether any aliens have reached the bottom of the screen"""
        alien: Alien
        for alien in self.fleet:
            if alien.rect.bottom >= self.settings.screen_h:
                return True
        return False
    
    def check_destroyed_status(self):
        """Check if the fleet has been destroyed"""
        return not self.fleet