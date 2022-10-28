import os
import subprocess
import time

ask = input('Are You READY(y/n) : ')
time.sleep(1)
if(ask=='y'):
    print('Pc will die...')
    time.sleep(1)
    while True:
        method = os.system('start calc.exe')
        method1 = os.system('start cmd')
        method2 = os.system('microsoftedge ')
        method3 = subprocess.run('start microsoft.windows.camera:', shell=True)
        print ('method')
        print ('method1')
        print ('method2')
elif(ask=='n'):
    print('Okay, See You Next Time!')
    exit()
else:
    print('Thats Not In Programs Choices')
    exit()
