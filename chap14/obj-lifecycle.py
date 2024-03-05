# contruction and destruction of classes:

class player:
    lives = 8

    def __init__(self):
        print('player contructed')

    def life_lost(self, y=1):
        self.lives -= y
        print('%d lives lost, %d lives remaining' % (y, self.lives))
        
    
    def __del__(self):
        print('player destructed', john)


john = player()

john.life_lost()
john.life_lost(4)