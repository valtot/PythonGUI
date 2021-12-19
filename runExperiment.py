import time
def thread_func1(fileN:str):

    for i in range(10):
        print(['bc'])
        time.sleep(0.2)
        with open(fileN, 'a') as fobj:
            fobj.write('bc\n')
        
    
if __name__ == '__main__':
    from ExperimentManagement import ExperimentManager
    import json
    from errorsGui import PathError
    from multiprocessing import Process
    import os 

    settingFile = r"C:\Users\valen\Desktop\miceSettings\gNex004.json"
    savingFile = r"C:\Users\valen\Desktop\miceSettings\newFile.txt"

    if not os.path.isfile(settingFile):
        raise PathError()
    


    
    # Opening JSON file
    with open(settingFile) as json_file:
        data = json.load(json_file)
 



    exp = ExperimentManager(
                        numOfTrials =3,
                        trialTypesRatio ={ 
                                "FC": 1,
                                "QC": 1, 
                                "NC" : 0,
                                "Pavlovian" : 0,
                                "AdLibitum" : 0},
                        trialTypesOri = data,
                                
                        numOfReminderPavlovian = 0,
                        percentPavlovian = 0,
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
                        mon_width_cm = 61.224,


                        )




    t1 = Process(target=thread_func1, args=(savingFile,))
    t1.start()
    exp.begin()
    t1.join()
    print(f'{exp.trialDict} and {exp.trialList}')

