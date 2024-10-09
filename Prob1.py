############################################################
# Name:Kendall Brown
# Name(s) of anyone worked with:Chat
# Est time spent (hr):2 hours
############################################################

from pgl import GWindow, GRect, GOval, GLine, GLabel
# Setting up initial window dimensions.
WIDTH = 400
HEIGHT = 400

def draw_image():
    """ Creates a window and draws a 4-square flag with different colors in each quadrant """

    # Create the window
    gw = GWindow(WIDTH, HEIGHT)
    
    w = WIDTH // 2  # Half of width for quadrants
    h = HEIGHT // 2 # Half of height for quadrants

    # Top-left (red)
    rect1 = GRect(0, 0, w, h)
    rect1.set_filled(True)
    rect1.set_fill_color("red")
    gw.add(rect1)

    # Top-right (blue)
    rect2 = GRect(w, 0, w, h)
    rect2.set_filled(True)
    rect2.set_fill_color("blue")
    gw.add(rect2)

    # Bottom-left (yellow)
    rect3 = GRect(0, h, w, h)
    rect3.set_filled(True)
    rect3.set_fill_color("yellow")
    gw.add(rect3)

    # Bottom-right (green)
    rect4 = GRect(w, h, w, h)
    rect4.set_filled(True)
    rect4.set_fill_color("green")
    gw.add(rect4)

    # Draw lines to divide the flag into quadrants
    gw.add(GLine(0, h, WIDTH, h))  # Horizontal line
    gw.add(GLine(w, 0, w, HEIGHT)) # Vertical line

    # Add a label in the center
    label = GLabel("My Flag", WIDTH // 2 - 30, HEIGHT // 2)
    gw.add(label)    
    # And now it is your turn! Add your code below! Make sure you meet all the requirements!




if __name__ == '__main__':
    draw_image()
