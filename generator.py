import figures
import interface
import random
import math

screen_divider = 50
screen_size = [300, 300]
max_x, max_y = 200, 200   # Maximum possible value of x and y for any dot


class RegionTextPos:
    def __init__(self, region_character_sample, pos_x, pos_y, r):
        self.region_character = region_character_sample
        self.x, self.y = pos_x, pos_y
        self.radius = r


def define_region(dot_x, dot_y, figures_mas_2):
    region_character = [0 for i in range(len(figures_mas_2))]
    for i in range(len(figures_mas_2)):
        region_character[i] = figures_mas_2[i].compare(dot_x, dot_y)
    return region_character


def compare_with_region(dot_x1, dot_y1, region_character_sample, figures_mas_3):
    region_character_1 = define_region(dot_x1, dot_y1, figures_mas_3)
    if region_character_sample == region_character_1:
        return True
    else:
        return False


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

    regions_text_positions = define_regions(figure_mas)

    # Draw the graph
    interface_go = interface.TurtleScreen(figure_mas, regions_positions=regions_text_positions)
    interface_go.show_graph()


def define_regions(figures_mas):
    # Defining regions by a mas of 0 of 1 of the same length as amount of figures,
    # where 1 means a point belongs to a figure (in a case of line - a point is above the line)
    # and 0 means it`s outside the figure (in case of line - a point is under the line)
    region_indices = []
    for temp_x in range(-350, 350):
        for temp_y in range(-350, 350):
            temp_indices = [0 for q in range(len(figures_mas))]
            for i in range(0, len(figures_mas)):
                if figures_mas[i].compare(temp_x, temp_y):
                    temp_indices[i] = 1
            if temp_indices not in region_indices:
                region_indices.append(temp_indices)

    for i in range(len(figures_mas)):
        print(figures_mas[i].type)
    for i in range(len(region_indices)):
        print(region_indices[i])

    # Checking for "squares" of screen divider side to belong to an area, if so - write a number of the area on it
    regions_text_pos = []
    regions_objects = []

    # For every dot
    for temp_x in range(-350, 350, screen_divider // 4):
        for temp_y in range(-350, 350, screen_divider // 4):
            temp_region_character = define_region(temp_x, temp_y, figures_mas)
            temp_r = 5
            # Going for the circle with every possible radius
            while temp_r + temp_x < screen_size[0] and temp_x - temp_r > -320 \
                    and temp_y - temp_r > -320 and temp_r + temp_y < screen_size[1]:
                angle = 0
                pass_result = True
                while angle < 360:
                    if not compare_with_region(temp_x + math.cos(angle / 180 * 3.1415926) * temp_r,
                                               temp_y + math.sin(angle / 180 * 3.1415926) * temp_r,
                                               temp_region_character, figures_mas):
                        pass_result = False
                        angle += 360
                    angle += 10

                # The circle is fully in the region
                if pass_result:
                    #print('a)')
                    change_result = True
                    if len(regions_objects) == 0:
                        #print('AD:LFJSD:LJ')
                        regions_objects.append(RegionTextPos(temp_region_character, temp_x, temp_y, temp_r))
                    for q in range(len(regions_objects)):
                        if regions_objects[q].region_character == temp_region_character:
                            if regions_objects[q].radius < temp_r:
                                #print('Better one found')
                                regions_objects[q] = RegionTextPos(temp_region_character, temp_x, temp_y, temp_r)
                            change_result = False
                    if change_result:
                        #print('New one found')
                        regions_objects.append(RegionTextPos(temp_region_character, temp_x, temp_y, temp_r))
                temp_r += 5
                #print(temp_r)

    print(len(regions_objects))
    for i in range(len(regions_objects)):
        regions_text_pos.append((regions_objects[i].x, regions_objects[i].y, regions_objects[i].radius))

    '''
    for i in range(len(region_indices)):
        regions_text_pos.append((0, 0))
    for temp_x in range(-350, 350, screen_divider):
        for temp_y in range(-350, 350, screen_divider):
            temp_indices = [[0 for j in range(len(figures_mas))] for i in range(0, 4)]
            for i in range(0, len(figures_mas)):
                if figures_mas[i].compare(temp_x, temp_y):
                    temp_indices[0][i] += 1
            for i in range(0, len(figures_mas)):
                if figures_mas[i].compare(temp_x + screen_divider, temp_y):
                    temp_indices[1][i] += 1
            for i in range(0, len(figures_mas)):
                if figures_mas[i].compare(temp_x, temp_y + screen_divider):
                    temp_indices[2][i] += 1
            for i in range(0, len(figures_mas)):
                if figures_mas[i].compare(temp_x + screen_divider, temp_y + screen_divider):
                    temp_indices[3][i] += 1
            check_result = True
            for i in range(1, 4):
                if temp_indices[i] != temp_indices[0]:
                    check_result = False
            if temp_x == temp_y == 0:
                check_result = False
            if check_result:
                print(temp_indices)
                for i in range(len(region_indices)):
                    if region_indices[i] == temp_indices[0]:
                        print('lol', region_indices[i], ' == ', temp_indices[0])
                        if regions_text_pos[i] == (0, 0):
                            regions_text_pos[i] = (temp_x, temp_y)   # +25 is just for it to look good
                            '''
    return regions_text_pos


def main():
    create_figures(4)


if __name__ == '__main__':
    main()
