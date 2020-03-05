from display import *
from draw import *
from parsing import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

script = open ("myscript", "w")

def draw_road ():
    script.write ("line\n0 250 0 500 250 0\n")

draw_road ()

def draw_legs ():
    x = 75
    while (x < 500):
        script.write ("line\n250 0 " + str (x) + " 0 0\n")
        script.write ("line\n0 0 " + str (x) + " 40 0 0\n")
        script.write ("line\n" + str (x + 40) + " 0 0 " + str (x + 40) +" 250 0\n")
        x += 300

draw_legs ()

def draw_cables (starting_x, ending_x):
    y = 250 + 175 - 25
    while (y > 250):
        script.write ("line\n" + str (starting_x) + " " + str (y) + " 0 " + str (ending_x) + " 250 0\n")
        y -= 20

def draw_beams ():
    x = 85
    draw_cables (x, x - 145)
    while (x < 500):
        script.write ("line\n" + str (x) + " " + "250 0 " + str (x) + " " + str (250 + 175) + " 0\n")
        script.write ("line\n" + str (x) + " " + str (250 + 175) + " 0 " + str (x + 20) + " " + str (250 + 175) + " 0\n")
        script.write ("line\n" + str (x + 20) + " " + str (250 + 175) + " 0 " + str (x + 20) + " 250 0\n")
        draw_cables (x + 20, x + 160)
        draw_cables (x + 300, x + 160)
        x += 300

draw_beams ()

def transformations ():
    script.write ("display\nident\nscale\n2 2 2\napply\ndisplay\nident\nmove\n100 100 0\napply\ndisplay\nident\nrotate\nz 20\nrotate\nx 20\nrotate\ny 20\napply\ndisplay\nident\nrotate\ny 20\napply\ndisplay\nsave\npic.png\n")

transformations ()

parse_file( 'myscript', edges, transform, screen, color )
#parse_file( 'myscript', edges, transform, screen, color )
