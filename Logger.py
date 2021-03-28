from os import system
from datetime import datetime
class Logger:
    def __init__(self):
        system("mkdir C:\\Users\\chrif\\AppData\\Local\\PythonFileSorter")

    def log(self, logmessage):
        f = open("C:/Users/chrif/AppData/Local/PythonFileSorter/log.log", "a")
        f.write("[" + str(datetime.now()) + "]" + " " +  logmessage)
        f.close()