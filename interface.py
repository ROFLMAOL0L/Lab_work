import turtle
import main
from tkinter import *
from PIL import Image
from generator import screen_divider


class TurtleScreen:
    def __init__(self, figures_mas, regions_positions=None):
        # Initialise the turtle library, get the figures list
        self.screen = turtle.getscreen()
        self.turtle_pen = turtle.Turtle()
        self.turtle_pen.speed(0)
        self.figures = figures_mas
        self.screen_width, self.screen_height = self.screen.screensize()[0], self.screen.screensize()[1]
        self.regions_text_pos = regions_positions

    def draw_figure(self, figure_instance):
        # Draw a point
        if figure_instance.type == 'Point':
            self.turtle_pen.up()
            self.turtle_pen.goto(figure_instance.x, figure_instance.y)
            self.turtle_pen.down()
            self.turtle_pen.dot(5, (0, 0, 0))
        # Draw a line
        elif figure_instance.type == 'Line':
            self.turtle_pen.up()
            self.turtle_pen.goto(figure_instance.x, figure_instance.y)
            self.turtle_pen.down()
            self.turtle_pen.goto(figure_instance.x_end, figure_instance.y_end)
        # Draw a rectangle
        elif figure_instance.type == 'Rectangle':
            temp_vertices = figure_instance.vertices
            self.turtle_pen.up()
            self.turtle_pen.goto(temp_vertices[0][0], temp_vertices[0][1])
            self.turtle_pen.down()
            # Here's the reason why vertices are stored in that strange way, it lets the code go through them one by one
            for i in range(len(temp_vertices)):
                self.turtle_pen.goto(temp_vertices[(i + 1) % 4][0], temp_vertices[(i + 1) % 4][1])
        # Draw a circle
        elif figure_instance.type == 'Circle':
            self.turtle_pen.up()
            # Subtract radius since turtle draws circles that way
            self.turtle_pen.goto(figure_instance.x,
                                 figure_instance.y - figure_instance.radius)
            self.turtle_pen.down()
            self.turtle_pen.circle(figure_instance.radius)

    def show_graph(self, plane_lines=False):
        # Draw every line of Oxy plane
        turtle.colormode(255)
        self.turtle_pen.pencolor((200, 200, 200))
        for i in range(-self.screen_width, self.screen_width, screen_divider):
            self.turtle_pen.up()
            self.turtle_pen.goto(i, -self.screen_height - 100)
            self.turtle_pen.down()
            self.turtle_pen.goto(i, self.screen_height + 100)
            self.turtle_pen.up()
        for i in range(-self.screen_height, self.screen_height, screen_divider):
            self.turtle_pen.up()
            self.turtle_pen.goto(-self.screen_width - 100, i)
            self.turtle_pen.down()
            self.turtle_pen.goto(self.screen_width + 100, i)

        # Draw a Oxy plane
        turtle.width(2)
        self.turtle_pen.pencolor((0, 0, 0))
        self.turtle_pen.up()
        self.turtle_pen.goto(0, -self.screen_height - 100)
        self.turtle_pen.down()
        self.turtle_pen.goto(0, self.screen_height + 100)
        self.turtle_pen.up()
        self.turtle_pen.goto(-self.screen_width - 100, 0)
        self.turtle_pen.down()
        self.turtle_pen.goto(self.screen_width + 100, 0)
        turtle.width(3)

        # Draw every figure in the figures list
        for i in range(len(self.figures)):
            self.draw_figure(self.figures[i])
        self.turtle_pen.hideturtle()

        # Write regions names if given
        if self.regions_text_pos is not None:
            for i in range(len(self.regions_text_pos)):
                self.turtle_pen.up()
                self.turtle_pen.goto((self.regions_text_pos[i][0], self.regions_text_pos[i][1]))
                self.turtle_pen.down()
                self.turtle_pen.write(str(i), font=("Arial", 8 + self.regions_text_pos[i][2] // 10, "normal"))
                '''self.turtle_pen.goto((self.regions_text_pos[i][0], self.regions_text_pos[i][1] - self.regions_text_pos[i][2]))
                self.turtle_pen.circle(self.regions_text_pos[i][2])'''

        # I really don`t know what is that but Turtle doesn't close without this line
        self.screen.mainloop()


# I`ve done these lines of code `cause I kept running this file instead of main
if __name__ == '__main__':
    main.main()

