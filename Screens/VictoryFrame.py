import tkinter as tk

import Settings.settings as settings
from Logic.Navigation import screenSwitch
from Logic.Utilites import formatTime


class VictoryFrame(tk.Frame):
    def __init__(self, playGameFrame, windowGrid=None):
        super().__init__(relief="raised", bg='grey', highlightbackground="black", highlightthickness=1)
        self.windowGrid = windowGrid
        self.playGameFrame = playGameFrame
        fontSize = int(settings.Width / 18)
        time = self.playGameFrame.timerWidget.clockTime
        self.highScore = False

        difficulty = self.playGameFrame.difficulty
        highScoreFile = "Settings/UserHighScores.txt"
        highScores = settings.fileImport(highScoreFile)
        if difficulty != "Custom" and time < highScores[difficulty] or highScores[difficulty] == -1:
            highScores[difficulty] = time
            settings.updateFile( "Settings/UserHighScores.txt", highScores)
            self.highScore = True

        self.victoryLabel = tk.Label(self, text="You Win", font=("DS-Digital", int(fontSize*1.5)), bg='grey')
        self.victoryLabel.grid(row=0, column=0, columnspan=3, pady=int(settings.Height / 64))


        if self.highScore:
            self.newRecordLabel = tk.Label(self, text=f"New {difficulty} Record!",
                                  font=("DS-Digital", int(fontSize * .75)), bg='grey')
            self.newRecordLabel.grid(row=1, column=0, columnspan=3, pady=int(settings.Height / 128))

        self.timeLabel = tk.Label(self, text=f"Time = {formatTime(time)}", font=("DS-Digital", int(fontSize*1.5)), bg='grey')
        self.timeLabel.grid(row=2, column=0, columnspan=3, pady=int(settings.Height / 64))


        self.mainMenuButton = tk.Button(self, text="  Main  \n  Menu  ", font=("DS-Digital", fontSize),
                                        command=self.backToMain)
        self.mainMenuButton.grid(row=3, column=0, pady=int(settings.Height / 32))

        self.returnToBoardButton= tk.Button(self, text="Return\nTo Board", font=("DS-Digital", fontSize),
                                            command=self.returnToBoard)
        self.returnToBoardButton.grid(row=3, column=1)

        self.restartButton = tk.Button(self, text="Restart", font=("DS-Digital", fontSize), height=2,
                                       command=self.restart)
        self.restartButton.grid(row=3, column=2)

    def backToMain(self):
        self.playGameFrame.faceWidget.windowState = "Menu"
        self.playGameFrame.faceWidget.config(image=self.playGameFrame.faceWidget.imageList[0])
        self.playGameFrame.destroy()
        screenSwitch(self, self.master.layout.mainMenuFrame)
        self.playGameFrame.timerWidget.killTimer()
        self.playGameFrame.bombCounterWidget.reset()
        self.destroy()

    def returnToBoard(self):
        self.grid_forget()

    def restart(self):
        self.playGameFrame.restart()

