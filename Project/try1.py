import pyglet
from pyglet.gl import *
 
win = pyglet.window.Window()
 
@win.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glBegin(GL_TRIANGLE_FAN)
    '''
    GL_LINES - Draws lines
    GL_POINTS - Draws points
    GL_LINE_STRIP - Full lines
    GL_LINE_LOOP - Closes lines
    GL_TRIANGLES - Creates line_loop for every 3 points
    GL_TRIANGLE_STRIP - Draws trangle for every 3 points, including past ones.
    GL_TRIANGLE_FAN - Draws triangles around a central point.
    '''
    glVertex2i(200, 200)
    glVertex2i(300, 300)
    glVertex2i(250, 250)
    glVertex2i(300, 200)
    glEnd()
 
pyglet.app.run()