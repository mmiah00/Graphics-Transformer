"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

def make_translate( x, y, z ):
    ans = new_matrix
    ident (ans)
    params = [x,y,z]
    ans[0][3] = x
    ans[1][3] = y
    ans[2][3] = z

    # for i in range (len (params)):
    #     ans [i][3] = params[i]
    return ans

def make_scale( x, y, z ):
    ans = new_matrix()
    params = [x,y,z]
    for i in range (len (params)):
        ans [i][i] = params[i]
    return ans
    # ans[0][0] = x
    # ans[1][1] = y
    # ans[2][2] = z
    # ans[3][3] = 1

def make_rotX( theta ):
    ans = new_matrix ()
    ident (ans)
    ans[1][1] = math.cos (theta)
    ans[1][2] = math.sin (theta)
    ans[2][1] = -1 * math.sin (theta)
    ans[2][2] = math.cos (theta)
    return ans

def make_rotY( theta ):
    ans = new_matrix ()
    ident (ans)
    ans[0][0] = math.cos (theta)
    ans[0][2] = -1 * math.sin (theta)
    ans[2][0] = math.sin (theta)
    ans[2][2] = math.cos (theta)
    return ans

def make_rotZ( theta ):
    ans = new_matrix ()
    ident (ans)
    ans[0][0] = math.cos (theta)
    ans[1][0] = -1 * math.sin (theta)
    ans[0][1] = math.sin (theta)
    ans[1][1] = math.cos (theta)
    return ans

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    s = ''
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            s+= str(matrix[c][r]) + ' '
        s+= '\n'
    print(s)

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            if r == c:
                matrix[c][r] = 1
            else:
                matrix[c][r] = 0

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):

    point = 0
    for row in m2:
        #get a copy of the next point
        tmp = row[:]

        for r in range(4):
            m2[point][r] = (m1[0][r] * tmp[0] +
                            m1[1][r] * tmp[1] +
                            m1[2][r] * tmp[2] +
                            m1[3][r] * tmp[3])
        point+= 1


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
#
# edges = [[3, 4, 0, 1],
#          [2, 7, 2, 1],
#          [1, 8, 9, 2],
#          [9, 1, 3, 7],
#          [8, 9, 10, 11]]
#
# matrix_mult (make_rotX (30), edges)
# print_matrix (edges)
