import turtle
import random


def random_color():                            # to be prepared for setting tile board in random color
    color = random.choice(['#FFB5C5', '#FFCE86', '#FFFFB5', '#B9BFFF', '#B8DEFF'])
    return color


def color_set():                               # set color set
    global cs1, cs2, cs3, cs4
    cs.up()
    cs.setpos(-120, -100)
    cs.color('black', '#FFB5C5')
    cs.stamp()
    cs1 = cs.clone()
    cs1.forward(60)
    cs1.color('black', '#FFCE86')
    cs2 = cs1.clone()
    cs2.forward(60)
    cs2.color('black', '#FFFFB5')
    cs3 = cs2.clone()
    cs3.forward(60)
    cs3.color('black', '#B9BFFF')
    cs4 = cs3.clone()
    cs4.forward(60)
    cs4.color('black', '#B8DEFF')
    cs.down()


def tile_board():                                       # set tile board
    global t_dict
    t_dict = {}
    for i in range(5):
        for j in range(5):
            t_dict["t" + str(i) + str(j)] = turtle.Turtle("square")
            t_dict["t" + str(i) + str(j)].up()
            t_dict["t" + str(i) + str(j)].shapesize(3, 3, 5)
            t_dict["t" + str(i) + str(j)].speed(10000)
            t_dict["t" + str(i) + str(j)].setpos(27 + 70 * i, 29 + 70 * j)
            t_dict["t" + str(i) + str(j)].down()
            t_dict["t" + str(i) + str(j)].color('white', random_color())
            sc.update()


def tile_coordinate(x, y):                # match coordinates to squares
    global a
    global b
    global c
    temp_y = y
    if c is None and (y < -5 or y > 340 or x < -5 or x > 340):     # eliminate blank space
        a = -1
        b = -1
    else:
        if -5 < x < 60 and -5 < y < 340:
            a = 0
            y_coordinate(temp_y)
            c = None
        elif 65 < x < 130 and -5 < y < 340:
            a = 1
            y_coordinate(temp_y)
            c = None
        elif 135 < x < 200 and -5 < y < 340:
            a = 2
            y_coordinate(temp_y)
            c = None
        elif 205 < x < 270:
            a = 3
            y_coordinate(temp_y)
            c = None
        elif 275 < x < 340:
            a = 4
            y_coordinate(temp_y)
            c = None

    try:                                                        # carry out the main process
        if 0 <= a <= 4 and 0 <= b <= 4 and c is not None:
            global d
            d = t_dict["t" + str(a) + str(b)].fillcolor()
            add_border(a, b)
            sc.update()
            toggle_color(a, b)
            sc.update()
            remove_border(a, b)
            sc.update()
    except:                                          # to avoid scope errors
        pass


def y_coordinate(y):                      # to match y coordinate to b
    global b
    if -5 < y < 60:
        b = 0
    elif 65 < y < 130:
        b = 1
    elif 135 < y < 200:
        b = 2
    elif 205 < y < 270:
        b = 3
    elif 275 < y < 340:
        b = 4


def color_set_coordinate(x, y):          # to match coordinates to color set color
    global c
    if -151 < x < -92 and -131 < y < -70:
        c = '#FFB5C5'
    elif -87 < x < -32 and -131 < y < -70:
        c = '#FFCE86'
    elif -28 < x < 29 and -131 < y < -70:
        c = '#FFFFB5'
    elif 33 < x < 88 and -131 < y < -70:
        c = '#B9BFFF'
    elif 93 < x < 150 and -131 < y < -70:
        c = '#B8DEFF'


def add_border(a, b):                     # to add border to the last selected tile
    t_dict["t" + str(a) + str(b)].pensize(200000)
    t_dict["t" + str(a) + str(b)].speed('slowest')


def remove_border(a, b):                  # to remove border from the last selected tile
    t_dict["t" + str(a) + str(b)].speed('slowest')
    t_dict["t" + str(a) + str(b)].pencolor('white')


def toggle_left_color(a, b):              # if condition permits, toggle the color of the selected tile's left tile
    global c
    if a < 1:
        return
    elif a >= 1 and t_dict["t" + str(a - 1) + str(b)].fillcolor() == d:
        t_dict["t" + str(a - 1) + str(b)].fillcolor(c)              # toggle color
        return toggle_left_color(a - 1, b), toggle_up_color(a - 1, b), toggle_down_color(a - 1, b)


def toggle_right_color(a, b):             # if condition permits, toggle the color of the selected tile's right tile
    global c
    if a > 3:
        return
    elif a <= 3 and t_dict["t" + str(a + 1) + str(b)].fillcolor() == d:
        t_dict["t" + str(a + 1) + str(b)].fillcolor(c)
        return toggle_right_color(a + 1, b), toggle_up_color(a + 1, b), toggle_down_color(a + 1, b)


def toggle_up_color(a, b):               # if condition permits, toggle the color of the tile above it
    global c
    if b > 3:
        return
    elif b <= 3 and t_dict["t" + str(a) + str(b + 1)].fillcolor() == d:
        t_dict["t" + str(a) + str(b + 1)].fillcolor(c)
        return toggle_up_color(a, b + 1), toggle_left_color(a, b + 1), toggle_right_color(a, b + 1)


def toggle_down_color(a, b):             # if condition permits, toggle the color of the tile below it
    global c
    if b < 1:
        return
    elif b >= 1 and t_dict["t" + str(a) + str(b - 1)].fillcolor() == d:
        t_dict["t" + str(a) + str(b - 1)].fillcolor(c)
        return toggle_down_color(a, b - 1), toggle_left_color(a, b - 1), toggle_right_color(a, b - 1)


def toggle_color(a, b):                 # toggle the color of the selected tile and its neighboring
    toggle_left_color(a, b)
    toggle_right_color(a, b)
    toggle_up_color(a, b)
    toggle_down_color(a, b)
    t_dict["t" + str(a) + str(b)].color('black', c)


if __name__ == "__main__":
    sc = turtle.Screen()                     # set screen
    sc.setup(800, 700)
    sc.tracer(0)

    cs = turtle.Turtle('square')             # set color set
    cs.shapesize(3, 3, 5)
    global cs1, cs2, cs3, cs4
    color_set()

    global t_dict                            # set tile board
    tile_board()

    a = -1
    b = -1
    c = None

    turtle.onscreenclick(tile_coordinate)    # set mouse click
    cs.onclick(color_set_coordinate)
    cs1.onclick(color_set_coordinate)
    cs2.onclick(color_set_coordinate)
    cs3.onclick(color_set_coordinate)
    cs4.onclick(color_set_coordinate)

    sc.update()
    sc.mainloop()
