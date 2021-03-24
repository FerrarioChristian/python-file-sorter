from event_handler import EventHandler
from watchdog.events import FileSystemEventHandler
import time
from watchdog.observers import Observer

handler = EventHandler()

observer = Observer()
observer.schedule(handler, 'C:/Users/chrif/Downloads', recursive=False)
observer.start()

try:
    while True:
        time.sleep(60)
except KeyboardInterrupt:
    print('Interrupted')
    observer.stop()


observer.join()