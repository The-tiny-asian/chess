#Import the logic for displaying spaces and gamestate for checks/checkmates
#Raheem and Emmanuel
import PieceLogic as pl
import GameState as gs

#Tile class, contains an x, y, 
class Tile:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.selected = False
        self.piece = " "
        self.isWhite = False
    #Display the tile
    #Emmanuel Luna
    def display(self, grey):
        if self.selected:
            fill(104,164,240)
        elif grey:
            fill(255)
        else:
            fill(225)
        rect(self.x*100+50,self.y*100+50,100,100,10)
        if self.piece == "Pawn":
             if self.isWhite:
                img = loadImage("Icons/PawnWhite.png")
             else:
                 img = loadImage("Icons/PawnBlack.png")
        elif self.piece == "Knight":
             if self.isWhite:
                img = loadImage("Icons/KnightWhite.png")
             else:
                 img = loadImage("Icons/KnightBlack.png")
        elif self.piece == "Rook":
             if self.isWhite:
                img = loadImage("Icons/RookWhite.png")
             else:
                 img = loadImage("Icons/RookBlack.png")
        elif self.piece == "Bishop":
             if self.isWhite:
                img = loadImage("Icons/BishopWhite.png")
             else:
                 img = loadImage("Icons/BishopBlack.png")
        elif self.piece == "Queen":
             if self.isWhite:
                img = loadImage("Icons/QueenWhite.png")
             else:
                 img = loadImage("Icons/QueenBlack.png")
        elif self.piece == "King":
             if self.isWhite:
                img = loadImage("Icons/KingWhite.png")
             else:
                 img = loadImage("Icons/KingBlack.png")
        else:
             return
        img.resize(80,80)
        imageMode(CENTER)
        image(img,self.x*100+50,self.y*100+50)
        
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
            gs.gameChecks(gameState)
        
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
                tileList = pl.rookCheck(self,gameState)
            elif self.piece == "Knight":
                tileList = pl.knightCheck(self,gameState)
            elif self.piece == "Pawn":
                tileList = pl.pawnCheck(self,gameState)
            elif self.piece == "Bishop":
                tileList = pl.bishopCheck(self,gameState)
            elif self.piece == "King":
                tileList = pl.kingCheck(self,gameState)
            elif self.piece == "Queen":
                tileList = pl.bishopCheck(self,gameState)
                secondTileList = pl.rookCheck(self,gameState)
                for i in range(len(secondTileList)):
                    tileList.append(secondTileList[i])
            try:
                for i in range(len(tileList)):
                    tileList[i].select(self)
            except:
                return
    def testCheck(self,gameState):
        if self.piece == "Rook":
            tileList = pl.rookCheck(self,gameState)
        elif self.piece == "Knight":
            tileList = pl.knightCheck(self,gameState)
        elif self.piece == "Pawn":
            tileList = pl.pawnCheck(self,gameState)
        elif self.piece == "Bishop":
            tileList = pl.bishopCheck(self,gameState)  
        elif self.piece == "King":
            tileList = pl.kingCheck(self,gameState)
        elif self.piece == "Queen":
            tileList = pl.bishopCheck(self,gameState)
            secondTileList = pl.rookCheck(self,gameState)
            for i in range(len(secondTileList)):
                tileList.append(secondTileList[i])
        try:
            return tileList
        except:
            return
