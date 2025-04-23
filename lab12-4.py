import math

class RegularShape:
    def __init__(self, shape_type):
        self.shape_type = shape_type.lower()
        self.dimensions = {}

    def set_dimensions(self, **kwargs):
        self.dimensions = kwargs

    def calculate_perimeter(self):
        if self.shape_type == "circle":
            radius = self.dimensions.get("radius", 0)
            return 2 * math.pi * radius
        elif self.shape_type == "square":
            side = self.dimensions.get("side", 0)
            return 4 * side
        elif self.shape_type == "triangle":
            side = self.dimensions.get("side", 0)
            return 3 * side
        elif self.shape_type == "rectangle":
            length = self.dimensions.get("length", 0)
            width = self.dimensions.get("width", 0)
            return 2 * (length + width)
        else:
            raise ValueError("Unsupported shape type")

    def calculate_area(self):
        if self.shape_type == "circle":
            radius = self.dimensions.get("radius", 0)
            return math.pi * radius ** 2
        elif self.shape_type == "square":
            side = self.dimensions.get("side", 0)
            return side ** 2
        elif self.shape_type == "triangle":
            base = self.dimensions.get("base", 0)
            height = self.dimensions.get("height", 0)
            return 0.5 * base * height
        elif self.shape_type == "rectangle":
            length = self.dimensions.get("length", 0)
            width = self.dimensions.get("width", 0)
            return length * width
        else:
            raise ValueError("Unsupported shape type")

shape = RegularShape("circle")
shape.set_dimensions(radius=5)
print("Circle Perimeter:", shape.calculate_perimeter())
print("Circle Area:", shape.calculate_area())