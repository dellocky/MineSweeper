import tkinter as tk

import Settings.settings as settings


#  A counter for the amount of Bombs in play minus flagged tiles
class BombCounterWidget(tk.Label):
    def __init__(self, targetFrame):

        self.bombCount= 0
        super().__init__(targetFrame, text=f'{self.bombCount:04}', font=("DS-Digital", int(settings.Width / 20)),
                         fg="#e60000", bg="Black",
                         width=int(settings.Width / 70), height=int(settings.Height / 300), relief="raised")
        self.pack()

    def initCount(self, num):
        self.bombCount = num
        self.config(text=f'{self.bombCount:04}')
    def countUp(self):
        self.bombCount += 1
        self.config(text=f'{self.bombCount:04}')

    def countDown(self):
        self.bombCount -= 1
        self.config(text=f'{self.bombCount:04}')

    def reset(self):
        self.bombCount = 0
        self.config(text=f'{self.bombCount:04}')


if __name__ == "__main__":

    TimerTest = BombCounterWidget(settings.Window)
    settings.Window.mainloop()

