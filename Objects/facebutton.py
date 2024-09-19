import tkinter as tk

import CSV
import Settings.settings as settings


#  For the Minesweeper clickable face
class FaceWidget(tk.Button):

    def __init__(self, targetFrame, path, playGameFrame = None):

        self.imageList = CSV.import_folder(path, (int(settings.Height/12), int(settings.Height/12)))
        self.imageNum = 0
        super().__init__(targetFrame, image=self.imageList[self.imageNum], command=self.faceClick)
        self.windowState = "Menu"
        self.playGameFrame = playGameFrame
        self.pack()


    def faceClick(self):

        if self.windowState == "Menu":
            if self.imageNum != 2:
                self.imageNum += 1
                self.config(image=self.imageList[self.imageNum])
            else:
                self.imageNum = 0
                self.config(image=self.imageList[self.imageNum])

        elif self.windowState == "Game":
            self.playGameFrame.winCheck()

        elif self.windowState == "GameOver":
            self.playGameFrame.restart()



    def initGameFrame(self, playGameFrame):

        self.playGameFrame = playGameFrame

    def switchToGameState(self):
        self.windowState = "Game"
        self.config(image=self.imageList[0])

if __name__ == "__main__":

    FaceTest = FaceWidget(settings.Test_Window)
    settings.Test_Window.mainloop()




