# trialTypesRatio ={"FC": 1, "QC": 1, "NC" : 0, "Pavlovian" : 0,"AdLibitum" : 0}
# trialTypesOri = {'Pavlovian':-20, 'FC': 0, 'QC':90, 'NC':45}

# a = sum(trialTypesRatio.values())
# print(a)
import os

f = r'C:\Users\valen\Desktop'
p =  os.path.join(f, 'nnn', 'ccc.docx')
e = os.path.join(f, 'newfile.txt')
print(os.path.dirname(e))
if   os.path.exists(os.path.dirname(e)):
    try:
        with open(p, 'a') as fobj:
            for i in fobj:
                print(i)
    except PermissionError :
        print('O')
else:
    print('merda')