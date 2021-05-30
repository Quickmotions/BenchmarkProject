from tkinter import Label, font
import tkinter
from typing import NewType
if __name__ == '__main__':
    try:
        from getComp import runGetComp
        from singleCPU import runSingleCPU
        from writeCSV import runWriteCSV
        from memoryTest import runMemoryTest
        from multiCPU import spawnMultiProcess
        from tkinter import *
    except:
        print("missing packages")
        exit()


def changeText(new):
    newText.set(new)

def main():
    #create array for all results
    results = []                      
    changeText("starting getComp")
    
    #get all system info and store in a list, concatonate list into results
    systemTag, system, machine, version, release, node,cpuTag, cpuBrand, physCore, allCore,memoryTag, memTotal, memUsed,storageTag, storageDevice = runGetComp()    #collect all system and component imfo
    compList =[systemTag, system, machine, "ver: "+str(version), release, node,cpuTag, "cpu: "+str(cpuBrand), "physical: "+str(physCore), "threads: "+str(allCore),memoryTag, "total: "+str(memTotal), "used: "+str(memUsed),storageTag, storageDevice]            #store all spec
    results += compList

    #add values of each test
    results.append("singleCPU: "+str(runSingleCPU()))      
    results.append("multiCPU: "+str(spawnMultiProcess()))  
    results.append("memory: "+str(runMemoryTest()))   
         
    #store all the reults in the csv     
    runWriteCSV(results)               
#TKINTER UI BELOW

root = tkinter.Tk()
frame = tkinter.Frame(root)
root.geometry("600x500")
frame.pack()
newText = StringVar()
newText.set("press start")
text = Label(root, textvariable=newText)
text.pack()
button = tkinter.Button(frame, 
                text="QUIT", 
                fg="red",
                command=quit,
                width=30,
                height=20)
button.pack(side=tkinter.LEFT,)
slogan = tkinter.Button(frame,
                text="START",
                command= main,
                width=30,
                height=20)
slogan.pack(side=tkinter.LEFT)

root.mainloop()
