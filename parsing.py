

from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         move: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing
See the file script for an example of the file format
"""

def parse_file( fname, points, transform, screen, color ):
    f = open (fname, "r")
    commands = []
    for line in f:
        c = line.split ("\n")
        c.remove ('')
        commands.append (c[0])

    i = 0
    while (i + 1 < len (commands)):
        line = commands[i]
        if line != "quit":
            if line == "line":
                cors = commands[i + 1].split (" ")
                add_edge (points, int (cors[0]), int (cors[1]), int (cors[2]), int (cors[3]), int (cors[4]), int (cors[5]))
                i += 2

            elif line == "ident":
                ident (transform)
                print ("done")
                i += 1

            elif line == "scale":
                params = commands[i + 1].split (" ")
                s = make_scale (int (params[0]), int (params[1]), int(params[2]))
                matrix_mult (s, transform)
                print ("done")
                i += 2

            elif line == "move":
                params = commands[i + 1].split (" ")
                print (params)
                t = make_translate (int (params[0]), int (params[1]), int(params[2]))
                matrix_mult (t, transform)
                print ("done")
                i += 2

            elif line == "rotate":
                params = commands[i + 1].split (" ")
                if (params[0] == "x"):
                    r = make_rotX (int (params[1]))
                    matrix_mult (r, transform)

                elif (params[0] == "y"):
                    r = make_rotY (int (params[1]))
                    matrix_mult (r, transform)

                elif (params[0] == "z"):
                    r = make_rotZ (int (params[1]))
                    matrix_mult (r, transform)
                print ("done")
                i += 2

            elif line == "apply":
                matrix_mult (transform, points)
                print ("done")
                i += 1

            elif line == "display":
                clear_screen (screen)
                draw_lines (points, screen, color)
                display (screen)
                print ("done")
                i += 1

            elif line == "save":
                save_ppm (screen, "pic.png")
                print ("done")
                i += 1
        else:
            file.close()
