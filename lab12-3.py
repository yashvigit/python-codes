import math

class Solid:
    def __init__(self):
        self.dimensions = {}

    def set_dimensions(self, **kwargs):
        self.dimensions = kwargs

    def surface_area(self):
        raise NotImplementedError("This method should be implemented by subclasses.")

    def volume(self):
        raise NotImplementedError("This method should be implemented by subclasses.")

class Sphere(Solid):
    def surface_area(self):
        radius = self.dimensions.get('radius', 0)
        return 4 * math.pi * radius ** 2

    def volume(self):
        radius = self.dimensions.get('radius', 0)
        return (4/3) * math.pi * radius ** 3

class Cube(Solid):
    def surface_area(self):
        side = self.dimensions.get('side', 0)
        return 6 * side ** 2

    def volume(self):
        side = self.dimensions.get('side', 0)
        return side ** 3

sphere = Sphere()
sphere.set_dimensions(radius=5)
print("Sphere Surface Area:", sphere.surface_area())
print("Sphere Volume:", sphere.volume())

cube = Cube()
cube.set_dimensions(side=3)
print("Cube Surface Area:", cube.surface_area())
print("Cube Volume:", cube.volume())