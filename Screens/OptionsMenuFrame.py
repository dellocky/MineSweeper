import tkinter as tk

import Settings.settings as settings
from Logic.Navigation import screenSwitch


class OptionsMenuFrame(tk.Frame):
    def __init__(self, windowGrid=False):

        super().__init__(bg=settings.Background_Color)
        self.windowGrid = windowGrid
        fontSize = int(settings.Width / 18)

        self.customSetupButton = tk.Button(self, text="Custom Setup", font=("DS-Digital", fontSize))
        self.customSetupButton.grid(row=0, column=0, pady=int(settings.Height/32))


        self.backButton = tk.Button(self, text="Back", font=("DS-Digital", fontSize))
        self.backButton.grid(row=1, column=0, pady=int(settings.Height/32))

        if windowGrid:
            self.grid(row=self.windowGrid[0], column=self.windowGrid[1], padx=int(settings.Width / 40),
                      pady=int(settings.Width / 40))
    def screenSwitchInit(self, target, button):
        button.config(command=lambda:  screenSwitch(self, target))



