# creating multiple intances:

# we might want to set different initial values for the different objects of our class:

# we will pass data to the contructor to give each object its own initial values:

class gamer:
    games_played = 0
    name = ''
    age = 0

    def __init__(self, nam='bob', ag=18):
        self.name = nam
        self.age = ag 
        print('%s constructed, player is %d years old' % (self.name, self.age))

    def play(self, y=1):
        self.games_played += y
        print('%s has played %d games' % (self.name, self.games_played))



# j = gamer('john', 43)

# k = gamer('kelly', 24)

# l = gamer()

# l.play(8)

# k.play(4)

# j.play(5)  

# this is very cool stuff