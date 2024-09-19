import tkinter as tk
import Settings.settings as settings
class ResetConfirmationFrame(tk.Frame):
    def __init__(self, highScoreFrame, windowGrid=False):

        super().__init__(relief="raised", bg='grey', highlightbackground="black", highlightthickness=1)
        self.windowGrid = windowGrid
        self.highScoreFrame = highScoreFrame
        fontSize = int(settings.Width / 18)

        self.warningLabel = tk.Label(self, text="Confirm Reset", font=("DS-Digital", fontSize), bg="grey")
        self.warningLabel.grid(row=0, column=0, columnspan=2, padx=int(settings.Height/64), pady=int(settings.Height / 32))

        self.cancelButton = tk.Button(self, text="Cancel",  font=("DS-Digital", fontSize))
        self.cancelButton.grid(row=1, column=0, pady=int(settings.Height / 32))

        self.confirmButton = tk.Button(self, text="Confirm", font=("DS-Digital", fontSize))
        self.confirmButton.grid(row=1, column=1, pady=int(settings.Height / 32))

    def cancel(self):

        self.highScoreFrame.enable()
        self.destroy()

    def confirm(self):

        self.highScoreFrame.reset()
        self.destroy()

