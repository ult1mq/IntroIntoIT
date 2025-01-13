class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        print(self.radius)

    def set_radius(self, new_radius):
        self.radius = new_radius


c = Circle(5)
c.set_radius(4)
print(c.get_radius())
