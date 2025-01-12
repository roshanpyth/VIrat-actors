import pgzrun
from random import randint
TITLE=" short game with actors"
message=""
WIDTH=800
HEIGHT=400
#actor is a built in object that presents the image and it responds to all the events
alien= Actor("viratalien.png")
alien.pos=50,50

def draw():
    screen.clear()
    screen.fill(color="Blue")
    alien.draw()
    screen.draw.text(message,center=(100,20), color="Orange",fontsize=35)
def place_alien():
    alien.x= randint(50, WIDTH-100)
    alien.y=randint(50,HEIGHT-100)
def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        message="Good shot!"
        place_alien()
    else:
        message="You are out"
    
place_alien()
pgzrun.go()


    
