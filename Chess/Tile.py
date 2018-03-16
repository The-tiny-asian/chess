#Import the logic for displaying spaces
import PieceLogic as pl

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
            rect(self.x*100+50,self.y*100+50,100,100,10)
        elif self.isWhite or self.piece == " ":
            fill(255)
            rect(self.x*100+50,self.y*100+50,100,100,10)
            
        else:
            fill(0)
            rect(self.x*100+50,self.y*100+50,100,100,10)
        if self.isWhite:
            fill(0)
            text(self.piece,self.x*100+50,self.y*100+50)
        else:
            fill(255)
            text(self.piece,self.x*100+50,self.y*100+50)
        
    #Method to replace the tile's current piece with a new one
    def newPiece(self, newPiece, newTeam):
        self.piece = newPiece
        self.isWhite = newTeam
    
    #A piece will either be selected or not selected
    def deselect(self):
        self.selected = False
    
    def select(self, incoming):
        self.incoming = incoming
        self.selected = True
    
    #What to do when a piece is clicked
    def clicked(self,gameState):
        
        #If a piece was already selected, 
        #it will replace its own piece and 
        #remove the other piece
        if self.selected:
            self.newPiece(self.incoming.piece,self.incoming.isWhite)
            gameState[self.incoming.x][self.incoming.y].newPiece(" ",True)
            for x in range(8):
                for y in range(8):
                    gameState[x][y].deselect()
        
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
                pl.rookCheck(self,gameState)
            elif self.piece == "Knight":
                pl.knightCheck(self,gameState)
            elif self.piece == "Pawn":
                pl.pawnCheck(self,gameState)
            #elif self.piece == "Bishop":
                
            elif self.piece == "King":
                pl.kingCheck(self,gameState)
                
            #elif self.piece == "Queen":
