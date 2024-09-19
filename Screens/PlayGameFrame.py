
import tkinter as tk

import Logic.BoardLogic as BoardLogic
import Settings.settings
from Logic.Navigation import screenSwitch
from Screens.GameOverFrame import GameOverFrame
from Screens.VictoryFrame import VictoryFrame


class PlayGameFrame(tk.Frame):
    def __init__(self, rows, columns, difficulty, num=0, chance=0, placementType=False, windowGrid=None):
        super().__init__()
        self.windowGrid = windowGrid

        self.rows = rows
        self.columns = columns
        self.num = num
        self.chance = chance
        self.placementType = placementType
        self.difficulty = difficulty

        self.gameOverFrame = None
        self.victoryFrame = None

        self.faceWidget = self.master.layout.topFrame.faceWidget
        self.timerWidget = self.master.layout.topFrame.timer
        self.bombCounterWidget = self.master.layout.topFrame.bombCounter

        #  BoardLogic creates the front end board and gives a dictionary object with the key of (row, column)
        self.tileDict, totalBombs = BoardLogic.generateBoard(self, self.rows, self.columns, self.num, self.chance, self.placementType)
        self.bombCounterWidget.initCount(totalBombs)
        BoardLogic.activateBoard(self.tileDict)

        self.master.update()



    def gameOver(self):

        BoardLogic.deactivateBoard(self.tileDict)
        BoardLogic.revealAllBombs(self.tileDict)

        self.timerWidget.freezeTimer()
        self.gameOverFrame = GameOverFrame(self, windowGrid=self.windowGrid)
        self.gameOverFrame.grid(row=self.windowGrid[0], column=self.windowGrid[1])
        self.faceWidget.windowState = "GameOver"
        self.faceWidget.config(image=self.faceWidget.imageList[2])


    def restart(self):

        for tile in self.tileDict.values():
            tile.destroy()
            del tile

        self.master.update()

        self.tileDict, totalBombs = BoardLogic.generateBoard(self, self.rows, self.columns, self.num, self.chance,
                                                             self.placementType)
        BoardLogic.activateBoard(self.tileDict)
        self.bombCounterWidget.initCount(self.num)
        self.timerWidget.resetTimer()
        self.timerWidget.clockOn()

        self.bombCounterWidget.initCount(totalBombs)
        self.faceWidget.switchToGameState()

        if self.gameOverFrame:
            self.gameOverFrame.destroy()
        if self.victoryFrame:
            self.victoryFrame.destroy()



    def winCheck(self):

        win = BoardLogic.victoryCheck(self.tileDict, self.num)
        if win is False:
            self.gameOver()
        else:
            BoardLogic.deactivateBoard(self.tileDict)
            self.timerWidget.freezeTimer()
            self.victoryFrame = VictoryFrame(self, windowGrid=self.windowGrid)
            self.victoryFrame.grid(row=self.windowGrid[0], column=self.windowGrid[1])
            self.faceWidget.windowState = "GameOver"
            self.faceWidget.config(image=self.faceWidget.imageList[1])





