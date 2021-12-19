import random
import os
from errorsGui import PathError, ExperimentConfigurationError
import json

# EXPERIMENT SETTINGS ----------------------------------------
numOfMice = 9
miceNames = ['gNex001', 'gNex002','gNex003','gNex004']
svgPath = r'C:\Users\valen\Desktop'
svgDirName = 'miceSettings'
variableTrialTypes = ['FC', 'QC',  'NC']
variableTrialOri = [0, 90, 45]

constantTrialTypes = ['Pavlovian', 'AdLibitum']
constantTrialOri = [0,0]
#-------------------------------------------------------------


#Check user parameters

if os.path.isdir(svgPath):

    p = os.path.join(svgPath, svgDirName)
else:
    raise PathError('specified path is not valid')

if len(variableTrialOri) != len(variableTrialTypes) or len(constantTrialOri) != len(constantTrialTypes):
    raise ExperimentConfigurationError('number of trial types does not match number of correspondent orientations (lists must have consistent dimensions)')
if len(miceNames) > numOfMice:
    numOfMice = len(miceNames)
elif len(miceNames) < numOfMice:
    miceNames.extend([f'mouse{x:03d}' for x in range(len(miceNames)+1, numOfMice+1)])
 

if not os.path.isdir(p):
    os.mkdir(p)



for mouse in miceNames:
    settingDict = {cstK: cstV for cstK, cstV in zip(constantTrialTypes, constantTrialOri)}
    random.shuffle(variableTrialOri)
    settingDict.update({varK: varV for varK, varV in zip(variableTrialTypes, variableTrialOri)})
    print(f'{mouse} = {settingDict}')
    fPath= os.path.join(p, mouse + '.json')
    if os.path.isfile(fPath):
        raise PathError('Overwriting existing files is not allowed')
    else:
        with open(fPath, 'w') as fobj:
            json.dump(settingDict, fobj)

print(f'data saved in folder: {p}')





