from psychopy import visual, core, event, monitors
from errorsGui import MonitorError
import numpy as np
import sys

# import sys

# EXPERIMENT SETTINGS
stimTime = 2 #seconds
respTime = 2
interTrial = 1
stimSize = [20,20] #deg
stimSf = 0.04 #cycles per unit
stimTf = 2 #temporal frequency, Hz

# MONITOR SETTINGS
monitorUsed = 'testMonitor'
dist_cm = 20



# apply monitor settings
mon = monitors.Monitor(monitorUsed)
mon.setDistance(dist_cm)
mon.setWidth(30)

#instances of experiment objects
win = visual.Window(units='deg',
            size = [800, 600],
            fullscr=False,
            monitor=mon)

grating = visual.GratingStim(
            win= win, 
            tex = 'sqr',
            units = 'deg',
            ori = 90,
            size = stimSize,
            mask = 'raisedCos',
            maskParams = {'fringeWidth':0.1},
            sf = stimSf
    )

gray = visual.ShapeStim(win= win,
            pos=[0,0],
            units='norm',
            vertices=((1,1),(-1,1),(-1,-1),(1,-1)),
            closeShape= True,
            lineWidth=0,
            fillColor=[0,0,0],
            fillColorSpace='rgb',
            autoDraw = False)


frameRate = win.getActualFrameRate(nIdentical=50, nMaxFrames=500, nWarmUpFrames=50, threshold=1)

if frameRate == None:
    raise MonitorError
    sys.exit()

stimFrames = int(round(stimTime*frameRate))
grayFrames = int(round((respTime + interTrial)*frameRate))

# Make the mouse invisible
# event.Mouse(visible=False)


for fr in range(stimFrames):
    grating.phase += (1/float(frameRate))*stimTf
    # print(grating.phase)
    grating.draw()
    win.flip()

for fr in range(grayFrames):
    gray.draw()
    win.flip()



win.close()

