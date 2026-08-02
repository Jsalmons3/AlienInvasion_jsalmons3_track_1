"""
Alien Invasion - Track 1
Author: Jeffrey Salmons
Purpose: Saves the game stats of the game
Starter Code: Professors Walters(RedBeard41) Alien_Invasion_starter
Date: 7/26/2026
"""
from pathlib import Path
import json

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class GameStats():
    """Track score, lives, level, and high score for Alien Invasion"""

    def __init__(self, game: 'AlienInvasion'):
        """Initialize the game statistics and load saved scores"""
        self.game = game
        self.setting = game.settings
        self.max_score = 0
        self.init_saved_scores()
        self.reset_stats()

    def init_saved_scores(self):
        """Load the saved high score"""
        self.path = self.setting.scores_file
        if self.path.exists() and self.path.stat.__sizeof__() > 20:
            contents = self.path.read_text()
            scores = json.loads(contents)
            self.hi_score = scores.get('hi_score', 0)

        else:
            self.hi_score = 0
            self.save_scores()
            # save the file

    def save_scores(self):
        """Save the high score to a file"""
        scores = {
            'hi_score': self.hi_score
        }
        contents = json.dumps(scores, indent=4)
        try:
            self.path.write_text(contents)
        except FileNotFoundError as e:
            print(f'File Not Found: {e}')

    def reset_stats(self):
        """Reset the game statistics for a new game"""
        self.ships_left = self.setting.starting_ship_count
        self.score = 0
        self.level = 1

    def update (self, collisions):
        """Update the player's score, max score, and high score"""
        
        self._update_score(collisions)

        self._update_max_score()

        self._update_hi_score()

    def _update_max_score(self):
        """Update the max score if the current score exceeds it"""
        if self.score > self.max_score:
            self.max_score = self.score
        # print(f'MAX: {self.max_score}')

    def _update_hi_score(self):
            """Update the high score if a new high score is achieved"""
            if self.score > self.hi_score:
                self.hi_score = self.score
            # print(f'Hi: {self.hi_score}')

    def _update_score(self, collisions):
            """Increase the score based on the number of aliens destroyed"""
            for alien in collisions.values():
                self.score += self.setting.alien_points
            # print(f'Basic: {self.score}')

    def update_level(self):
        """Increase the level by 1"""
        self.level += 1
        print(self.level)

        