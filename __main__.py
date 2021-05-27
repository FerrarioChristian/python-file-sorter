from EventHandler import EventHandler
from time import sleep
from watchdog.observers import Observer
from json import load #X
import AutoStart
import getpass #X

AutoStart.add_to_startup()

USERNAME = getpass.getuser() #X

json_dict = load(open(r'C:\Users\%s\Documents\PythonFileSorter\destinations.json' % USERNAME)) #X
observed_folder = json_dict['config']['Observed']

print(observed_folder)

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

