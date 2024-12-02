class Turtle:
    def __init__(self):
        pass
        self.x = 0
        self.y = 0
    def pos(self):
        return (self.x, self.y)
    def teleport(self, a, b):
        self.x = a
        self.y = b
    def goto(self, a):
        self.x = a[0]
        self.y = a[1]
    def color(self, c):
        pass
    def fillcolor(self, c):
        pass
    def begin_fill(self):
        pass
    def end_fill(self):
        pass
    def circle(self, r):
        pass
    def getscreen(self):
        return self
    def bgcolor(self, c):
        pass
    def hideturtle(self):
        pass
    def speed(self, c):
        pass
