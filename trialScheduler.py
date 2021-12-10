import numpy as np
import random
class TrialScheduler():
    '''TrialManager() is a class computing the different tipes of trials that can be used in an operant conditioning paradigm
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
        - numOfReminderPavlovian    default: numOfReminderPavlovian = 4
                                        indicates the number of pavlovian trials preceding the experimental session
        - percentPavlovian          default: percentPavlovian = 0.10 
                                        indicates the percentage of pavlovian trials intermingled in the experimental session
                                        (trial types indicated in the trialTypesRatio dictionary)
    ATTRIBUTES
        trialList                    list of the pseudorandomized trial codes
        trialDict                    dictionary indicating each type of trial and the number of occurrences in trialList
    METHODS
        reshuffle                    shuffle trial codes in trialList.
        '''
    # constructor function
    def __init__(self,numOfTrials =3,
                        trialTypesRatio = 
                        {"FC": 1,
                        "QC": 1, 
                        "NC" : 0,
                        "Pavlovian" : 0,
                        "AdLibitum" : 0},
                        numOfReminderPavlovian = 0,
                        percentPavlovian = 0.10
                        ):
        #ATTRIBUTES
        #initialized
        self.trialList = []
        self.trialDict = {}

        #computes the sequence of trials representing the 'body of the experiment'
        sumTrialWeights = sum(trialTypesRatio.values())
        n_trials = round(numOfTrials*(1-percentPavlovian))
        for trial in trialTypesRatio:
            trialWeight = trialTypesRatio[trial]/sumTrialWeights
            numTrial = round(n_trials*trialWeight)
            self.trialList.extend([trial]*numTrial)
            self.trialDict[trial] = numTrial

        # adds pavlovian trials intermingled in the main part of the session
        self.trialDict["Pavlovian"] = numOfTrials- n_trials
        self.trialList.extend(["Pavlovian"]*self.trialDict["Pavlovian"])
        random.shuffle(self.trialList)

        #add reminders presented at the beginning
        for n in range(numOfReminderPavlovian):
            self.trialList.insert(0,'Pavlovian')
        self.trialDict["Reminders"] = numOfReminderPavlovian
        
    #-------------------------------------------------------------
    #METHODS        
    def reshuffle(self):
        # list = self.trialList
        ind = self.trialDict["Reminders"]
        random.shuffle(self.trialList[ind:])
        return self       
        
        

if __name__ == '__main__':
    a = TrialScheduler(trialTypesRatio={'a':1, 'b':2})
    # b = ["FC" for i in range(5)]
    # b = ["FC"] * 5
    # print(type(a.trialDict['Reminders']))
    print(a.reshuffle().trialList)
    
