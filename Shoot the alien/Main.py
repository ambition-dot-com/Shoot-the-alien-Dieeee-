import pgzrun
from random import randint

WIDTH = 500
HEIGTH = 500

TITLE = "Shoot the alien!!!! Dieeeeee!"
message = ""

#Character is basically Actor. Actor is a built in objject in pgzero.
#It can interact with other objects and can move on the screen. 
alien = Actor("alien")


def draw():
    screen.clear()
    screen.fill(color = "purple")
    #Drawing the alien actor on the screen.
    alien.draw()


def place_alien():
    alien.x = randint(50,WIDTH-50)
    alien.y = randint(50,HEIGTH-50)


place_alien()









pgzrun.go()