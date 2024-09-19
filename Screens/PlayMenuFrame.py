import tkinter as tk

import Settings.settings as settings
from Logic.Navigation import screenSwitch
from Screens.PlayGameFrame import PlayGameFrame


class PlayMenuFrame(tk.Frame):
    def __init__(self, windowGrid=False):
        super().__init__(background=settings.Background_Color)

        self.windowGrid = windowGrid
        fontSize = int(settings.Width / 18)

        self.easyButton = tk.Button(self, text="Easy", font=("DS-Digital", fontSize), command=self.easyModeStart)
        self.easyButton.grid(row=0, column=0, pady=int(settings.Height/32))

        self.mediumButton = tk.Button(self, text="Medium", font=("DS-Digital",  fontSize), command=self.mediumModeStart)
        self.mediumButton.grid(row=0, column=1, pady=int(settings.Height/32))

        self.hardButton = tk.Button(self, text="Hard", font=("DS-Digital",  fontSize), command=self.hardModeStart)
        self.hardButton.grid(row=1, column=0, pady=int(settings.Height/32))

        self.customButton = tk.Button(self, text="Custom", font=("DS-Digital",  fontSize), command=self.customModeStart)
        self.customButton.grid(row=1, column=1,  pady=int(settings.Height/32))

        self.backButton = tk.Button(self, text="Back", font=("DS-Digital", fontSize))
        self.backButton.grid(row=2, column=0, pady=int(settings.Height / 32), columnspan=2)



    def screenSwitchInit(self, target, button):
        button.config(command=lambda: screenSwitch(self, target))

    def initNormalGame(self, num, difficulty):

        playGameFrame = PlayGameFrame(15, 14, difficulty, num=num)
        screenSwitch(self, playGameFrame)
        self.master.layout.topFrame.faceWidget.initGameFrame(playGameFrame)
        self.master.layout.topFrame.faceWidget.switchToGameState()
        self.master.layout.topFrame.timer.clockOn()


    def easyModeStart(self):
        self.initNormalGame(30, "Easy")

    def mediumModeStart(self):
        self.initNormalGame(40, "Medium")

    def hardModeStart(self):
        self.initNormalGame(50, "Hard")

    def customModeStart(self):
        gameSettings = settings.fileImport("Settings/UserSettings.txt")
        playGameFrame = PlayGameFrame(gameSettings["Rows"], gameSettings["Columns"],
                                      "Custom", gameSettings["BombNum"],
                                      gameSettings["BombChance"], gameSettings["PlacementType"])
        screenSwitch(self, playGameFrame)
        self.master.layout.topFrame.faceWidget.initGameFrame(playGameFrame)
        self.master.layout.topFrame.faceWidget.switchToGameState()
        self.master.layout.topFrame.timer.clockOn()
        self.topFrameSize = self.master.layout.topFrame.size

        self.master.geometry(f"{int(gameSettings["Rows"]*settings.Width/18.5)}x{int(gameSettings["Columns"]*settings.Height/17.5)}"
                             f"+{int((settings.Desktop_Width/2)-(settings.Width/2))}"
                             f"+{int((settings.Desktop_Height/2)-(settings.Height/2))}")




