########################################
# Name:Kendall Brown 
# Collaborators:Mary
# Estimated time spent (hrs): 1
########################################

from pgl import GWindow, GRect

WIDTH = 800
HEIGHT = 600
BRICK_WIDTH = 40
BRICK_HEIGHT = 20
BRICKS_IN_BASE = 15

def draw_pyramid():
    """ 
    Draws a pyramid of bricks centered on the screen with a height of BRICKS_IN_BASE. 
    """
    def build_brick(x,y):
        gw.add(GRect(x-BRICK_WIDTH/2,y-BRICK_HEIGHT/2,BRICK_WIDTH,BRICK_HEIGHT))

    gw = GWindow(WIDTH, HEIGHT)
    middlex=WIDTH/2
    middley=HEIGHT/2
    for i in range (BRICKS_IN_BASE):
        for j in range (i+1):
            x= middlex - (i/2) *BRICK_WIDTH + j*BRICK_WIDTH
            y= middley-(BRICKS_IN_BASE* BRICK_HEIGHT)/2 +BRICK_HEIGHT/2 +i*BRICK_HEIGHT
            build_brick(x,y)

    # You got it from here


















if __name__ == '__main__':
    draw_pyramid()
