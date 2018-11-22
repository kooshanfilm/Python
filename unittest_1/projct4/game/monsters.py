

class Monster:
    sound = 'roar'
    hit_points = 20
    color = 'blue'

    def __init__(self,hit_points=20):
        self.hit_points = hit_points


    def battle_cry(self):
        return self.sound.upper()
