import os

from win32api import GetSystemMetrics


#  Placement Type of True activates chance, False activates raw number
#  SettingsImport extracts information from the usersettings text file if it exists allowing them to save settings
#  If the file does not exist the function will instead write a text file with the information in it
def fileImport(path):
    with open(path) as File:
        Settings ={}
        for line in File:
            if "=" in line:
                Settings_Reader = line.split("=")
                Settings[f"{Settings_Reader[0].strip()}"] = int(Settings_Reader[1].strip())
            elif ":" in line:
                Settings_Reader = line.split(":")
                Settings_Reader[1] = Settings_Reader[1].strip()
                if Settings_Reader[1] == "True":
                    Settings_Reader[1] = True
                else:
                    Settings_Reader[1] = False
                Settings[f"{Settings_Reader[0].strip()}"] = Settings_Reader[1]

        return Settings


def updateFile(path, dictionary):
    with open(path, "w") as File:
        for key, value in dictionary.items():
            if isinstance(value, bool):
                File.write(f"{key} : {value}\n")
            elif isinstance(value, int):
                File.write(f"{key} = {value}\n")


def writeSettings():
    with open("Settings/UserSettings.txt", "w") as User_Settings_File:
        Settings = {
            "Rows" : 10,
            "Columns" : 10,
            "BombChance" : 20,
            "BombNum" : 20,
            "PlacementType" : True
            }

        User_Settings_File.write(f"Rows = {Settings['Rows']}\n"
                                 f"Columns = {Settings['Columns']}\n"
                                 f"BombChance = {Settings['BombChance']}\n"
                                 f"BombNum = {Settings['BombNum']}\n"
                                 f"PlacementType : {Settings["PlacementType"]}")
        return Settings

def writeHighScore():
    with open("Settings/UserHighScores.txt", "w") as User_HighScore_File:
        Settings = {
            "Easy" : -1,
            "Medium" : -1,
            "Hard" : -1,
            }

        User_HighScore_File.write(f"Easy = {Settings['Easy']}\n"
                                 f"Medium = {Settings['Medium']}\n"
                                 f"Hard = {Settings['Hard']}\n")

        return Settings


#  To allow pulling other values from this module from a different directory
User_Settings_File = "Settings/UserSettings.txt"
user_settings_path = os.path.join(os.getcwd(), User_Settings_File)


if not os.path.exists(user_settings_path):
    writeSettings()

User_HighScore_File = "Settings/UserHighScores.txt"
user_highScore_path = os.path.join(os.getcwd(), User_HighScore_File)

if not os.path.exists(user_highScore_path):
    writeHighScore()


#  Test_Window = tk.Tk() For Testing Objects in Isolation
Desktop_Width = GetSystemMetrics(0)
Desktop_Height = GetSystemMetrics(1)
Background_Color = '#918D94'

Width = int(Desktop_Width/4)
Height = int(Desktop_Height/2)
