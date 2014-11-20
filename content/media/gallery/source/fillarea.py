import vcs
canvas = vcs.init()

# Convex shapes don't fill well; you have to break them into multiple parts
# Here we're creating the letter "v", so we will break it into two halves across the middle
v = canvas.createfillarea('v')

# If you want to specify different colors for each part, you can supply colors as a list
v.color = 152

# v.x[0] and v.y[0] will describe the left half; v.x[1] and v.y[1] describe the second half
v.x = [[0.1, 0.12, 0.15, 0.15], [0.15, 0.18, 0.2, 0.15]]
v.y = [[0.3, 0.3, 0.16, 0.1], [0.16, 0.3, 0.3, 0.1]]


c = canvas.createfillarea('c')
c.color = 22

# Break the letter C into three parts; top, left, and bottom
c.x = [[0.21, 0.3, 0.3, 0.23], [0.21, 0.23, 0.23, 0.21], [0.21, 0.23, 0.3, 0.3]]
c.y = [[0.3, 0.3, 0.28, 0.28], [0.3, 0.28, 0.12, 0.1], [0.1, 0.12, 0.12, 0.1]]


s = canvas.createfillarea('s')
s.color = 60

# Break the letter S into 5 parts: Top, left, middle, right, bottom
s.x = [[0.31, 0.4, 0.4, 0.33], [0.31, 0.33, 0.33, 0.31], [0.31, 0.33, 0.4, 0.38], [0.4, 0.4, 0.38, 0.38], [0.38, 0.4, 0.31, 0.31]]
s.y = [[0.3, 0.3, 0.28, 0.28], [0.3, 0.28, 0.22, 0.2], [0.2, 0.22, 0.22, 0.2], [0.22, 0.1, 0.12, 0.2], [0.12, 0.1, 0.1, 0.12]]

canvas.plot(v)
canvas.plot(c)
canvas.plot(s)

# Fillarea is not limited to quadrilaterals.

# Eqilateral triangle
tri = canvas.createfillarea("tri")
tri.color = 200

tri.x = [.6, .75, .9]
tri.y = [.1, .15 * (3 ** .5) + .1, .1]

canvas.plot(tri)

# Regular Dodecahedron
dodeca = canvas.createfillarea("dodeca")
dodeca.color = 250

import math

center = (.5, .5)
radius = .2
theta = math.radians(30)

dodeca.x = []
dodeca.y = []

for point in range(12):
    theta_p = point * theta
    dodeca.x.append( center[0] + radius * math.cos(theta_p))
    dodeca.y.append( center[1] + radius * math.sin(theta_p))

canvas.plot(dodeca)

#Set the window size
canvas.geometry(600, 600)
canvas.update()

canvas.png("/tmp/fillarea.png")