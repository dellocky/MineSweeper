from random import randint

from Logic.Navigation import getNeighborTiles
from Objects.tile import tile


def generateBoard(frame, rows, columns, bombs, chance, placementType):

    currentRow = 0
    currentColumn = 0
    totalTiles = rows * columns
    if placementType is False:
        totalBombs = bombs
    else:
        totalBombs = 0
    remainingTiles = totalTiles
    remainingBombs = bombs
    tileDict={}

    for items in range(totalTiles):
        currentTile = tile(frame, currentRow, currentColumn)
        #  Creating bombs depending on chosen mode
        if placementType is False:
            randomValue = randint(1, remainingTiles)
            remainingTiles -= 1
            if randomValue <= remainingBombs:
                currentTile.isBomb = True
                remainingBombs -= 1



        else:
            randomValue = randint(1, 100)
            if randomValue < chance:
                currentTile.isBomb = True
                totalBombs += 1
        currentTile.grid(row=currentRow, column=currentColumn)


        tileDict[(currentRow, currentColumn)] = currentTile

        currentColumn += 1
        if currentColumn == columns:
            currentRow += 1
            currentColumn = 0

    return tileDict, totalBombs



def activateBoard(dictionary):
    for key, value in dictionary.items():
        value.cascadePushDownInit(dictionary)
        neighborBombCount = 0
        neighborTiles = getNeighborTiles(dictionary, key)
        for Tile in neighborTiles:
            if Tile.isBomb:
                neighborBombCount += 1
        value.neighborBombs = neighborBombCount
def deactivateBoard(dictionary):
    for key, value in dictionary.items():
        value.disable()

def victoryCheck(dictionary, bombNum):
    correctFlagNum = 0
    for key, value in dictionary.items():
        if value.isFlagged and value.isBomb:
            correctFlagNum +=1

    if correctFlagNum == bombNum:
        return True
    else:
        return False

def revealAllBombs(dictionary):
    for key, value in dictionary.items():
        if value.isBomb:
            value.revealBomb()











