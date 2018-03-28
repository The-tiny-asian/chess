from Tile import Tile

whiteCheck = False
blackCheck = False
whiteCheckMate = False
blackCheckMate = False

#Raheem Nimnicht
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
                    grid[x][y].newPiece("Rook",False)
                elif y==7:
                    grid[x][y].newPiece("Rook",True)
            elif (x ==1) or (x ==6) or (x ==1) or (x ==6):
                if y==0:
                    grid[x][y].newPiece("Knight",False)
                elif y==7:
                    grid[x][y].newPiece("Knight",True)
            elif (x ==2) or (x ==5) or (x ==2) or (x ==5):
                if y==0:
                    grid[x][y].newPiece("Bishop",False)
                elif y==7:
                    grid[x][y].newPiece("Bishop",True)
            elif (x ==4 and y==0) or (x ==3 and y==7):
                if y==0:
                    grid[x][y].newPiece("King",False)
                elif y==7:
                    grid[x][y].newPiece("King",True)
            elif (x==3 and y==0) or (x ==4 and y==7):
                if y==0:
                    grid[x][y].newPiece("Queen",False)
                elif y==7:
                    grid[x][y].newPiece("Queen",True)
            if y==1:
                grid[x][y].newPiece("Pawn",False)
            if y==6:
                grid[x][y].newPiece("Pawn",True)
    
    return grid

def gameChecks(gameState):
    global whiteCheck
    global blackCheck
    whiteSuccess = False
    blackSuccess = False
    for i in range(8):
        for j in range(8):
            #Find King piece
            if gameState[i][j].piece == "King":
                if gameState[i][j].isWhite:
                    whiteKing = gameState[i][j]
                else:
                    blackKing = gameState[i][j]
                for i_ in range(8):
                    for j_ in range(8):
                        #Find each non-blank piece of the opposite team
                        if gameState[i][j].isWhite != gameState[i_][j_].isWhite and gameState[i_][j_].piece != " ":
                            #Get a list of each piece that piece can select
                            tileList = gameState[i_][j_].testCheck(gameState)
                            for n in range(len(tileList)):
                                if tileList[n].x == i and tileList[n].y == j:
                                    if gameState[i][j].isWhite:
                                        whiteCheck = True
                                        whiteSuccess = True
                                    else:
                                        blackCheck = True
                                        blackSuccess = True
                                    break
    
    if not whiteSuccess:
        whiteCheck = False
    else:
        checkCheckmate(gameState,whiteKing)
    if not blackSuccess:
        blackCheck = False
    else:
        checkCheckmate(gameState,blackKing)

def checkCheckmate(gameState,king):
    isWhite = king.isWhite
    x = king.x
    y = king.y
    global whiteCheckMate
    global blackCheckMate
    
    nullTile = Tile(-1,-1)
    allyPieces = [nullTile]
    possibleMoves = [nullTile]
    
    for i in range(8):
        for j in range(8):
            if gameState[i][j].isWhite == isWhite:
                tempList = gameState[i][j].testCheck(gameState)
                try:
                    for n in range(len(tempList)):
                        allyPieces.append(gameState[i][j])
                        possibleMoves.append(tempList[n])
                except:
                    print("Hello")
    del allyPieces[0]
    del possibleMoves[0]
    for i in range(len(allyPieces)):
        print(allyPieces[i].x, ",", allyPieces[i].y, "|", possibleMoves[i].x, ",", possibleMoves[i].y)
        #testBoard = gameState
        #testBoard[possibleMoves[i].x][possibleMoves[i].y].newPiece(allyPieces[i].piece,allyPieces[i].isWhite)
        #testBoard[allyPieces[i].x][allyPieces[i].y].newPiece(" ", False)

def interfaceUpdate():
    global blackCheck
    global whiteCheck
    
    if blackCheck:
        fill(0)
        text("BLACK IS \n UNDER CHECK",900,375)
    if whiteCheck:
        fill(255)
        text("WHITE IS \n UNDER CHECK",900,425)
    if blackCheckMate:
        fill(0)
        text("BLACK IS \n UNDER CHECKMATE",900,300)
    if whiteCheckMate:
        fill(255)
        text("WHITE IS \n UNDER CHECKMATE",900,500)
