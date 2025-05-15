from textnode import *
from htmlnode import *
import os
import shutil


def copy_static(source, target):
    if os.path.exists(target):
        shutil.rmtree(target)
        os.mkdir(target)
    copy_directory(source, target)
            
def copy_directory(source, target):
    if not os.path.exists(target):
        os.mkdir(target)
    
    for item in os.listdir(source):
        source_item = os.path.join(source, item)
        target_item = os.path.join(target, item)
        
        if os.path.isfile(source_item):
            shutil.copy(source_item, target_item)
            print(f"Copied: {source_item} to {target_item}")
        else:
            copy_static(source_item, target_item)


def main():
    copy_static("static", "public")
    
if __name__ == '__main__':
    main()