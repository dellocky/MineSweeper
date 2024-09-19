import tkinter as tk

import Settings.settings as settings
from Logic.Navigation import screenSwitch


#  Placement Type of True activates chance, False activates raw number


class CustomSetupFrame(tk.Frame):
    def __init__(self, windowGrid=False):
        super().__init__(bg=settings.Background_Color)
        self.windowGrid = windowGrid
        fontSize = int(settings.Width / 18)

        self.settings = settings.fileImport("Settings/UserSettings.txt")
        if self.settings["PlacementType"]:
            PlacementText = "Bomb Chance"
        else:
            PlacementText = "Bomb Number"
        self.rowLabel = tk.Label(self, text="Rows", font=("DS-Digital", fontSize),
                                 bg=settings.Background_Color)
        self.rowLabel.grid(row=0, column=0)
        self.rowScale = tk.Scale(self, font=("DS-Digital", fontSize), from_=5, to=25,  orient="horizontal",
                                 bg=settings.Background_Color, highlightthickness=0,
                                 relief="sunken", command=self.bombSliderUpdate)
        self.rowScale.set(self.settings["Rows"])
        self.rowScale.grid(row=0, column=1)

        self.columnLabel = tk.Label(self, text="Columns", font=("DS-Digital", fontSize),
                                    bg=settings.Background_Color)
        self.columnLabel.grid(row=1, column=0, pady=int(settings.Height / 24))
        self.columnScale = tk.Scale(self, font=("DS-Digital", fontSize), from_=5, to=25,
                                    orient="horizontal", bg=settings.Background_Color, highlightthickness=0,
                                    relief="sunken", command=self.bombSliderUpdate)
        self.columnScale.set(self.settings["Columns"])
        self.columnScale.grid(row=1, column=1)

        self.bombNumberButton = tk.Button(self, text="Number", font=("DS-Digital", fontSize),
                                          command=self.bombModeToggle)
        self.bombNumberButton.grid(row=2, column=0, pady=int(settings.Height/24))

        self.bombChanceButton = tk.Button(self, text="Chance", font=("DS-Digital", fontSize),
                                          relief="sunken", state="disabled",  command=self.bombModeToggle)
        self.bombChanceButton.grid(row=2, column=1)

        self.bombLabel = tk.Label(self, text=PlacementText, font=("DS-Digital", fontSize), bg=settings.Background_Color)
        self.bombLabel.grid(row=3, column=0, padx=int(settings.Height/48), pady=int(settings.Height/24))
        self.bombScale = tk.Scale(self, font=("DS-Digital", fontSize), from_=15, to=75,  orient="horizontal",
                                  bg=settings.Background_Color, highlightthickness=0, relief="sunken")
        self.bombScale.grid(row=3, column=1)

        self.cancelButton = tk.Button(self, text="Cancel", font=("DS-Digital", fontSize))
        self.cancelButton.grid(row=6, column=0, pady=int(settings.Height/24))
        self.confirmButton = tk.Button(self, text="Confirm", font=("DS-Digital", fontSize))
        self.confirmButton.grid(row=6, column=1)

        if windowGrid:
            self.grid(row=self.windowGrid[0], column=self.windowGrid[1], padx=int(settings.Width / 40),
                      pady=int(settings.Width / 40))


        if self.settings["PlacementType"] is False:
            self.swapActive()


    def bombModeToggle(self):

        if self.settings["PlacementType"]:

            self.settings["BombChance"] = self.bombScale.get()
            self.bombScale.set(self.settings["BombNum"])
            tempRows = self.rowScale.get()
            tempColumns = self.columnScale.get()

            self.settings["PlacementType"] = False
            self.bombChanceButton.config(relief="raised", state="normal")
            self.bombNumberButton.config(relief="sunken", state="disabled")
            self.bombLabel.config(text="Bomb Number")
            self.bombScale.config(from_=1, to=tempRows*tempColumns)

        else:

            self.settings["BombNum"] = self.bombScale.get()
            self.bombScale.set(self.settings["BombChance"])

            self.settings["PlacementType"] = True
            self.bombNumberButton.config(relief="raised", state="normal")
            self.bombChanceButton.config(relief="sunken", state="disabled")
            self.bombLabel.config(text="Bomb Chance")
            self.bombScale.config(from_=15, to=75)

    def swapActive(self):
        self.bombChanceButton.config(relief="raised", state="normal")
        self.bombNumberButton.config(relief="sunken", state="disabled")

    def bombSliderUpdate(self, event):
        if self.settings["PlacementType"] is False:
            tempRows = self.rowScale.get()
            tempColumns = self.columnScale.get()
            bombMax = tempRows*tempColumns
            self.bombScale.config(from_=1, to=bombMax)
            if self.bombScale.get() > bombMax:
                self.bombScale.set(bombMax)

    def cancelInit(self, target, button):
        def screenSwitchCancelCommand(target):
            screenSwitch(self, target)
            values = settings.fileImport("Settings/UserSettings.txt")
            self.rowScale.set(values["Rows"])
            self.columnScale.set(values["Columns"])
            if self.settings["PlacementType"] is False:
                self.bombScale.set(values["BombNum"])
            else:
                self.bombScale.set(values["BombChance"])

        button.config(command=lambda: screenSwitchCancelCommand(target))

    def continueInit(self, target, button):
        def screenSwitchUpdateCommand(target):
            if self.settings["PlacementType"]:
                self.settings["BombChance"] = self.bombScale.get()
            else:
                self.settings["BombNum"] = self.bombScale.get()
            self.settings["Rows"] = self.rowScale.get()
            self.settings["Columns"] = self.columnScale.get()
            screenSwitch(self, target)
            settings.updateFile("Settings/UserSettings.txt", self.settings)
            print(self.settings)

        button.config(command=lambda: screenSwitchUpdateCommand(target))
