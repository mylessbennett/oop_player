class Player:
    """ does player """

    def __init__(self, gold_coins, health_points, lives):
        self.gold_coins = 0
        self.health_points = 10
        self.lives = 5

    def __str__(self):
        return "Gold Coins: {}\nHealth Points: {}\nLives: {}".format(self.gold_coins, self.health_points, self.lives)

    def level_up(self):
        self.lives += 1

    def collect_treasure(self):
        self.gold_coins += 1
        if self.gold_coins % 10 == 0:
            self.level_up()

    def do_battle(self, damage):
        self.health_points = self.health_points - damage
        if self.health_points < 1:
            self.lives -= 1
            self.health_points = 10
            if self.lives < 1:
                self.reset()

    def reset(self):
        self.gold_coins = 0
        self.health_points = 10
        self.lives = 5

player1 = Player(0, 10, 5)

#-------------------------------------------------------------------------------------------------------------
# Test level up
player1.level_up()

print(player1)
#-------------------------------------------------------------------------------------------------------------
# Test collect treasure
player1.collect_treasure()
player1.collect_treasure()
player1.collect_treasure()
player1.collect_treasure()
player1.collect_treasure()
player1.collect_treasure()
player1.collect_treasure()
player1.collect_treasure()
player1.collect_treasure()
player1.collect_treasure()

print(player1)
#-------------------------------------------------------------------------------------------------------------
# Test do battle
player1.do_battle(10)

print(player1)
#-------------------------------------------------------------------------------------------------------------
# To test player reset
player1.do_battle(10)
player1.do_battle(10)
player1.do_battle(10)
player1.do_battle(10)

print(player1)
