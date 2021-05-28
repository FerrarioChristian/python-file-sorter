import json

with open(r'C:\Users\chrif\Documents\Developing\PythonFileSorter\destinations.json') as dict:
    json_dict = json.load(dict)

def addCategory(category, extensions, path):
    json_dict[category] = extensions
    json_dict['destinations'][category] = path

def delCategory(category):
    del json_dict[category] 
    del json_dict['destinations'][category]

def addExtensions(category, extensions):
    for extension in extensions:
        json_dict[category].append(extension)

def removeExtension(category, extensions):
    for extension in extensions:
        json_dict[category].remove(extension)

def modifyPath(category, path):
    del json_dict['destinations'][category]
    json_dict['destinations'][category] = path
    
def saveJSON():
    with open(r'C:\Users\chrif\Documents\Developing\PythonFileSorter\destinationsTest.json', 'w') as f:
        json.dump(json_dict, f, indent=2)

