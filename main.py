import sounddevice as sd
import numpy as np
import winsound as ws

numTracker = 0  

def print_sound(indata, outdata, frames, time, status):
    global numTracker
    volume_norm = np.linalg.norm(indata)*10
    print ("|"+ "|"* int(volume_norm))
    #volume level
    if int(volume_norm)>=80:
        numTracker += 1
    else:
        numTracker = 0
    #how many times to repeat at expected volume
    if numTracker >= 3:
        frequency = 2000
        duration = 1500
        ws.Beep(frequency, duration)
    
with sd.Stream(callback=print_sound):
    sd.sleep(1000000000)
