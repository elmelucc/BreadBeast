import serial
from tkinter import *
from time import sleep
from PIL import Image, ImageTk

#SERIAL STUFF
def beginVoltage():
    ser = serial.Serial('COM5')
    print(ser.name)

    sread = ser.read(4).decode("utf-8")
    ser.readline()
    s.set(sread)
    root.update_idletasks()

    ser.close()

def learnVoltage():
    beginVoltage()
    sfloat = float(s.get())
    if sfloat > 1.63 and sfloat < 1.67:
        success.set('Correct!')
    else:
        success.set('Not quite... Try Again.')

#TKINTER SETUP
root = Tk()
root.title("BreadBeast")
root.iconbitmap(r'C:\Users\emelu\pypro\emicon.ico')
root.geometry("700x500")

def back():
    Frame.grid_forget()
    s.set('0.00')


def measurePage():
    secondaryFrame.grid_forget()
    back.grid_forget()
    learnLabel.grid_forget()
    circuitLabel.grid_forget()
    learnSeparator.grid_forget()
    learnVoltageButton.grid_forget()
    voltageOutputCheckLabel.grid_forget()
    voltageCheckVLabel.grid_forget()
    voltageSuccessLabel.grid_forget()

    Frame.grid(row=0, column=1, columnspan=7, rowspan=2, sticky='nsew')
    back.grid(row=2, column=5)
    measureVoltageLabel.grid(row=0, column=1, columnspan=5)
    measureVoltageButton.grid(row=1, column=2)
    voltageOutputLabel.grid(row=1, column=3)
    voltageVLabel.grid(row=1, column=4)

def learnPage():
    back.grid_forget()
    measureVoltageLabel.grid_forget()
    measureVoltageButton.grid_forget()
    voltageOutputLabel.grid_forget()
    voltageVLabel.grid_forget()

    Frame.grid(row=0, column=1, columnspan=7, rowspan=2, sticky='nsew')
    secondaryFrame.grid(row=1, column=4)
    back.grid(row=3, column=4)
    learnLabel.grid(row=0, column=1, columnspan=5)
    circuitLabel.grid(row=1, column=2)
    learnSeparator.grid(row=1, column=3)
    learnVoltageButton.grid(row=0, column=0, columnspan=2)
    voltageOutputCheckLabel.grid(row=1, column=0, sticky='we')
    voltageCheckVLabel.grid(row=1, column=1, sticky='nswe')
    voltageSuccessLabel.grid(row=2, column=0, columnspan=2, sticky='nsew')

#triangleFile = Image.open('triangle.png')
#trianglePIL = ImageTk.PhotoImage(triangleFile)
#triangleCanvas = Canvas(root, width=700, height=500)
#triangleCanvas.pack(fill='both', expand=True)
#triangleCanvas.create_image(0,0, image=trianglePIL)
welcomeLabel = Label(root, text='WELCOME TO\nBREADBEAST!', font=(None, 40, 'bold'), padx=30, pady=80)
welcomeLabel.grid(row=0, column=1, columnspan=5)
measureButton = Button(root, text='Measure', font=(None, 15), command=measurePage, justify='center')
measureButton.grid(row=1, column=2, sticky='ew')
welcomeButtonSeparator = Label(root, text='|', font=(None, 15))
welcomeButtonSeparator.grid(row=1, column=3, sticky='ew')
learnButton = Button(root, text='Learn', font=(None,15), command=learnPage)
learnButton.grid(row=1, column=4, sticky='ew', ipadx=12)
root.grid_columnconfigure((0, 6), weight=1)

s = StringVar()
success = StringVar()
s.set('0.00')
success.set('|||||||||||||||||')

Frame = Frame(root)
back = Button(Frame, text='Back', font=(None,15), command=back)
#Measure Page
measureVoltageLabel = Label(Frame, text='Measure Voltage (Under 5V)', font=(None, 30), padx=30, pady=80)
measureVoltageButton = Button(Frame, text='Begin:', font=(None,15), command=beginVoltage)
voltageOutputLabel = Label(Frame, textvariable=s, font=(None,15), bg='black', fg='white', padx=50)
voltageVLabel = Label(Frame, text='V', font=(None,15), pady=25)
#Learn Page
learnLabel = Label(Frame, text='Construct the following circuit:\nConnect the voltage probe as indicated below.', font=(None, 15), padx=30, pady=40, justify='left')
secondaryFrame = Label(Frame)
secondaryFrame.grid_columnconfigure(1, weight=1)
circuitFile = Image.open('circuit.png')
circuitPIL = ImageTk.PhotoImage(circuitFile)
circuitLabel = Label(Frame, image=circuitPIL, bg='black')
learnSeparator = Label(Frame, text='        ')
learnVoltageButton = Button(secondaryFrame, text='Check Voltage:', font=(None,15), command=learnVoltage, padx=25)
voltageOutputCheckLabel = Label(secondaryFrame, textvariable=s, font=(None,15), bg='black', fg='white', padx=20)
voltageCheckVLabel = Label(secondaryFrame, text='V', font=(None,15), pady=10, padx=20)
voltageSuccessLabel = Label(secondaryFrame, textvariable=success, font=(None,15), bg='black', fg='green2')

root.mainloop()
