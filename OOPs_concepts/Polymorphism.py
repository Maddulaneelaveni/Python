
# PROBLEM : Take a class as parent class define draw method in it, child  class as circle as usual draw method should be in child class also then  implement it as method overriding.
# Method overriding

class Shape:
    def draw(self):
        print("Drawing a shape")
class Circle(Shape):
    def draw(self):
        super().draw()
        print("Drawing a circle")
# Object creation and calling
s = Shape()
s.draw()
c = Circle()
c.draw()