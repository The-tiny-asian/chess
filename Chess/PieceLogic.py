#Raheem Nimnicht
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
            
#Raheem Nimnicht
def knightCheck(piece, gameState):
    
    isWhite = piece.isWhite
    x = piece.x
    y = piece.y
    
    if x+2 < 8 and y + 1 < 8: #Right 2, Down 1
        if gameState[x+2][y+1].isWhite is not isWhite or (gameState[x+2][y+1].piece is " "):
            gameState[x+2][y+1].select(tile)
    if x+2 < 8 and y - 1 >= 0: #Right 2, Up 1
        if gameState[x+2][y-1].isWhite is not isWhite or (gameState[x+2][y-1].piece is " "):
            gameState[x+2][y-1].select(tile)
    if x-2 >= 0 and y + 1 < 8: #Left 2, Down 1
        if gameState[x-2][y+1].isWhite is not isWhite or (gameState[x-2][y+1].piece is " "):
            gameState[x-2][y+1].select(tile)
    if x-2 >= 0 and y - 1 >= 0: #Left 2, Up 1
        if (gameState[x-2][y-1].isWhite != isWhite) or (gameState[x-2][y-1].piece == " "):
            gameState[x-2][y-1].select(tile)
    if x+1 < 8 and y + 2 < 8: #Right 1, Down 2
        if gameState[x+1][y+2].isWhite is not isWhite or (gameState[x+1][y+2].piece is " "):
            gameState[x+1][y+2].select(tile)
    if x+1 < 8 and y - 2 >= 0: #Right 1, Up 2
        if gameState[x+1][y-2].isWhite is not isWhite or (gameState[x+1][y-2].piece is " "):
            gameState[x+1][y-2].select(tile)
    if x-1 >= 0 and y + 2 < 8: #Left 1, Down 2
        if gameState[x-1][y+2].isWhite is not isWhite or (gameState[x-1][y+2].piece is " "):
            gameState[x-1][y+2].select(tile)
    if x-1 >= 0 and y - 2 >= 0: #Left 1, Up 2
        if gameState[x-1][y-2].isWhite is not isWhite or (gameState[x-1][y-2].piece is " "):
            gameState[x-1][y-2].select(tile)
            
#David Kang
def pawnCheck(piece, gameState):
    
    isWhite = piece.isWhite
    x = piece.x
    y = piece.y
    
    if isWhite:
        if gameState[x][y-1].piece == " ":
            gameState[x][y-1].select(piece)
        if x - 1 >= 0 and y - 1 >= 0:
            if gameState[x-1][y-1].piece != " " and gameState[x-1][y-1].isWhite != isWhite:
                gameState[x-1][y-1].select(piece)
        if x + 1 < 8 and y - 1 >= 0:
            if gameState[x+1][y-1].piece != " " and gameState[x+1][y-1].isWhite != isWhite:
                gameState[x+1][y-1].select(piece)
    #white
    elif y+1 < 8:
        if gameState[x][y+1].piece == " ":
            gameState[x][y+1].select(piece)
        if x - 1 >= 0 and y + 1 < 8:
            if gameState[x-1][y+1].piece != " " and gameState[x-1][y+1].isWhite != isWhite:
                gameState[x-1][y+1].select(piece)
        if x + 1 < 8 and y + 1 < 8:
            if gameState[x+1][y+1].piece != " " and gameState[x+1][y+1].isWhite != isWhite:
                gameState[x+1][y+1].select(piece)
            
    if y==6 and isWhite:
        if gameState[x][y-2].piece == " " and gameState[x][y-1].piece == " ":
            gameState[x][y-2].select(piece)
    #Black
    if y==1 and not isWhite:
        if gameState[x][y+2].piece == " " and gameState[x][y+1].piece == " ":
            gameState[x][y+2].select(piece)
def kingCheck(piece, gameState):
    isWhite = piece.isWhite
    x = piece.x
    y = piece.y
# comments in king refer to code below--Bella
    # I want to check for out of bounds
