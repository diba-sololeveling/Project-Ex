
class Warrior (object):

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
        self.experience = 100
        self.achievements = []

    @property
    def level(self):
        return self.experience // 100

    @property
    def rank(self):
        return Warrior.ranks[self.experience // 1000]

    def update_exp(self, exp):
        self.experience += exp
        self.experience = min(10000, self.experience)

    def training(self, lst):
        description, exp, min_lev = lst
        if self.level < min_lev:
            return "Not strong enough"

        self.update_exp(exp)
        self.achievements.append(description)
        return description

    def battle(self, emy_lev):

        if emy_lev < 1 or emy_lev > 100:
            return "Invalid level"

        diff = self.level - emy_lev

        if diff <= -5 and (self.level // 10 - emy_lev // 10 <= -1):
            return "You've been defeated"
        if diff >= 2:
            return "Easy fight"
        if diff == 0:
            self.update_exp(10)
            return "A good fight"
        if diff == 1:
            self.update_exp(5)
            return "A good fight"

        self.update_exp(20 * diff * diff)
        return "An intense fight"


# Code Driver
bruce_lee = Warrior()
print(bruce_lee.level)         # => 1
print(bruce_lee.experience)    # => 100
print(bruce_lee.rank)          # => "Pushover"
print(bruce_lee.achievements)  # => []
# => "Defeated Chuck Norris"
print(bruce_lee.training(["Defeated Chuck Norris", 9000, 1]))
print(bruce_lee.experience)    # => 9100
print(bruce_lee.level)        # => 91
print(bruce_lee.rank)          # => "Master"
print(bruce_lee.battle(90))    # => "A good fight"
print(bruce_lee.experience)    # => 9105
print(bruce_lee.achievements)  # => ["Defeated Chuck Norris"]
