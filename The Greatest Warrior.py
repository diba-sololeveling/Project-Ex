"""
This code defines a Warrior class that simulates a game-like character progression system.
A warrior starts with 100 experience points, which determine their level (experience // 100) 
and rank (based on experience // 1000). The warrior can gain experience through training 
(if they meet a minimum level requirement) or by engaging in battles against enemies of 
various levels. Battles yield different outcomes—Easy fight, A good fight, An intense fight, 
or Defeat—and award experience accordingly. Additionally, the warrior can collect 
achievements from successful training, and experience is capped at 10,000 (level 100, 
rank "Greatest").
"""

class Warrior (object):

    # List of possible ranks (based on experience / 1000)
    ranks = [
        "Pushover",
        "Novice",
        "Fighter",
        "Warrior",
        "Veteran",
        "Sage",
        "Elite",
        "Conqueror",
        "Champion",
        "Master",
        "Greatest"]

    def __init__(self):
        # Starting experience points
        self.experience = 100
        # List of achievements from training
        self.achievements = []

    @property
    def level(self):
        # Level = experience divided by 100 (max 100)
        return self.experience // 100

    @property
    def rank(self):
        # Rank = based on 1000 XP steps (index in ranks list)
        return Warrior.ranks[self.experience // 1000]

    def update_exp(self, exp):
        # Add experience but cap it at 10000
        self.experience += exp
        self.experience = min(10000, self.experience)

    def training(self, lst):
        # Training data: [description, exp gained, minimum level required]
        description, exp, min_lev = lst
        if self.level < min_lev:
            # Too weak to complete this training
            return "Not strong enough"

        # Otherwise: gain experience and record the achievement
        self.update_exp(exp)
        self.achievements.append(description)
        return description

    def battle(self, emy_lev):
        # Enemy level must be between 1 and 100
        if emy_lev < 1 or emy_lev > 100:
            return "Invalid level"

        # Level difference between warrior and enemy
        diff = self.level - emy_lev

        # If enemy is at least 5 levels higher and in a higher rank tier → defeat
        if diff <= -5 and (self.level // 10 - emy_lev // 10 <= -1):
            return "You've been defeated"

        # If warrior is much stronger (≥2 levels higher) → easy fight (no XP)
        if diff >= 2:
            return "Easy fight"

        # Same level → gain 10 XP
        if diff == 0:
            self.update_exp(10)
            return "A good fight"

        # Enemy is 1 level lower → gain 5 XP
        if diff == 1:
            self.update_exp(5)
            return "A good fight"

        # Enemy is stronger but not too much → intense fight, XP based on squared diff
        self.update_exp(20 * diff * diff)
        return "An intense fight"


# -------------------- Code Driver --------------------

bruce_lee = Warrior()

# Initial stats
print(bruce_lee.level)         # => 1 (100 XP // 100)
print(bruce_lee.experience)    # => 100
print(bruce_lee.rank)          # => "Pushover"
print(bruce_lee.achievements)  # => []

# Training example
print(bruce_lee.training(["Defeated Chuck Norris", 9000, 1]))
# Warrior gains 9000 XP and an achievement

print(bruce_lee.experience)    # => 9100
print(bruce_lee.level)         # => 91
print(bruce_lee.rank)          # => "Master"

# Battle example
print(bruce_lee.battle(90))    # => "A good fight"
print(bruce_lee.experience)    # => 9105
print(bruce_lee.achievements)  # => ["Defeated Chuck Norris"]
