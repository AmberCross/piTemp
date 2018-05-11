from tkinter import*
from time import sleep

def getCpu():
    # pull cpu temperature from file converts it and save as cpuTemp
    f = open("/sys/class/thermal/thermal_zone0/temp")
    global cpuTemp
    cpuTemp = f.read()
    f.close
    cpuTemp = str(int(cpuTemp) / 1000)
    sleep(1)

def cpuLoop():
    getCpu()
    labelCpu.set(cpuTemp[:5])
    root.after(1000, cpuLoop)
    
root = Tk()

getCpu()

labelCpu = StringVar()
labelCpu.set(cpuTemp[:5])

topFrame = Frame(root)
topFrame.grid(row=0)
bottomFrame = Frame(root)
bottomFrame.grid(row=1)

cpuString = Label(topFrame, text="CPU temperature:")
cpuString.grid(row=0)
#cpuOut is label for cpu temp veriable
cpuOut = Label(topFrame, textvariable=labelCpu)
cpuOut.grid(row=0, column=1)

gpuString = Label(bottomFrame, text="GPU temperature:")
gpuString.grid(row=0)
#gpuOut is label for gpu temp veriable
gpuOut = Label(bottomFrame, textvariable=labelCpu)
gpuOut.grid(row=0, column=1)

cpuLoop()

root.mainloop()


