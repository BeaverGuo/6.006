#Event Queue
from threading import Thread
import time
import sys

class EventQueue():
    def __init__(self):
        self.q = BST()
    
    def put(self, seconds_from_now, word):
        self.q.insert(time.time() + seconds_from_now, word)
    
    def execute(self):
        while not self.q.empty():
            m = self.q.minimum()
            scheduled_time = m.key
            if scheduled_time >= time.time():
                time.sleep(scheduled_time - time.time())
            print(m.payload)
            sys.stdout.flush()
            self.q.delete(m)


events = EventQueue()
events.put(1,"hi")
events.put(2,"hey")
events.put(3, "...")
events.put(5, "are you there?")
events.execute()