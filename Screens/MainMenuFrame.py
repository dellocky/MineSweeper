import tkinter as tk

import Settings.settings as settings
from Logic.Navigation import screenSwitch


class MainMenuFrame(tk.Frame):
    def __init__(self, windowGrid=False):
        super().__init__(bg=settings.Background_Color)
        self.windowGrid = windowGrid

        fontSize = int(settings.Width/18)

        self.playButton = tk.Button(self, text="Play", font=("DS-Digital", fontSize))
        self.playButton.grid(row=0, column=0, pady=int(settings.Height/32))

        self.optionsButton = tk.Button(self, text="Options", font=("DS-Digital",  fontSize))
        self.optionsButton.grid(row=1, column=0, pady=int(settings.Height/32))

        self.extrasButton = tk.Button(self, text="Extras", font=("DS-Digital",  fontSize))
        self.extrasButton.grid(row=2, column=0, pady=int(settings.Height/32))

        self.exitButton = tk.Button(self, text="Exit", font=("DS-Digital",  fontSize))
        self.exitButton.grid(row=3, column=0,  pady=int(settings.Height/32))

        if windowGrid:
            self.grid(row=self.windowGrid[0], column=self.windowGrid[1], padx=int(settings.Width/40), pady=int(settings.Width/40))

    def screenSwitchInit(self, target, button):
        button.config(command=lambda: screenSwitch(self, target))

    def exitButtonInit(self, target):
        def exitButtonCommand(target):
            self.master.quit()
            target.freezeTimer()

        self.exitButton.config(command=lambda: exitButtonCommand(target))


if __name__ == "__main__":
    TimerTest = MainMenuFrame(settings.Window, windowGrid=(0, 0))
    settings.Window.mainloop()




