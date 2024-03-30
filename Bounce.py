from vpython import *
#GlowScript 3.0 VPython
# Program Libraries:
from visual import *
from visual.graph import *
# Scene Display
scene.width = 700
scene.height = 600
scene.title = 'Graphing the bounce of a ball bouncing Vertically'
scene.autoscale=False
scene.fullscreen = False
scene.center = vector(0, 10, 10)
# Variables I am Using
t_max = 26 # Program timeout
g = -9.81 # Acceleration due to gravity
y = 10 # initial height of the ball
v = 10 # initial velocity of the ball
dt= 0.006 # Increase of time for each iteration
e = 0.9 # coef. lost of energy in each bounce
k = 0 # friction with air
t = 0 # initial time
# Drawing the objects(floor,ball)
floor= box(height = 0.2, width = 30, length = 30, color = color.green)
ball = sphere(pos = vector(0, y, 0), radius = 1, color = color.red)
# Plotting Graph
f1 = gdisplay(x=0, y=0, width=600, height=600,
          title='MOVEMENT (Y vs T graph)', xtitle="T", ytitle='Y',
          foreground=color.black, background=color.blue,
          xmax=t_max, xmin=0, ymax=15, ymin=0)
f1 = gcurve(color=color.white) # Setting The Graphic Curve
while t < t_max: # main loop
    rate (200) # loops/sec
    
# Differential Equations
    dv = g*dt - k*v*dt
    v = v + dv
    dy = v*dt
    y = y + dy
    t = t + dt
# Bounce conditions
    if  y < ball.radius:
        v = -v*e
        y = ball.radius

# Scene updating
    ball.pos.y = y
# Drawing in the plot
    f1.plot(pos = (t , y))
  
