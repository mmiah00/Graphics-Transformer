from display import *
from draw import *
from parsing import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

parse_file( 'testscript', edges, transform, screen, color )
#parse_file( 'myscript', edges, transform, screen, color )
