########################################
# Name:Kendall Brown
# Collaborators:Mary
# Estimate time spent (hrs):1.5
########################################

from pgl import GWindow, GRect, GLabel, GLine
import random

GW_WIDTH = 500                      # Width of window
GW_HEIGHT = 500                     # Height of window
SQUARE_SIZE = 50                    # Width and height of square
SCORE_DX = 10                       # Distance from left of window to origin
SCORE_DY = 10                       # Distance up from bottom of window to baseline
SCORE_FONT = "bold 40pt 'serif'"    # Font for score

def clicky_box():

    # Defining the callback function, which you won't need until Part C
    def on_mouse_down(event):
        print("You clicked the window!") # Delete this once you start Part C
        mousex=event.get_x()
        mousey=event.get_y()
        mouseinfo=gw.get_element_at(mousex, mousey)

        if mouseinfo==the_square:
            gw.score +=1 #1+score
            new_x=random.randint(0,GW_WIDTH - SQUARE_SIZE)
            new_y=random.randint(0,GW_HEIGHT - SQUARE_SIZE) #move square
            the_square.set_location(new_x,new_y)
            scoreboard.set_label(str(gw.score))



    # Down here you should initialize the window and draw the initial square
    # Make sure you tab it in so that it is part of the clicky_box function

    gw = GWindow(GW_WIDTH, GW_HEIGHT)
    
    xcenter= GW_WIDTH/2
    ycenter=GW_HEIGHT/2
	
    the_square= GRect(xcenter-SQUARE_SIZE/2, ycenter-SQUARE_SIZE/2, SQUARE_SIZE, SQUARE_SIZE)
    the_square.set_color('Blue')
    the_square.set_filled(True)
    gw.add(the_square) #make the first square

    gw.score=0
    scoreboard=GLabel(str(gw.score), SCORE_DX, GW_HEIGHT-SCORE_DY)
    scoreboard.set_font(SCORE_FONT)
    gw.add(scoreboard) #put the score at the bottom
    gw.add_event_listener ("click", on_mouse_down)













if __name__ == '__main__':
    clicky_box()
