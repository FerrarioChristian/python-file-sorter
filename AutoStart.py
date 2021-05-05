# only for windows
import getpass
from os import path
USERNAME = getpass.getuser()


def add_to_startup(file_path=""):
    if file_path == "":
        file_path = path.dirname(path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USERNAME
    with open(bat_path + '\\' + "Autostart_PythonFileSorter.bat", "w+") as bat_file:
        bat_file.write(r'python "" %s' % file_path)