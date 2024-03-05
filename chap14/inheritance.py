# inheritance:

# original class is parent class and new class is the child class:

# import the class gamer from the file multi_instances:

from multi_instances import gamer

class call_of_duty(gamer):
    wins = 0

    def won_game(self, y=1):
        self.wins += y
        # self.play()  
        print('%s has %d wins' % (self.name, self.wins))


t = call_of_duty('tom', 28)

t.won_game(3)
t.play(3)

p = gamer('paul', 72)

p.play(19)