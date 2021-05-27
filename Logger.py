from AutoStart import USERNAME
from os import system
from datetime import datetime
import getpass #X
class Logger:
    def __init__(self):
        USERNAME = getpass.getuser() #X
        system(r"mkdir C:\Users\%s\AppData\Local\PythonFileSorter" % USERNAME) #X

    def log(self, logmessage):
        USERNAME = getpass.getuser()
        f = open(r"C:\Users\%s\AppData\Local\PythonFileSorter\log.log" % USERNAME, "a") #X
        f.write("[" + str(datetime.now()) + "]" + " " +  logmessage)
        f.close()