# showButton = 0
def changeTxt(txt):
    global labelText
    labelText.configure(text=txt)
    labelText.update()
# def makeShowButton():
#     global showButton
#     showButton = 1
# def hideButton():
#     global showButton
#     showButton = 0
def createUI():
    from tkinter import Label
    import tkinter
    from main import main
    root = tkinter.Tk()
    frame = tkinter.Frame(root)
    root.geometry("500x200")
    frame.pack()
    global labelText
    labelText = Label(root, text="press start", font=("Courier", 14))
    
    button = tkinter.Button(frame, 
                    text="QUIT", 
                    fg="red",
                    command=quit,
                    width=30,
                    height=5)
    
    slogan = tkinter.Button(frame,
                    text="START",
                    command= main,
                    width=30,
                    height=5)
    
    # if showButton == 1:
    button.pack(side=tkinter.LEFT)
    slogan.pack(side=tkinter.LEFT)
    labelText.pack(side=tkinter.TOP)

    root.mainloop()
   

