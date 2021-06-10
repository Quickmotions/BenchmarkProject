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
    from main import mainProgram
    root = tkinter.Tk()
    frame = tkinter.Frame(root, bg='lightblue')
    root.geometry("450x200")
    frame.pack(fill='both', expand=True)
    global labelText
    labelText = Label(root, text="press start", font=("Courier", 14), fg='blue', bg='lightblue')
    
    button = tkinter.Button(frame, 
                    text="QUIT", 
                    fg="blue",
                    command=quit,
                    width=20,
                    height=5,
                    bg='lightblue',
                    font=("Courier", 14))
    
    slogan = tkinter.Button(frame,
                    text="START",
                    command= mainProgram,
                    fg='blue',
                    width=20,
                    height=5,
                    bg='lightblue',
                    font=("Courier", 14))
    
    # if showButton == 1:
    button.pack(side=tkinter.RIGHT)
    slogan.pack(side=tkinter.LEFT)
    labelText.pack(side=tkinter.TOP,fill='both')

    root.mainloop()
   
