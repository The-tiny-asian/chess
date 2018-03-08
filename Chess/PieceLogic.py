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
        if gameState[x+2][y+1].getTeam() is not isWhite or (gameState[x+2][y+1].getPiece() is " "):
            gameState[x+2][y+1].select()
    if x+2 < 8 and y - 1 >= 0:
        if gameState[x+2][y-1].getTeam() is not isWhite or (gameState[x+2][y-1].getPiece() is " "):
            gameState[x+2][y-1].select()
    if x-2 >= 0 and y + 1 < 8:
        if gameState[x-2][y+1].getTeam() is not isWhite or (gameState[x-2][y+1].getPiece() is " "):
            gameState[x-2][y+1].select()
    if x-2 >= 0 and y - 1 >= 0:
        if (gameState[x-2][y-1].getTeam() != isWhite) or (gameState[x-2][y-1].getPiece() == " "):
            gameState[x-2][y-1].select()
    if x+1 < 8 and y + 2 < 8:
        if gameState[x+1][y+2].getTeam() is not isWhite or (gameState[x+1][y+2].getPiece() is " "):
            gameState[x+1][y+2].select()
    if x+1 < 8 and y - 2 >= 0:
        if gameState[x+1][y-2].getTeam() is not isWhite or (gameState[x+1][y-2].getPiece() is " "):
            gameState[x+1][y-2].select()
    if x-1 >= 0 and y + 2 < 8:
        if gameState[x-1][y+2].getTeam() is not isWhite or (gameState[x-1][y+2].getPiece() is " "):
            gameState[x-1][y+2].select()
    if x-1 >= 0 and y - 2 >= 0:
        if gameState[x-1][y-2].getTeam() is not isWhite or (gameState[x-1][y-2].getPiece() is " "):
            gameState[x-1][x-2].select()