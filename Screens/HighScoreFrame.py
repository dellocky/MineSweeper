import tkinter as tk

import Settings.settings as settings
from Logic.Navigation import screenSwitch
from Logic.Utilites import formatTime
from Screens.ResetConfirmationFrame import ResetConfirmationFrame



class HighScoresFrame(tk.Frame):
    def __init__(self, windowGrid=False):

        super().__init__(bg=settings.Background_Color)
        self.windowGrid = windowGrid
        fontSize = int(settings.Width / 18)

        self.easyLabel = tk.Label(self, font=("DS-Digital", fontSize), bg=settings.Background_Color)
        self.easyLabel.grid(row=0, column=0, pady=int(settings.Height / 32))

        self.mediumLabel = tk.Label(self, font=("DS-Digital", fontSize), bg=settings.Background_Color)
        self.mediumLabel.grid(row=1, column=0, pady=int(settings.Height / 32))

        self.hardLabel = tk.Label(self, font=("DS-Digital", fontSize), bg=settings.Background_Color)
        self.hardLabel.grid(row=2, column=0, pady=int(settings.Height / 32))

        self.resetButton = tk.Button(self, text="Reset", font=("DS-Digital", fontSize),
                                    command=self.confirmReset)
        self.resetButton.grid(row=3, column=0, pady=int(settings.Height / 32))

        self.backButton = tk.Button(self, text="Back", font=("DS-Digital", fontSize),
                                    command=self.screenSwitchExtrasMenu)
        self.backButton.grid(row=4, column=0, pady=int(settings.Height/32))

        if windowGrid:
            self.grid(row=self.windowGrid[0], column=self.windowGrid[1], padx=int(settings.Width / 40),
                      pady=int(settings.Width / 40))
    def screenSwitchExtrasMenu(self):
        screenSwitch(self, self.master.layout.extrasMenuFrame)

    def update(self):
        highscores = settings.fileImport("Settings/UserHighScores.txt")
        for key, value in highscores.items():
            if value == -1:
                highscores[key] = "No Score"
            else:
                highscores[key] = formatTime(value)

        self.easyLabel.config(text=f"Easy     --   {highscores["Easy"]}")
        self.mediumLabel.config(text=f"Medium   --   {highscores["Medium"]}")
        self.hardLabel.config(text=f"Hard     --   {highscores["Hard"]}")

    def confirmReset(self):
        self.disable()
        confirmationFrame = ResetConfirmationFrame(self)
        confirmationFrame.grid(row=self.windowGrid[0], column=self.windowGrid[1])

    def reset(self):
        self.enable()
        settings.writeHighScore()
        self.update()

    def disable(self):
        self.resetButton.config(state="disabled")
        self.backButton.config(state="disabled")

    def enable(self):
        self.resetButton.config(state="active")
        self.backButton.config(state="active")
