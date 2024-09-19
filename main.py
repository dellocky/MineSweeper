import tkinter as tk

import Settings.settings as settings
from Layout import Layout


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry(f"{settings.Width}x{settings.Height}"
                             f"+{int((settings.Desktop_Width/2)-(settings.Width/2))}"
                             f"+{int((settings.Desktop_Height/2)-(settings.Height/2))}")
        self.configure(background=settings.Background_Color)
        self.resizable(width=False, height=False)
        self.layout = Layout(self)
        self.iconbitmap("Bomb.ico")
        self.title("Minesweeper")

    def onClosing(self):
   
        self.layout.topFrame.timer.freezeTimer()
        self.quit()


if __name__ == "__main__":

    window = Window()
    window.protocol("WM_DELETE_WINDOW", window.onClosing)
    window.mainloop()







