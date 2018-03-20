#Import other classes and declare global variables
import GameState as gs
from Tile import Tile
#Create begining game board
gameState = gs.newGame()

def setup():
    size(1000,800)
    textAlign(CENTER)
    rectMode(CENTER)

def draw():
    #Use the global gameState variable
    global gameState
    #Display all items in gameState
    for x in range(8):
        for y in range(8):
            gameState[x][y].display()

def mouseClicked():
    #Use the global gameState variable
    global gameState
    #Buttons
    x = int((mouseX)/100)
    y = int((mouseY)/100)
    if x < 8 and y < 8:
        gameState[x][y].clicked(gameState)