# this if statement is checking what team the piece is on,
# if it is a white team than the piece can move up one, if it is a black team it can move down one
# the if statement that look like this: **if y-1 > 7 and y-1 < 7:** it is to check and make sure things are not out of bounds
# the if statement that looks like this: **gameState[x][y-1].isWhite** is checking if a tile near
# it is the other team, if it is, it gets highlighted
    # while y+1 == 0-7 or y-1 == 0-7 or x+1 == 0-7 or x-1 == 0-7:
    if isWhite:
        if not gameState[y][x].x  < 1:#outofbounds exeption up
            if gameState[x][y-1].piece == " " or not gameState[x][y-1].isWhite:
                gameState[x][y-1].select(piece)
        if not gameState[y][x].x  > 6:#outofbounds exeption down
            if gameState[x][y+1].piece == " " or not gameState[x][y+1].isWhite:
                gameState[x][y+1].select(piece)
            if not gameState[y][x].y > 6:#outofbounds exeption right
                if gameState[x+1][y].piece == " " or not gameState[x+1][y].isWhite:
                    gameState[x+1][y].select(piece)
            if not gameState[y][x].x  > 6:#outofbounds exeption down
                if gameState[x+1][y+1].piece == " " or not gameState[x+1][y+1].isWhite:
                    gameState[x+1][y+1].select(piece)
            if not gameState[y][x].x  < 1:#outofbounds exeption up
                if gameState[x+1][y-1].piece == " " or not gameState[x+1][y-1].isWhite:
                    gameState[x+1][y-1].select(piece)
        if  not gameState[y][x].y < 1:#this line of code is making sure that their is not an outofbounds exeption for going left on the board.
            if gameState[x-1][y].piece == " " or not gameState[x-1][y].isWhite:
                gameState[x-1][y].select(piece)
            if not gameState[y][x].x  > 6:#outofbounds exeption down
                if gameState[x-1][y+1].piece == " " or not gameState[x-1][y+1].isWhite:
                    gameState[x-1][y+1].select(piece)
            if not gameState[y][x].x  < 1:#outofbounds exeption up
                if gameState[x-1][y-1].piece == " " or not gameState[x-1][y-1].isWhite:
                    gameState[x-1][y-1].select(piece)
    else:
        if not gameState[y][x].x  < 1:#outofbounds exeption up
            if gameState[x][y-1].piece == " " or gameState[x][y-1].isWhite:
                gameState[x][y-1].select(piece)
        if not gameState[y][x].x  > 6:#outofbounds exeption down
            if gameState[x][y+1].piece == " " or gameState[x][y+1].isWhite:
                gameState[x][y+1].select(piece)
            if not gameState[y][x].y > 6:#outofbounds exeption right
                if gameState[x+1][y].piece == " " or gameState[x+1][y].isWhite:
                    gameState[x+1][y].select(piece)
            if not gameState[y][x].x  > 6:#outofbounds exeption down
                if gameState[x+1][y+1].piece == " " or gameState[x+1][y+1].isWhite:
                    gameState[x+1][y+1].select(piece)
            if not gameState[y][x].x  < 1:#outofbounds exeption up
                if gameState[x+1][y-1].piece == " " or gameState[x+1][y-1].isWhite:
                    gameState[x+1][y-1].select(piece)
        if  not gameState[y][x].y < 1:#this line of code is making sure that their is not an outofbounds exeption for going left on the board.
            if gameState[x-1][y].piece == " " or gameState[x-1][y].isWhite:
                gameState[x-1][y].select(piece)
            if not gameState[y][x].x  > 6:#outofbounds exeption down
                if gameState[x-1][y+1].piece == " " or gameState[x-1][y+1].isWhite:
                    gameState[x-1][y+1].select(piece)
            if not gameState[y][x].x  < 1:#outofbounds exeption up
                if gameState[x-1][y-1].piece == " " or gameState[x-1][y-1].isWhite:
                    gameState[x-1][y-1].select(piece)
            
