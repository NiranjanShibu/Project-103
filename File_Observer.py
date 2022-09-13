import sys
import time
import random
import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/vishn/Downloads"

dir_tree = { 
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'], 
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'], 
    "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'], 
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg'] }

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self, event):
        print("A file of path - "+event.src_path+" - was created");
    def on_deleted(self, event):
        print("A file of path - "+event.src_path+" - was deleted");
    def on_modified(self, event):
        print("A file of path - "+event.src_path+" - was modified");
    def on_moved(self, event):
        print("A file of path - "+event.src_path+" - was moved or renamed");

event_handler = FileMovementHandler()

observer = Observer()
observer.schedule(event_handler, from_dir, recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("Running")
except KeyboardInterrupt:
    print("Stopped")
    observer.stop()