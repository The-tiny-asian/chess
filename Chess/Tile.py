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
