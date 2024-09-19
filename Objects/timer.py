import threading
import tkinter as tk
from time import sleep

import Settings.settings as settings


# Timer for how long a player takes to solve puzzle

class TimerWidget(tk.Label):
    # Target Frame is the object the timer will be placed in, Frame position is the position within that frame
    def __init__(self, frame):
        self.clockTime = 0
        super().__init__(frame, text=f'{self.clockTime:04}', font=("DS-Digital", int(settings.Width/20)), fg="#e60000", bg="Black",
                              width=int(settings.Width/70), height=int(settings.Height/300), relief="raised")
        self.clockThread = None
        self.ticking = True
        self.pack()
        self.exitEvent = threading.Event()

    def tic(self):  # For Incrementing Clock
        while self.ticking:
            if self.exitEvent.is_set():
                break
            else:
                self.config(text=f'{self.clockTime:04}')
                sleep(1)
                self.clockTime += 1



    def clockOn(self):  # Creating a thread for the clock

        self.ticking = True
        self.clockThread = threading.Thread(target=self.tic)
        self.exitEvent.clear()
        self.clockThread.start()

    def resetTimer(self):
        self.clockTime = 0
        self.config(text=f'{self.clockTime:04}')


    def freezeTimer(self):
        self.exitEvent.set()


if __name__ == "__main__":

    TimerTest = TimerWidget(settings.Test_Window)
    TimerTest.clockOn()
    settings.Test_Window.mainloop()

    #TimerTest.test()



