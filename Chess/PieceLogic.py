import Tile

#Raheem Nimnicht
def rookCheck(tile, gameState):
    isWhite = tile.isWhite
    x = tile.x
    y = tile.y
    nullTile = Tile.Tile(-1,-1)
    tileList = [nullTile]
    
    for tileX in range(7-x):
        rightX = x + tileX + 1
        if gameState[rightX][y].piece == " ":
            tileList.append(gameState[rightX][y])
        elif gameState[rightX][y].isWhite != isWhite:
            tileList.append(gameState[rightX][y])
            break
        else:
            break
    for tileX in range(x):
        leftX = x - tileX - 1
        if gameState[leftX][y].piece == " ":
            tileList.append(gameState[leftX][y])
        elif gameState[leftX][y].isWhite != isWhite:
            tileList.append(gameState[leftX][y])
            break
        else:
            break
    
    for tileY in range(7-y):
        downY = y + tileY + 1
        if gameState[x][downY].piece == " ":
            tileList.append(gameState[x][downY])
        elif gameState[x][downY].isWhite != isWhite:
            tileList.append(gameState[x][downY])
            break
        else:
            break
    if y - 1 >= 0:
        for tileY in range(y):
            upY = y - tileY - 1
            if gameState[x][upY].piece == " ":
                tileList.append(gameState[x][upY])
            elif gameState[x][upY].isWhite != isWhite:
                tileList.append(gameState[x][upY])
                break
            else:
                break
    
    del tileList[0]
    return tileList
            
#Raheem Nimnicht
def knightCheck(tile, gameState):
    
    isWhite = tile.isWhite
    x = tile.x
    y = tile.y
    nullTile = Tile.Tile(-1,-1)
    tileList = [nullTile]
    
    if x+2 < 8 and y + 1 < 8: #Right 2, Down 1
        if gameState[x+2][y+1].isWhite is not isWhite or (gameState[x+2][y+1].piece == " "):
            tileList.append(gameState[x+2][y+1])
    if x+2 < 8 and y - 1 >= 0: #Right 2, Up 1
        if gameState[x+2][y-1].isWhite is not isWhite or (gameState[x+2][y-1].piece == " "):
            tileList.append(gameState[x+2][y-1])
    if x-2 >= 0 and y + 1 < 8: #Left 2, Down 1
        if gameState[x-2][y+1].isWhite is not isWhite or (gameState[x-2][y+1].piece == " "):
            tileList.append(gameState[x-2][y+1])
    if x-2 >= 0 and y - 1 >= 0: #Left 2, Up 1
        if (gameState[x-2][y-1].isWhite != isWhite) or (gameState[x-2][y-1].piece == " "):
            tileList.append(gameState[x-2][y-1])
    if x+1 < 8 and y + 2 < 8: #Right 1, Down 2
        if gameState[x+1][y+2].isWhite is not isWhite or (gameState[x+1][y+2].piece == " "):
            tileList.append(gameState[x+1][y+2])
    if x+1 < 8 and y - 2 >= 0: #Right 1, Up 2
        if gameState[x+1][y-2].isWhite is not isWhite or (gameState[x+1][y-2].piece == " "):
            tileList.append(gameState[x+1][y-2])
    if x-1 >= 0 and y + 2 < 8: #Left 1, Down 2
        if gameState[x-1][y+2].isWhite is not isWhite or (gameState[x-1][y+2].piece == " "):
            tileList.append(gameState[x-1][y+2])
    if x-1 >= 0 and y - 2 >= 0: #Left 1, Up 2
        if gameState[x-1][y-2].isWhite is not isWhite or (gameState[x-1][y-2].piece == " "):
            tileList.append(gameState[x-1][y-2])
    
    del tileList[0]
    return tileList
            
