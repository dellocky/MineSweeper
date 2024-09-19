from Screens.TopFrame import TopFrame
from Screens.MainMenuFrame import MainMenuFrame
from Screens.OptionsMenuFrame import OptionsMenuFrame
from Screens.PlayMenuFrame import PlayMenuFrame
from Screens.CustomSetupFrame import CustomSetupFrame
from Screens.ExtrasMenuFrame import ExtrasMenuFrame
from Screens.HighScoreFrame import HighScoresFrame

#  Layout in charge of putting all objects together on the window
class Layout():

    def __init__(self, window):

        self.topFrame = TopFrame(windowGrid=(0, 0))
        self.mainMenuFrame = MainMenuFrame(windowGrid=(1, 0))

        self.optionsMenuFrame = OptionsMenuFrame()
        self.customSetupFrame = CustomSetupFrame()

        self.extrasMenuFrame = ExtrasMenuFrame()
        self.highScoresFrame = HighScoresFrame()

        self.playMenuFrame = PlayMenuFrame()

        #  Initializing Button Commands with the passed in objects
        self.mainMenuFrame.screenSwitchInit(self.optionsMenuFrame, self.mainMenuFrame.optionsButton)
        self.mainMenuFrame.screenSwitchInit(self.playMenuFrame, self.mainMenuFrame.playButton)
        self.mainMenuFrame.screenSwitchInit(self.extrasMenuFrame, self.mainMenuFrame.extrasButton)
        self.mainMenuFrame.exitButtonInit(self.topFrame.timer)

        self.playMenuFrame.screenSwitchInit(self.mainMenuFrame, self.playMenuFrame.backButton)

        self.optionsMenuFrame.screenSwitchInit(self.mainMenuFrame, self.optionsMenuFrame.backButton)
        self.optionsMenuFrame.screenSwitchInit(self.customSetupFrame, self.optionsMenuFrame.customSetupButton)

        self.customSetupFrame.cancelInit(self.optionsMenuFrame, self.customSetupFrame.cancelButton)
        self.customSetupFrame.continueInit(self.optionsMenuFrame, self.customSetupFrame.confirmButton)


