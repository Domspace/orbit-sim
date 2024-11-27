class Velocity:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_velocity(self):
        return [self.x, self.y]

    def set_velocity(self, v):
        self.x = v[0]
        self.y = v[1]
        return

    def add_velocity(self, v):
        #print("added", v)
        self.x += v[0]
        self.y += v[1]
        return
