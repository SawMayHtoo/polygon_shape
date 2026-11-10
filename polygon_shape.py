"""EXERCISE: finish the Polygon class. Use import turtle (not selective imports)."""
import turtle


class Polygon:
    def __init__(self, x, y, sides, side_length, color, pen_size=3, angle=0):
        """Store the first vertex, number of sides, side length, color,
        line width, angle, and an internal turtle.Turtle object.
        Reject sides < 3, side_length <= 0, and pen_size <= 0.
        """
        if sides < 3:
            raise ValueError("Polygon must have at least 3 sides.")
        if side_length <= 0:
            raise ValueError("side_length must be positive.")
        if pen_size <= 0:
            raise ValueError("pen_size must be positive.")

        self.x = x
        self.y = y
        self.sides = sides
        self.side_length = side_length
        self.color = color
        self.pen_size = pen_size
        self.angle = angle

        # Create an independent Turtle instance for this polygon
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        self.turtle.speed(0)

    def draw(self):
        """Draw a regular polygon using left(360 / sides)."""
        t = self.turtle
        t.penup()
        t.goto(self.x, self.y)
        t.setheading(self.angle)
        t.color(self.color)
        t.pensize(self.pen_size)
        
        t.pendown()
        turn_angle = 360 / self.sides
        for _ in range(self.sides):
            t.forward(self.side_length)
            t.left(turn_angle)
        t.penup()

    def move_to(self, x, y):
        """Update the starting vertex; clear only this polygon; redraw."""
        self.x = x
        self.y = y
        self.turtle.clear()
        self.draw()