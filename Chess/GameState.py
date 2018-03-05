from Tile import Tile

def newGame():
    #Create an 8x8 grid of tiles
    #This is a multidimensional array
    #It's basically a grid, with each
    #square holding a tile type
    defaultTile = Tile(0,0)
    grid = [[defaultTile for xSize in range(8)] for ySize in range(8)]
    
    #Assign each item in the grid correct values
    for x in range(8):
        for y in range(8):
            grid[x][y] = Tile(x,y)
            
            #Assign correct tiles their correct pieces and teams
            if (x==0) or (x==7) or (x==0) or (x==7):
                if y==0:
                    grid[x][y].newPiece("Rook",True)
                elif y==7:
                    grid[x][y].newPiece("Rook",False)
            elif (x ==1) or (x ==6) or (x ==1) or (x ==6):
                if y==0:
                    grid[x][y].newPiece("Knight",True)
                elif y==7:
                    grid[x][y].newPiece("Knight",False)
            elif (x ==2) or (x ==5) or (x ==2) or (x ==5):
                if y==0:
                    grid[x][y].newPiece("Bishop",True)
                elif y==7:
                    grid[x][y].newPiece("Bishop",False)
            elif (x ==4 and y==0) or (x ==3 and y==7):
                if y==0:
                    grid[x][y].newPiece("King",True)
                elif y==7:
                    grid[x][y].newPiece("King",False)
            elif (x==3 and y==0) or (x ==4 and y==7):
                if y==0:
                    grid[x][y].newPiece("Queen",True)
                elif y==7:
                    grid[x][y].newPiece("Queen",False)
            if y==1:
                grid[x][y].newPiece("Pawn",True)
            if y==6:
                grid[x][y].newPiece("Pawn",False)
    
    return grid