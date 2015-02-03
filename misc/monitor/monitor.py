#!/usr/bin/env python

import os
import pyinotify

wm = pyinotify.WatchManager()
mask = pyinotify.IN_CREATE

class CVProcessing(pyinotify.ProcessEvent):
        def process_IN_CREATE(self, event):
                execfile("/home/pi/process.py")

notifier = pyinotify.Notifier(wm, CVProcessing(), timeout=10)

wm.add_watch('/home/pi/OpenCV/', mask, rec=False)

while True:
        try:
                notifier.process_events()
                if notifier.check_events():
                        notifier.read_events()
        except KeyboardInterrupt:
                notifier.stop()
                break
