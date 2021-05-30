from tkinter import Label, font
if __name__ == '__main__':
    try:
        from getComp import runGetComp
        from singleCPU import runSingleCPU
        from writeCSV import runWriteCSV
        from memoryTest import runMemoryTest
        from multiCPU import spawnMultiProcess
        import tkinter as tk
    except:
        print("missing packages")
        exit()

class UI():
    def __init__(self):
        self.root = tk.Tk()
        self.frame = tk.Frame(self.root)
        self.root.geometry("600x500")
        self.frame.pack()
        self.text = Label(self.root, text="Press start to begin", height=10)
        self.text.pack()
        self.button = tk.Button(self.frame, 
                        text="QUIT", 
                        fg="red",
                        command=quit,
                        width=30,
                        height=20)
        self.button.pack(side=tk.LEFT,)
        self.slogan = tk.Button(self.frame,
                        text="START",
                        command= main,
                        width=30,
                        height=20)
        self.slogan.pack(side=tk.LEFT)

        self.root.mainloop()

    def changeText(self):
        self.text['text'] = "textShown"       



#change ui text
def main():
    #create array for all results
    results = []                        
    UI().changeText()

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
if __name__ == '__main__': 
   app=UI()
