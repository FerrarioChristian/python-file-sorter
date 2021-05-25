from EventHandler import EventHandler
from time import sleep
from watchdog.observers import Observer
import AutoStart

AutoStart.add_to_startup()

observed_folder = 'C:/Users/chrif/Downloads/Downloading'

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

