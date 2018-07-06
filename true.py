#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from watchdog.observers import Observer
from watchdog.events import *
import time
class FileEventHandler(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)
    def on_created(self, event):
        with open('/var/log/img.log','a+') as f:
           # line=event.src_path +"\n"
            f.write(event.src_path+"\n")  
            os.system("fileline=`tail -n 1 /var/log/img.log|awk -F '/' '{print $3}'`")    
            os.system("git add /img/$fileline")
            os.system("git commit -a -m 'add $fileline'")
            os.system("git push origin master")
            os.system("echo https://raw.githubusercontent.com/ananzhoujiaan/img/master/$fileline")             
if __name__ == "__main__":
    observer = Observer()
    event_handler = FileEventHandler()
    observer.schedule(event_handler,"/img",True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()