#David Kang
def pawnCheck(tile, gameState):
    
    isWhite = tile.isWhite
    x = tile.x
    y = tile.y
    nullTile = Tile.Tile(-1,-1)
    tileList = [nullTile]
    
    if isWhite:
        if gameState[x][y-1].piece == " ":
            tileList.append(gameState[x][y-1])
        if x - 1 >= 0 and y - 1 >= 0:
            if gameState[x-1][y-1].piece != " " and gameState[x-1][y-1].isWhite != isWhite:
                tileList.append(gameState[x-1][y-1])
        if x + 1 < 8 and y - 1 >= 0:
            if gameState[x+1][y-1].piece != " " and gameState[x+1][y-1].isWhite != isWhite:
                tileList.append(gameState[x+1][y-1])
    #white
    elif y+1 < 8:
        if gameState[x][y+1].piece == " ":
            tileList.append(gameState[x][y+1])
        if x - 1 >= 0 and y + 1 < 8:
            if gameState[x-1][y+1].piece != " " and gameState[x-1][y+1].isWhite != isWhite:
                tileList.append(gameState[x-1][y+1])
        if x + 1 < 8 and y + 1 < 8:
            if gameState[x+1][y+1].piece != " " and gameState[x+1][y+1].isWhite != isWhite:
                tileList.append(gameState[x+1][y+1])
            
    if y==6 and isWhite:
        if gameState[x][y-2].piece == " " and gameState[x][y-1].piece == " ":
            tileList.append(gameState[x][y-2])
    #Black
    if y==1 and not isWhite:
        if gameState[x][y+2].piece == " " and gameState[x][y+1].piece == " ":
            tileList.append(gameState[x][y+2])
#the code below is to check weather you got a rook to the end of the board, this turns that rook into a king.
#--Bella and Raheem
    if y==7 and not isWhite:
        tile.newPiece("Queen",isWhite)
    if y==0 and isWhite:
        tile.newPiece("Queen",isWhite)
        
    del tileList[0]
    return tileList
        
def kingCheck(tile, gameState):#Bella
    isWhite = tile.isWhite
    x = tile.x
    y = tile.y
    nullTile = Tile.Tile(-1,-1)
    tileList = [nullTile]
    
    if isWhite:
        if not gameState[y][x].x  < 1:#outofbounds exeption up
            if gameState[x][y-1].piece == " " or not gameState[x][y-1].isWhite:
                tileList.append(gameState[x][y-1])
        if not gameState[y][x].x  > 6:#outofbounds exeption down
        
            if gameState[x][y+1].piece == " " or not gameState[x][y+1].isWhite:
        
                tileList.append(gameState[x][y+1])
        if not gameState[y][x].y > 6:#outofbounds exeption right
            if gameState[x+1][y].piece == " " or not gameState[x+1][y].isWhite:
                tileList.append(gameState[x+1][y])
            if not gameState[y][x].x  > 6:#outofbounds exeption down
                if gameState[x+1][y+1].piece == " " or not gameState[x+1][y+1].isWhite:
                    tileList.append(gameState[x+1][y+1])
            if not gameState[y][x].x  < 1:#outofbounds exeption up
                if gameState[x+1][y-1].piece == " " or not gameState[x+1][y-1].isWhite:
                    tileList.append(gameState[x+1][y-1])
        if  not gameState[y][x].y < 1:#this line of code is making sure that their is not an outofbounds exeption for going left on the board.
            if gameState[x-1][y].piece == " " or not gameState[x-1][y].isWhite:
                tileList.append(gameState[x-1][y])
            if not gameState[y][x].x  > 6:#outofbounds exeption down
                if gameState[x-1][y+1].piece == " " or not gameState[x-1][y+1].isWhite:
                    tileList.append(gameState[x-1][y+1])
            if not gameState[y][x].x  < 1:#outofbounds exeption up
                if gameState[x-1][y-1].piece == " " or not gameState[x-1][y-1].isWhite:
                    tileList.append(gameState[x-1][y-1])
    else:
        if not gameState[y][x].x  < 1:#outofbounds exeption up
            if gameState[x][y-1].piece == " " or gameState[x][y-1].isWhite:
                tileList.append(gameState[x][y-1])
        if not gameState[y][x].x  > 6:#outofbounds exeption down
            if gameState[x][y+1].piece == " " or gameState[x][y+1].isWhite:
                tileList.append(gameState[x][y+1])
            if not gameState[y][x].y > 6:#outofbounds exeption right
                if gameState[x+1][y].piece == " " or gameState[x+1][y].isWhite:
                    tileList.append(gameState[x+1][y])
                if not gameState[y][x].x  > 6:#outofbounds exeption down
                    if gameState[x+1][y+1].piece == " " or gameState[x+1][y+1].isWhite:
                        tileList.append(gameState[x+1][y+1])
                if not gameState[y][x].x  < 1:#outofbounds exeption up
                    if gameState[x+1][y-1].piece == " " or gameState[x+1][y-1].isWhite:
                        tileList.append(gameState[x+1][y-1])
        if  not gameState[y][x].y < 1:#this line of code is making sure that their is not an outofbounds exeption for going left on the board.
            if gameState[x-1][y].piece == " " or gameState[x-1][y].isWhite:
                tileList.append(gameState[x-1][y])
            if not gameState[y][x].x  > 6:#outofbounds exeption down
                if gameState[x-1][y+1].piece == " " or gameState[x-1][y+1].isWhite:
                    tileList.append(gameState[x-1][y+1])
            if not gameState[y][x].x  < 1:#outofbounds exeption up
                if gameState[x-1][y-1].piece == " " or gameState[x-1][y-1].isWhite:
                    tileList.append(gameState[x-1][y-1])
                    
    del tileList[0]
    return tileList
            
