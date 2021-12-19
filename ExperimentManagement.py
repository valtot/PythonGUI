import random
# from threading import Thread
from psychopy import visual, event, monitors
from errorsGui import ExperimentConfigurationError, MonitorError, PathError

class ExperimentManager():
    '''ExperimentManager() is a class computing the different tipes of trials that can be used in an operant conditioning paradigm
    It is possible to pass the following parameters to the constructor function:
        - numOfTrials :             default numOfTrials = 80
                                        indicates the number of total trials in the experimental session
        - trialTypesRatio:          dictionary
                                        indicates the types of trials applied applied and the experiment.
                                        the keys of the dictionary are the strings indicating the trial type, the values indicates the ratio between them.
                                    default: trialTypesRatio = 
                                                {"FC": 1,
                                                "QC": 1, 
                                                "NC" : 0,
                                                "Pavlovian" : 0,
                                                "AdLibitum" : 0}
                                            in which FC and QC trials are equally represented
        - trialTypesOri             dictionary
                                        indicates the orientation associated to each trial. Keys must be subset of trialTypesRatio keys
                                    default: trialTypesOri = {
                                                'Pavlovian':0,
                                                'FC': 0,
                                                'QC':90,
                                                'NC':45},
        - numOfReminderPavlovian    default: numOfReminderPavlovian = 4
                                        indicates the number of pavlovian trials preceding the experimental session
        - percentPavlovian          default: percentPavlovian = 0.10 
                                        indicates the percentage of pavlovian trials intermingled in the experimental session
                                        (trial types indicated in the trialTypesRatio dictionary)
        - numOfTrials
        - numOfReminderPavlovian 
        - percentPavlovian 
        - trialTypesRatio
        - trialTypesOri 
        - stimTime 
        - respTime 
        - interTrial
        - stimSize
        - stimSf
        - stimTf
        - gratingTex
        - monitorUsed
        - dist_cm
        - mon_width_cm 
    ATTRIBUTES
        trialList                    list of the pseudorandomized trial codes
        trialDict                    dictionary indicating each type of trial and the number of occurrences in trialList
        _numOfTrials 
        _numOfReminderPavlovian 
        _percentPavlovian 
        _trialTypesRatio
        _trialTypesOri 
        _stimTime 
        _respTime 
        _interTrial
        _stimSize
        _stimSf
        _stimTf
        _gratingTex
        _monitorUsed
        _dist_cm
        _mon_width_cm 

    
    METHODS
        reshuffle                    shuffle trial codes in trialList.
        begin                        terminate experiment
        terminate                    starts experiment
        '''
    # constructor function
    def __init__(self,numOfTrials =3,
                        trialTypesRatio ={ 
                                "FC": 1,
                                "QC": 1, 
                                "NC" : 0,
                                "Pavlovian" : 0,
                                "AdLibitum" : 0},
                        trialTypesOri = {
                                'Pavlovian':0,
                                'FC': 0,
                                'QC':90,
                                'NC':45,
                                'AdLibitum':0
                                },
                                
                        numOfReminderPavlovian = 0,
                        percentPavlovian = 0.10,
                        #experiment parameters
                        stimTime = 2, #seconds
                        respTime = 2,
                        interTrial = 1,
                        #grating parameters
                        stimSize = [20,20], #deg
                        stimSf = 0.04, #cycles per unit
                        stimTf = 2, #temporal frequency, Hz
                        gratingTex = 'sqr',
                        #monitor parameters
                        monitorUsed = 'testMonitor',
                        dist_cm = 20,
                        mon_width_cm = 30,
        
                        serialCodeDict = {
                            "FC" : {
                                    "beginningOfTrials": "T",
                                    "responseWindow" : "Z" ,
                                    "trialType" : "conditional"},
                            "QC" : {
                                    "beginningOfTrials": "T",
                                    "responseWindow" : "X" ,
                                    "trialType" : "conditional"},
                            "NC" : {
                                    "beginningOfTrials": "T",
                                    "responseWindow" : "C" ,
                                    "trialType" : "conditional"},
                            "Pavlovian" : {
                                    "beginningOfTrials": "P",
                                    "responseWindow" : None,
                                    "trialType" : "pavlovian"},
                            "AdLibitum" : {
                                    "beginningOfTrials": "A",
                                    "responseWindow" : None ,
                                    "trialType" : "adLibitum"}
                                    },
                        esp = None
                        ):
        #ATTRIBUTES
        #initialized
        self.trialList = []
        self.trialDict = {}
        self._numOfTrials = numOfTrials
        self._numOfReminderPavlovian = numOfReminderPavlovian
        self._percentPavlovian = percentPavlovian
        self._trialTypesRatio = trialTypesRatio
        self._trialTypesOri = trialTypesOri

        self._stimTime = stimTime
        self._respTime = respTime
        self._interTrial = interTrial
        self._stimSize = stimSize
        self._stimSf = stimSf
        self._stimTf = stimTf
        self._gratingTex = gratingTex
        self._monitorUsed = monitorUsed
        self._dist_cm = dist_cm
        self._mon_width_cm = mon_width_cm

        self._esp = esp
        self._serialCodeDict = serialCodeDict


        # check for uncorrect arguments passed to the constructor

        # if set(trialTypesOri.keys()).issubset(set(trialTypesRatio.keys()))== False:
        #     raise ExperimentConfigurationError("Dictionary indicating orientation does not match the one indicating trial types")
        # if numOfReminderPavlovian > numOfTrials:
        #     raise ExperimentConfigurationError("Number of reminders exceed the number of trials")
        if percentPavlovian > 1:
            raise ExperimentConfigurationError("Percentage of pavlovian trials must be [0,1]")

        
        #computes the sequence of trials representing the 'body of the experiment'
        sumTrialWeights = sum(self._trialTypesRatio.values())
        n_trials = round(self._numOfTrials*(1-self._percentPavlovian))

        # for trial in self._trialTypesRatio:
        #     trialWeight = self._trialTypesRatio[trial]/sumTrialWeights
        #     numTrial = round(n_trials*trialWeight)
        #     self.trialList.extend([trial]*numTrial)
        #     self.trialDict[trial] = numTrial

        for trial in self._trialTypesRatio:
            trialWeight = {trial : self._trialTypesRatio[trial]/sumTrialWeights}
        for trial in range(n_trials):
            self.trialList = random.choices(list(self._trialTypesRatio.keys()), list(self._trialTypesRatio.values()), k =n_trials)
            self.trialDict = {x:self.trialList.count(x) for x in self.trialList}

        # adds pavlovian trials intermingled in the main part of the session
        self.trialDict["Pavlovian"] = self._numOfTrials - n_trials
        self.trialList.extend(["Pavlovian"]*self.trialDict["Pavlovian"])
        # random.shuffle(self.trialList)

        #add reminders presented at the beginning
        for n in range(self._numOfReminderPavlovian): 
            self.trialList.insert(0,'Pavlovian')
        self.trialDict["Reminders"] = self._numOfReminderPavlovian

    #-------------------------------------------------------------
    #METHODS 
    def reshuffle(self):
        # list = self.trialList
        ind = self.trialDict["Reminders"]
        random.shuffle(self.trialList[ind:])
        return self       
        
    def begin(self):
        #prevent projection of visual stimulus for ad libitum delivery of Ensure
        #initializes trial object which will be updated by iterating through the list of trials
        
        self.singleTrial = TrialStimulus(
                        stimTime = self._stimTime, #seconds
                        respTime = self._respTime,
                        interTrial = self._interTrial,
                        #grating parameters
                        stimSize = self._stimSize, #deg
                        stimSf = self._stimSf, #cycles per unit
                        stimTf = self._stimTf, #temporal frequency, Hz
                        #____________________
                        # CRUCIAL for the experiment
                        stimOri = self._trialTypesOri[self.trialList[0]], 
                        #____________________
                        gratingTex = self._gratingTex,
                        #monitor parameters
                        monitorUsed = self._monitorUsed,
                        dist_cm = self._dist_cm,
                        mon_width_cm = self._mon_width_cm,

                        esp = self._esp,
                        serialTrialCodes = None

                    )
        for trial in self.trialList:
            if self._esp != None:
                self.singleTrial._serialTrialCodes = self._serialCodeDict[trial]
                
            if trial == "AdLibitum":
                self.singleTrial.display_gray()
            else:
                self.singleTrial.change(ori=self._trialTypesOri[trial])
                self.singleTrial.display()

        self.singleTrial.closeWin()
    def terminate(self):
        return self.singleTrial.closeWin()
                
    # def run(self):
    #     try:
    #         t1 = Thread(target=self.begin(), args=())
    #         t2 = Thread(target=self._esp.print(), args=())
    #     except PathError:
    #         print("Invalid path provided as output of esp class")
    #     # reads, should be implemented saving file indication
    #     # with open('somefile.txt', 'a') as the_file:
    #     #    the_file.write('Hello\n')

    #     t1.start()
    #     t2.start()
    #     t1.join()
    #     t2.join()
        
        

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
                mon_width_cm = 30,

                serialTrialCodes = {
                    "beginningOfTrials": "T",
                    "responseWindow": "Z",
                    "trialType": "conditional"  
                },
                esp = None
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
                    size = [400, 400],
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
        self._frameRate = self.win.getActualFrameRate(nIdentical=50, nMaxFrames=500, nWarmUpFrames=50, threshold=1)

        if self._frameRate == None:
            raise MonitorError(monitorUsed)
        
        # pre-compute number of frames for graphical display
        self._stimFrames = int(round(stimTime*self._frameRate))
        self._respFrames = int(round(respTime *self._frameRate))
        self._interTrialFrames = int(round(interTrial* self._frameRate))
        
        self._esp = esp
        self._serialTrialCodes = serialTrialCodes
        
    # something went wrong here: stimulus continously updating the window
    def change(self, tex = None,
                     ori = None,
                     sf = None
                    ):
        if tex == None:
            tex = self._gratingTex
        if ori == None:
            ori = self._stimOri
        if sf == None:
            sf = self._stimSf


        self.grating.sf = sf
        self.grating.ori = ori
        self.grating.tex = tex

        
    def display(self):
        # Make the mouse invisible
        event.Mouse(visible=False)

        if self._esp != None:
            self._esp.write(self._serialTrialCodes["beginningOfTrials"])
            

        for fr in range(self._stimFrames):
            self.grating.phase += (1/float(self._frameRate))*self._stimTf
            self.grating.draw()
            self.win.flip()

        for fr in range(self._respFrames):
            if self._esp != None:
                self._esp.write(self._serialTrialCodes["responseWindow"])
                
            self.gray.draw()
            self.win.flip()
        for fr in range(self._interTrialFrames):
            if self._esp != None:
                self._esp.write("I")
            self.gray.draw()
            self.win.flip()
    def display_gray(self):
        for fr in range(self._stimFrames + self._respFrames + self._interTrialFrames):
            self.gray.draw()
            self.win.flip()

    def closeWin(self):
        self.win.close()




if __name__ == '__main__':
    try:
        a = ExperimentManager(
        
            numOfTrials = 4,
            respTime=1,
            interTrial=1,
            trialTypesRatio={'FC' :1, "AdLibitum":0},
            percentPavlovian=0,
            mon_width_cm= 61,
            esp=None
        )
        a.begin()
    except ExperimentConfigurationError:
        print('error')

