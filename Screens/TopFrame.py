import tkinter as tk

import Settings.settings as settings
from Objects.bombcounter import BombCounterWidget
from Objects.facebutton import FaceWidget
from Objects.timer import TimerWidget


#  TopFrame object holds the objects constantly visible at the top of the Screen
class TopFrame(tk.Frame):
    def __init__(self, windowGrid=False):
        super().__init__(relief="sunken", bg='grey', highlightbackground="black", highlightthickness=1)

        self.windowGrid = windowGrid
        self.bombCounterFrame = tk.Frame(self)
        self.bombCounter = BombCounterWidget(self.bombCounterFrame)
        self.bombCounterFrame.grid(row=0, column=0, padx=int(settings.Width/40))

        self.faceFrame = tk.Frame(self)
        self.faceWidget = FaceWidget(self.faceFrame, r"Assets/Faces")
        self.faceFrame.grid(row=0, column=1, padx=int(settings.Width/5))

        self.timerFrame = tk.Frame(self)
        self.timer = TimerWidget(self.timerFrame)
        self.timerFrame.grid(row=0, column=2,  padx=int(settings.Width/40))

        self.master.update()
        self.size = (self.winfo_width(), self.winfo_height())

        if windowGrid:
            self.grid(row=windowGrid[0], column=windowGrid[1], padx=int(settings.Width/40), pady=settings.Height/32)