def bishopCheck(tile, gameState):#Raheem
    
    isWhite = tile.isWhite
    x = tile.x
    y = tile.y
    nullTile = Tile.Tile(-1,-1)
    tileList = [nullTile]
    
    tilesLeft = x
    tilesUp = y
    tilesRight = 7-x
    tilesDown = 7-y
    
    #Down Right
    if tilesDown < tilesRight:
        maxTiles = tilesDown
    else:
        maxTiles = tilesRight
    for i in range(maxTiles):
        xSpace = x+i+1
        ySpace = y+i+1
        if gameState[xSpace][ySpace].piece == " ":
            tileList.append(gameState[xSpace][ySpace])
        elif gameState[xSpace][ySpace].isWhite is not isWhite:
            tileList.append(gameState[xSpace][ySpace])
            break
        else:
            break
    
    #Up Left
    if tilesUp < tilesLeft:
        maxTiles = tilesUp
    else:
        maxTiles = tilesLeft
    for i in range(maxTiles):
        xSpace = x-i-1
        ySpace = y-i-1
        if gameState[xSpace][ySpace].piece == " ":
            tileList.append(gameState[xSpace][ySpace])
        elif gameState[xSpace][ySpace].isWhite is not isWhite:
            tileList.append(gameState[xSpace][ySpace])
            break
        else:
            break
    #Down Left
    if tilesDown < tilesLeft:
        maxTiles = tilesDown
    else:
        maxTiles = tilesLeft
    for i in range(maxTiles):
        xSpace = x-i-1
        ySpace = y+i+1
        if gameState[xSpace][ySpace].piece == " ":
            tileList.append(gameState[xSpace][ySpace])
        elif gameState[xSpace][ySpace].isWhite is not isWhite:
            tileList.append(gameState[xSpace][ySpace])
            break
        else:
            break
    #Up Right
    if tilesUp < tilesRight:
        maxTiles = tilesUp
    else:
        maxTiles = tilesRight
    for i in range(maxTiles):
        xSpace = x+i+1
        ySpace = y-i-1
        if gameState[xSpace][ySpace].piece == " ":
            tileList.append(gameState[xSpace][ySpace])
        elif gameState[xSpace][ySpace].isWhite is not isWhite:
            tileList.append(gameState[xSpace][ySpace])
            break
        else:
            break
        
    del tileList[0]
    return tileList
