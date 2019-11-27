import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


def on_created(event):
    print(f"{event.src_path} has been created")

def on_deleted(event):
    print(f"deleted {event.src_path}")

def on_modified(event):
    print(f"{event.src_path} modified")

def on_moved(event):
   print(f"moved {event.src_path} to {event.dest_path}")


if __name__=="__main__":
   patterns="*"
   ignore_patterns=""
   ignore_directories=False
   case_sensitive=True
   my_event_handler=PatternMatchingEventHandler(patterns,ignore_patterns,ignore_directories,case_sensitive)
   my_event_handler.on_created=on_created
   my_event_handler.on_deleted=on_deleted
   my_event_handler.on_modified=on_modified
   my_event_handler.on_moved=on_moved
   path="."
   go_recursively=True
   my_observer=Observer()
   my_observer.schedule(my_event_handler,path,recursive=go_recursively)
   my_observer.start()
   try:
     while True:
       time.sleep(1)
   except KeyboardInterrupt:
       my_observer.stop()
       my_observer.join()



   

