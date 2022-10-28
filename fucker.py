import os
import subprocess // Same As Os
import time
import PIL.ImageGrab // Image Screenshoter

ask = input('Are You READY(y/n) : ')
time.sleep(1)
if(ask=='y'):
    print('Pc will die...')
    time.sleep(1)
    while True: //Cycle
        method = os.system('start calc.exe')
        method1 = os.system('start cmd')
        method2 = os.system('microsoftedge ')
        method3 = subprocess.run('start microsoft.windows.camera:', shell=True)
        time = time.sleep(2)
        im = PIL.ImageGrab.grab()
        show = im.show()
        im.dump()
        print ('method')
        print ('method1')
        print ('method2')
        print ('method3')
        print ('time')
        print ('im')
        print ('show')
elif(ask=='n'): 
    print('Okay, See You Next Time!')
    exit()
else: //Invaild Argument
    print('Thats Not In Programs Choices')
    exit()
