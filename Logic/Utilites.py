from math import trunc
def formatTime(time):
    seconds = time % 60
    minutes = trunc(time / 60) % 60
    hours = trunc(time / 3600)
    formatedTime = f"{hours:02}:{minutes:02}:{seconds:02}"
    return formatedTime