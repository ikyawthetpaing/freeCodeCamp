class Rectangle:
    def __init__(self, width, height) -> None:
        self.set_width(width)
        self.set_height(height)

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    
    def get_picture(self):
        if (self.width > 50 or self.height > 50):
            return "Too big for picture."
        else:
            line = "*" * self.width + "\n"
            return (line * self.height)
    
    def get_amount_inside(self, shape):
        return self.get_area() // shape.get_area()


class Square(Rectangle):
    def __init__(self, side) -> None:
        self.set_side(side)

    def __str__(self) -> str:
        return f"Square(side={self.width})"

    def set_side(self, side):
        self.width = side
        self.height = side


rect = Rectangle(width=5, height=5)
print(rect.get_picture())
print(rect.get_amount_inside(Rectangle(width=2.5, height=2.5)))
print(str(rect))