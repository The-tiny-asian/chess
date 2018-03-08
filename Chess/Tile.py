#Tile class, contains an x, y, 
class Tile:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.selected = False
        self.piece = " "
        self.isWhite = False
    #Display the tile
    def display(self):
        if self.selected:
            fill(128)
        else:
            fill(255)
        rect(self.x*100+50,self.y*100+50,100,100,10)
        fill(0)
        text(self.piece,self.x*100+50,self.y*100+50)
    
    #Method to replace the tile's current piece with a new one
    def newPiece(self, newPiece, newTeam):
        self.piece = newPiece
        self.isWhite = newTeam
    
    #A piece will either be selected or not selected
    def deselect(self):
        self.selected = False
    
    def select(self):
        self.selected = True
    
    #What to do when a piece is clicked
    def clicked(self,gameState):
        
        #If a piece was already selected, 
        #it will replace its own piece and 
        #remove the other piece
        if self.selected:
            #TODO: add this stuff
            return
        
        #Otherwise, it will select specific tiles 
        #depending on what piece it is 
        else:
            
            #First it deselects every tile
            for x in range(8):
                for y in range(8):
                    gameState[x][y].deselect()
            
            #Then it will check what piece it is and act accordingly
            #I moved all these methods down to make it more readable
            if self.piece == "Rook":
                rookCheck(self.isWhite, gameState, self.x, self.y)
            elif self.piece == "Knight":
                knightCheck(self.isWhite, gameState, self.x, self.y)
            #elif self.piece == "Bishop":
                
            #elif self.piece == "King":
                
            #elif self.piece == "Queen":
                
            #elif self.piece == "Pawn":
    
    #These methods are used to get variables from the tile
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getPiece(self):
        return self.piece
    
    def getTeam(self):
        return self.isWhite
    
#Method to display movement options specific to the rook
def rookCheck(isWhite, gameState, x, y):
    for tileX in range(7-x):
        rightX = x + tileX + 1
        if gameState[rightX][y].getPiece() == " ":
            gameState[rightX][y].select()
        elif gameState[rightX][y].getTeam() != isWhite:
            gameState[rightX][y].select()
            break
        else:
            break
    for tileX in range(x-1):
        leftX = x - tileX - 1
        if gameState[leftX][y].getPiece() == " ":
            gameState[leftX][y].select()
        elif gameState[leftX][y].getTeam() != isWhite:
            gameState[leftX][y].select()
            break
        else:
            break
    
    for tileY in range(7-y):
        downY = y + tileY + 1
        if gameState[x][downY].getPiece() == " ":
            gameState[x][downY].select()
        elif gameState[x][downY].getTeam() != isWhite:
            gameState[x][downY].select()
            break
        else:
            break
    if y - 1 >= 0:
        for tileY in range(y-1):
            upY = y - tileY - 1
            if gameState[x][upY].getPiece() == " ":
                gameState[x][upY].select()
            elif gameState[x][upY].getTeam() != isWhite:
                gameState[x][upY].select()
                break
            else:
                break

#Method to display movement options specific to the knight
def knightCheck(isWhite, gameState, x, y):
    if x+2 < 8 and y + 1 < 8:
        if gameState[x+2][y+1].getTeam() is not isWhite or (gameState[x+2][y+1].getPiece is " "):
            gameState[x+2][y+1].select()
    if x+2 < 8 and y - 1 < 8:
        if gameState[x+2][y-1].getTeam() is not isWhite or (gameState[x+2][y-1].getPiece is " "):
            gameState[x+2][y-1].select()
    if x-2 < 8 and y + 1 < 8:
        if gameState[x-2][y+1].getTeam() is not isWhite or (gameState[x-2][y+1].getPiece is " "):
            gameState[x-2][y+1].select()
    if x-2 < 8 and y - 1 < 8:
        if (gameState[x-2][y-1].getTeam() != isWhite) or (gameState[x-2][y-1].getPiece == " "):
            gameState[x-2][y-1].select()
    if x+1 < 8 and y + 2 < 8:
        if gameState[x+1][y+2].getTeam() is not isWhite or (gameState[x+1][y+2].getPiece is " "):
            gameState[x+1][y+2].select()
    if x+1 < 8 and y - 2 < 8:
        if gameState[x+1][y-2].getTeam() is not isWhite or (gameState[x+1][y-2].getPiece is " "):
            gameState[x+1][y-2].select()
    if x-1 < 8 and y + 2 < 8:
        if gameState[x-1][y+2].getTeam() is not isWhite or (gameState[x-1][y+2].getPiece is " "):
            gameState[x-1][y+2].select
    if x-1 < 8 and y - 2 < 8:
        if gameState[x-1][y-2].getTeam() is not isWhite or (gameState[x-1][y-2].getPiece is " "):
            gameState[x-1][x-2].select
