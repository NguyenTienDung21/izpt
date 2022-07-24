class Points:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '\{x: {x},y: {y}\}'.format(x=self.x, y=self.y)

    def __repr__(self):
        return '{} {}'.format(self.x, self.y)
