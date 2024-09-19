import Settings.settings as settings


def screenSwitch(origin, target):
    origin.grid_forget()
    target.grid(row=origin.windowGrid[0], column=origin.windowGrid[1], padx=int(settings.Width / 40),
                          pady=int(settings.Width / 40))
    target.windowGrid = origin.windowGrid

#  To find neighboring tiles relative to a key
def getNeighborTiles(dictionary, key):
    neighbors = []
    potentialNeighbors = [(-1, -1), (0, -1), (1, -1),
                          (-1, 0), (1, 0),
                          (-1, 1), (0, 1), (1, 1)]

    for n in potentialNeighbors:
        try:
            nX, nY = n  # unpacking tuples
            keyX, keyY = key
            currentKey = (nX+keyX, nY+keyY)
            neighbors.append(dictionary[currentKey])
        except KeyError:
            continue

    return neighbors