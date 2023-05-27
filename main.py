import figures
import interface
import os


def main():
    figures_instances = []
    temp_ans, temp_x, temp_y, temp_x1, temp_y1 = '', '', '', '', ''
    while True:
        print('Pick a figure:')
        print(' 1. Point')
        print(' 2. Line')
        print(' 3. Rectangle')
        print(' 4. Circle')
        temp_ans = input()
        if temp_ans == '1':
            os.system('cls')
            print('Enter x and y coordinates:')
            temp_x = int(input())
            temp_y = int(input())
            figures_instances.append(figures.Point(temp_x, temp_y))
        elif temp_ans == '2':
            os.system('cls')
            print('Enter x and y coordinates of the beginning of the line:')
            temp_x = int(input())
            temp_y = int(input())
            print('Enter x and y coordinates of the end of the line:')
            temp_x1 = int(input())
            temp_y1 = int(input())
            figures_instances.append(figures.Line(temp_x, temp_y, temp_x1, temp_y1))
        elif temp_ans == '3':
            os.system('cls')
            print('Enter x and y coordinates of one of the rectangle vertices:')
            temp_x = int(input())
            temp_y = int(input())
            print('Enter x and y coordinates of the opposite vertex:')
            temp_x1 = int(input())
            temp_y1 = int(input())
            figures_instances.append(figures.Rectangle(temp_x, temp_y, temp_x1, temp_y1))
        elif temp_ans == '4':
            os.system('cls')
            print('Enter x and y coordinates of the center of the circle:')
            temp_x = int(input())
            temp_y = int(input())
            print('Enter the radius of the circle:')
            temp_x1 = int(input())
            figures_instances.append(figures.Circle(temp_x, temp_y, temp_x1))

        os.system('cls')
        print('Figure is written successfully. Do you wish to write another one? (1 - yes, 0 - no')
        temp_x = int(input())
        if temp_x == 0:
            break
        os.system('cls')

    interface_go = interface.TurtleScreen(figures_instances)
    interface_go.show_graph()


if __name__ == '__main__':
    main()
