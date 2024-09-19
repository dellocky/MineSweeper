import tkinter as tk

import Settings.settings as settings
from Logic.Navigation import screenSwitch


class GameOverFrame(tk.Frame):
    def __init__(self, playGameFrame, windowGrid=None):
        super().__init__(relief="raised", bg='grey', highlightbackground="black", highlightthickness=1)
        self.windowGrid = windowGrid
        self.playGameFrame = playGameFrame
        fontSize = int(settings.Width / 18)

        self.gameOverLabel = tk.Label(self, text="Gameover", font=("DS-Digital", int(fontSize*1.5)), bg='grey')
        self.gameOverLabel.grid(row=0, column=0, columnspan=3, pady=int(settings.Height / 32))

        self.mainMenuButton = tk.Button(self, text="  Main  \n  Menu  ", font=("DS-Digital", fontSize), command=self.backToMain)
        self.mainMenuButton.grid(row=1, column=0, pady=int(settings.Height / 32))

        self.returnToBoardButton= tk.Button(self, text="Return\nTo Board", font=("DS-Digital", fontSize), command=self.returnToBoard)
        self.returnToBoardButton.grid(row=1, column=1)

        self.restartButton = tk.Button(self, text="Restart", font=("DS-Digital", fontSize), height=2, command=self.restart)
        self.restartButton.grid(row=1, column=2)

    def backToMain(self):
        self.playGameFrame.faceWidget.windowState = "Menu"
        self.playGameFrame.faceWidget.config(image=self.playGameFrame.faceWidget.imageList[0])
        self.playGameFrame.destroy()
        screenSwitch(self, self.master.layout.mainMenuFrame)
        self.playGameFrame.timerWidget.freezeTimer()
        self.playGameFrame.bombCounterWidget.reset()
        self.destroy()
        del self

    def returnToBoard(self):
        self.grid_forget()

    def restart(self):
        self.playGameFrame.restart()


