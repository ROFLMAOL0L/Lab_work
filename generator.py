import figures
import interface
import random

screen_divider = 50
max_x, max_y = 200, 200   # Maximum possible value of x and y for any dot


def create_figures(figures_amount):
    figure_mas = []
    for i in range(0, figures_amount):
        # We can define x and y here since every figure is based on them.
        x, y = random.randint(-max_x, max_x), random.randint(-max_y, max_y)
        x -= x % screen_divider
        y -= y % screen_divider
        # Randomly choosing a figure to add
        figure_choice = random.randint(2, 4)
        if figure_choice == 2:
            x2, y2 = x, y
            while x2 == x:
                x2 = random.randint(-max_x, max_x)
                x2 -= x2 % screen_divider
            while y2 == y:
                y2 = random.randint(-max_y, max_y)
                y2 -= y2 % screen_divider
            figure_mas.append(figures.Line(x, y, x2, y2))
        elif figure_choice == 3:
            x2, y2 = x, y
            while x2 == x:
                x2 = random.randint(-max_x, max_x)
                x2 -= x2 % screen_divider
            while y2 == y:
                y2 = random.randint(-max_y, max_y)
                y2 -= y2 % screen_divider
            figure_mas.append(figures.Rectangle(x, y, x2, y2))
        elif figure_choice == 4:
            radius = random.randint(screen_divider, max_x)
            radius -= radius % screen_divider
            figure_mas.append(figures.Circle(x, y, radius))

    # Draw the graph
    interface_go = interface.TurtleScreen(figure_mas)
    interface_go.show_graph()


def main():
    create_figures(4)


if __name__ == '__main__':
    main()
