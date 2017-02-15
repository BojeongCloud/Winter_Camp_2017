class Rectangle:
    def __init__(self, width = 1, height = 1):
        self.set_width(width)
        self.set_height(height)

    def set_width(self, width):
        self.width = width

    def get_width(self):
        return self.width

    def set_height(self, height):
        self.height = height

    def get_height(self):
        return self.height

    def get_area(self):
        return self.get_width() * self.get_height()

rectangle = Rectangle()
print("사각형의 너비는", rectangle.get_width(), "입니다.")
print("사각형의 높이는", rectangle.get_height(), "입니다.")
print("사각형의 넓이는", rectangle.get_area(), "입니다.\n")

rectangle.set_width(2)
rectangle.set_height(3)
print("사각형의 너비와 높이를 각각 2 와 3 으로 수정!\n")
print("사각형의 너비는", rectangle.get_width(), "입니다.")
print("사각형의 높이는", rectangle.get_height(), "입니다.")
print("사각형의 넓이는", rectangle.get_area(), "입니다.")
