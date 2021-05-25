from json import load
from shutil import move
from os import listdir
from watchdog.events import FileSystemEventHandler
from Logger import Logger

class EventHandler(FileSystemEventHandler):
    def __init__(self, observed_folder):
        self.observed_folder = observed_folder
        self.json_dict = load(open(r'C:\Users\chrif\Documents\Developing\PythonFileSorter\destinations.json'))
        self.logger = Logger()
        self.found = False

    def on_modified(self, event):
        for file_name in listdir(self.observed_folder):
            self.found = False
            src = self.observed_folder + '/' + file_name
            if  file_name.split('.')[1] not in self.json_dict['Ignore']:
                for destination, path in self.json_dict['destinations'].items():
                    if file_name.split('.')[1] in self.json_dict[destination]:
                        dest = path + file_name
                        move(src, dest)
                        self.found = True
                        self.logger.log("File " + file_name + " moved in " + dest +" (?)")
                        break
                if(self.found == False):
                    dest = self.json_dict['destinations']['Default'] + file_name
                    move(src, dest)
                    self.logger.log("File " + file_name + " moved in " + dest +" (?)")
                    break
