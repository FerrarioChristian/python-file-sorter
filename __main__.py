from EventHandler import EventHandler
from watchdog.observers import Observer
from time import sleep
from json import load

with open(r'C:\Program Files\PythonFileSorter\destinations.json') as json_file:
    json_dict = load(json_file)
    
observed_folder = json_dict['config']['Observed']

handler = EventHandler(observed_folder)

observer = Observer()
observer.schedule(handler, observed_folder, recursive=False)
observer.start()

try:
    while True:
        sleep(60)
except KeyboardInterrupt:
    print('Interrupted')
    observer.stop()
observer.join()

