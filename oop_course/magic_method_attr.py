class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y

    def __getattribute__(self, name):
        if name == "x":
            raise ValueError("доступ запрещен")
        else:
            return object.__getattribute__(self, name)

    def __setattr__(self, name, value):
        if name == "z":
            raise AttributeError("недопустимое имя атрибута")
        else:
            object.__setattr__(self, name, value)

    def __getattr__(self, name):
        return False

    def __delattr__(self, name):
        print("__getattr__: " + name)
        object.__delattr__(self, name)


pt1 = Point(1, 2)
pt2 = Point(10, 20)
del pt1.x
print(pt1.__dict__)
