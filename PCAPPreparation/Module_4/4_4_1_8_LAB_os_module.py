

from cmath import e
import os


def find(path, dir_to_find):
    """Who cares? """
    
    # Change the current working Directory   
    dir_found =''   
    next_dirs = []
    subdirs_and_files = os.scandir(path)  
    for obj in subdirs_and_files:
        print("obj: ", obj.name)
        if obj.is_dir():
            next_path = path + '\\' + obj.name
            print("next_path: ",next_path) 
            next_dirs.append(next_path)
            if obj.name == dir_to_find:
                dir_found = next_path
                break
    return dir_found, next_dirs         
     
    
    
    
       


start_path = "c:/Users/joank/Documents/Python"
find_dir = "Module_2"

path_found, subdirs = find(start_path, find_dir)
while path_found == "":
    for obj in subdirs:
        path_found, subdirs = find(obj, find_dir)
        if path_found != "":
            break
print("Path Found: ",path_found)


