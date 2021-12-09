from psychopy import visual, event, monitors
from trialScheduler import TrialScheduler
from errorsGui import MonitorError
import sys

class TestingSession(TrialScheduler):
    def __init__(self,
                trialTypesOri = {
                                'Pavlovian':-20,
                                'FC': 0,
                                'QC':90,
                                'NC':45,
                                },             
                **kwargs):
        super(TestingSession,self).__init__(**kwargs)
        self.trialTypesOri = trialTypesOri

        

    def begin(self):
        for trial in self.trialList:
            singleTrial = TrialStimulus(stimOri=self.trialTypesOri[trial])
            singleTrial.display()
            pass
        singleTrial.closeWin()
    def terminate(self):
        return sys.exit()
        




class TrialStimulus():
    def __init__(self,
                #experiment parameters
                stimTime = 2, #seconds
                respTime = 2,
                interTrial = 1,
                #grating parameters
                stimSize = [20,20], #deg
                stimSf = 0.04, #cycles per unit
                stimTf = 2, #temporal frequency, Hz
                stimOri = 0,
                gratingTex = 'sqr',
                #monitor parameters
                monitorUsed = 'testMonitor',
                dist_cm = 20,
                mon_width_cm = 30
                ):
        
                        
        self._stimSf = stimSf
        self._stimTf = stimTf
        self._stimOri = stimOri
        self._gratingTex = gratingTex
        # apply monitor settings
        self._mon = monitors.Monitor(monitorUsed)
        self._mon.setDistance(dist_cm)
        self._mon.setWidth(mon_width_cm)

        #instances of experiment objects
        self.win = visual.Window(units='deg',
                    size = [800, 600],
                    fullscr=False,
                    monitor=self._mon)

        self.grating = visual.GratingStim(
                    win= self.win, 
                    tex = self._gratingTex,
                    units = 'deg',
                    ori = self._stimOri,
                    size = stimSize,
                    mask = 'raisedCos',
                    maskParams = {'fringeWidth':0.1},
                    sf = self._stimSf
            )

        self.gray = visual.ShapeStim(
                    win= self.win,
                    pos=[0,0],
                    units='norm',
                    vertices=((1,1),(-1,1),(-1,-1),(1,-1)),
                    closeShape= True,
                    lineWidth=0,
                    fillColor=[0,0,0],
                    fillColorSpace='rgb',
                    autoDraw = False)

        # compute framerate
        # self._frameRate = self.win.getActualFrameRate(nIdentical=50, nMaxFrames=500, nWarmUpFrames=50, threshold=1)
        self._frameRate = 60

        if self._frameRate == None:
            raise MonitorError
        

        # pre-compute number of frames for graphical display
        self._stimFrames = int(round(stimTime*self._frameRate))
        print(self._stimFrames)
        self._grayFrames = int(round((respTime + interTrial)*self._frameRate))
        print(self._grayFrames)
        
    # something went wrong here: stimulus continously updating the window
    # def change(self, tex = self._gratingtext,
    #                  ori = self._stimOri,
    #                  sf = self._stimSf
    #                 ):

    #     self.grating.sf = tex

        pass
    def display(self):
        # Make the mouse invisible
        event.Mouse(visible=False)


        for fr in range(self._stimFrames):
            self.grating.phase += (1/float(self._frameRate))*self._stimTf
            # print(grating.phase)
            self.grating.draw()
            self.win.flip()

        for fr in range(self._grayFrames):
            self.gray.draw()
            self.win.flip()
    def closeWin(self):
        self.win.close()

if __name__ == '__main__':
    a = TestingSession()
    a.begin()