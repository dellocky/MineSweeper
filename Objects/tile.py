import tkinter as tk
import CSV
import Settings.settings as settings
from Logic.Navigation import getNeighborTiles


class tile(tk.Label):
    def __init__(self, frame, row, column):
        super().__init__(master=frame, width=2,
                         relief="raised", borderwidth=2,
                         bg="#F1EEEC")

        self.numImageList = CSV.import_folder(r"Assets/Numbers", (int(settings.Width/24), int(settings.Height / 25)))
        self.miscImageList = CSV.import_folder(r"Assets/Misc", (int(settings.Width/24), int(settings.Height / 25)))

        self.row = row
        self.column = column
        self.isBomb = False
        self.isFlagged = False
        self.isPushed = False
        self.neighborBombs = 0
        self.bombCounter = self.master.master.layout.topFrame.bombCounter


        self.bind("<Button-2>", self.flag)
        self.bind("<Button-3>", self.flag)



    def pushDown(self):
            self.isPushed = True
            self.config(relief='sunken', bg="#CCC9C7")
            if self.neighborBombs != 0 and not self.isBomb:
                self.config(image=self.numImageList[self.neighborBombs-1], width=int(settings.Width/24))
            if self.isBomb:
                self.config(bg="red")
                self.master.gameOver()

    def revealBomb(self):
        if self.isBomb:
            if self.isFlagged:
                self.config(image=self.miscImageList[2], width=int(settings.Width / 24))
            else:
                self.config(image=self.miscImageList[0], width=int(settings.Width/24))


    def cascadePushDown(self, event, dictionary):
        if self.isPushed is False and self.isFlagged is False:
            self.pushDown()
            if self.neighborBombs == 0:
                currentNeighbors = getNeighborTiles(dictionary,(self.row, self.column))
                for tile in currentNeighbors:
                    if tile.neighborBombs == 0 and tile.isPushed is False:
                        tile.cascadePushDown(event, dictionary)
                    else:
                        tile.pushDown()


    def cascadePushDownInit(self, dictionary):
        self.bind("<Button-1>", lambda event, dummy=dictionary: self.cascadePushDown(event, dictionary))

    def flag(self, event):
        if self.isPushed is False:
            if self.isFlagged is False and self.bombCounter.bombCount != 0:
                self.isFlagged = True
                self.config(image=self.miscImageList[1], width=int(settings.Width/24))
                self.bombCounter.countDown()

            elif self.isFlagged is True:
                self.isFlagged = False
                self.config(image="", width=2)
                self.bombCounter.countUp()

    def disable(self):
        self.unbind("<Button-1>")
        self.unbind("<Button-2>")
        self.unbind("<Button-3>")






