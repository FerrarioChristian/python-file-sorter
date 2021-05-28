from json import load
from shutil import move
from os import listdir
from watchdog.events import FileSystemEventHandler
from datetime import datetime

class EventHandler(FileSystemEventHandler):
    def __init__(self, observed_folder):
        self.observed_folder = observed_folder
        with open(r'C:\Program Files\PythonFileSorter\destinations.json') as json_file:
            self.json_dict = load(json_file)
        self.found = False

    def on_any_event(self, event):
        for file_name in listdir(self.observed_folder):
            self.found = False
            src = self.observed_folder + '/' + file_name
            if  file_name.split('.')[1] not in self.json_dict['config']['Ignored']:
                for destination, path in self.json_dict['destinations'].items():
                    if file_name.split('.')[1] in self.json_dict['extensions'][destination]:
                        dest = path + file_name
                        move(src, dest)
                        self.found = True
                        self.log("File \'" + file_name + "\' moved in \'" + dest +"\'")
                        break
                if(self.found == False):
                    dest = self.json_dict['config']['Default'] + file_name
                    move(src, dest)
                    self.log("File \'" + file_name + "\' moved in \'" + dest +"\'")
                    break

    def log(self, logmessage):
        self.f = open(r"C:\Program Files\PythonFileSorter\log.log", "a") 
        self.f.write("[" + str(datetime.now()) + "]" + " " +  logmessage + "\n")
        self.f.close()