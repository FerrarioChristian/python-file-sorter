from json import load
from shutil import move
from os import listdir
from watchdog.events import FileSystemEventHandler
from Logger import Logger

class EventHandler(FileSystemEventHandler):
    def __init__(self, observed_folder, destination_folder):
        self.observed_folder = observed_folder
        self.destination_folder = destination_folder
        self.json_dict = load(open('destinations.json'))
        self.logger = Logger()

    def on_modified(self, event):
        for file_name in listdir(self.observed_folder):
            src = self.observed_folder + '/' + file_name
            
            for destination, path in self.json_dict['destinations'].items():
                if file_name.split('.')[1] in self.json_dict[destination]:
                    dest = path + file_name
                    move(src, dest)
                    self.logger.log("File " + file_name + " moved in " + destination +" (?)")
                    break