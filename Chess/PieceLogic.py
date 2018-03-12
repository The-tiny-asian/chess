def rookCheck(piece, gameState):
    isWhite = piece.isWhite
    x = piece.x
    y = piece.y
    for tileX in range(7-x):
        rightX = x + tileX + 1
        if gameState[rightX][y].piece == " ":
            gameState[rightX][y].select(piece)
        elif gameState[rightX][y].isWhite != isWhite:
            gameState[rightX][y].select(piece)
            break
        else:
            break
    for tileX in range(x):
        leftX = x - tileX - 1
        if gameState[leftX][y].piece == " ":
            gameState[leftX][y].select(piece)
        elif gameState[leftX][y].isWhite != isWhite:
            gameState[leftX][y].select(piece)
            break
        else:
            break
    
    for tileY in range(7-y):
        downY = y + tileY + 1
        if gameState[x][downY].piece == " ":
            gameState[x][downY].select(piece)
        elif gameState[x][downY].isWhite != isWhite:
            gameState[x][downY].select(piece)
            break
        else:
            break
    if y - 1 >= 0:
        for tileY in range(y):
            upY = y - tileY - 1
            if gameState[x][upY].piece == " ":
                gameState[x][upY].select(piece)
            elif gameState[x][upY].isWhite != isWhite:
                gameState[x][upY].select(piece)
                break
            else:
                break
            
def knightCheck(piece, gameState):
    
    isWhite = piece.isWhite
    x = piece.x
    y = piece.y
    
    if x+2 < 8 and y + 1 < 8:
        if gameState[x+2][y+1].isWhite is not isWhite or (gameState[x+2][y+1].piece is " "):
            gameState[x+2][y+1].select(piece)
    if x+2 < 8 and y - 1 >= 0:
        if gameState[x+2][y-1].isWhite is not isWhite or (gameState[x+2][y-1].piece is " "):
            gameState[x+2][y-1].select(piece)
    if x-2 >= 0 and y + 1 < 8:
        if gameState[x-2][y+1].isWhite is not isWhite or (gameState[x-2][y+1].piece is " "):
            gameState[x-2][y+1].select(piece)
    if x-2 >= 0 and y - 1 >= 0:
        if (gameState[x-2][y-1].isWhite != isWhite) or (gameState[x-2][y-1].piece == " "):
            gameState[x-2][y-1].select(piece)
    if x+1 < 8 and y + 2 < 8:
        if gameState[x+1][y+2].isWhite is not isWhite or (gameState[x+1][y+2].piece is " "):
            gameState[x+1][y+2].select(piece)
    if x+1 < 8 and y - 2 >= 0:
        if gameState[x+1][y-2].isWhite is not isWhite or (gameState[x+1][y-2].piece is " "):
            gameState[x+1][y-2].select(piece)
    if x-1 >= 0 and y + 2 < 8:
        if gameState[x-1][y+2].isWhite is not isWhite or (gameState[x-1][y+2].piece is " "):
            gameState[x-1][y+2].select(piece)
    if x-1 >= 0 and y - 2 >= 0:
        if gameState[x-1][y-2].isWhite is not isWhite or (gameState[x-1][y-2].piece is " "):
            gameState[x-1][x-2].select(piece)
            
def pawnCheck(piece, gameState):
    
    isWhite = piece.isWhite
    x = piece.x
    y = piece.y
    
    if not isWhite:
        if gameState[x][y-1].piece == " ":
            gameState[x][y-1].select(piece)
    else:
        if gameState[x][y+1].piece == " ":
            gameState[x][y+1].select(piece)
    if y==6 and not isWhite:
        if gameState[x][y-2].piece == " " and gameState[x][y-1].piece == " ":
            gameState[x][y-2].select(piece)
    if y==1 and isWhite:
        if gameState[x][y+2].piece == " " and gameState[x][y+1].piece == " ":
            gameState[x][y+2].select(piece)
