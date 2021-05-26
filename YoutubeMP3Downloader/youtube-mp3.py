from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import pafy #pip install pafy #pip install youtube-dl

Folder_Name = ""

def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name, fg="green")

    else:
        locationError.config(text = "Please Choose Folder!!", fg="red")

def Download():
    url = urlEntry.get()

    if(len(url)>1):
        urlError.config(text="")
        file = pafy.new(urlEntry.get())
        bestaudio = file.getbestaudio()
    else:
        urlError.config(text = "Paste Link again!",fg="red")

    bestaudio.download(filepath = Folder_Name)
    urlError.config(text = "Download Completed")

    
root = Tk() 
root.title("Youtube to webm")
root.geometry("350x300") #window dimentions
root.columnconfigure(0, weight = 1) #centers all content

urlLabel = Label(root, text = "Enter Video URL", font = ("jost",15))
urlLabel.grid()

urlError = Label(root, text = "Error Msg", fg="red", font = ("jost",10))
urlError.grid()

urlEntryVar = StringVar()
urlEntry = Entry(root, width = 50, textvariable = urlEntryVar)
urlEntry.grid()

saveLabel = Label(root, text = "Save the Video File", font = ("jost",15,"bold"))
saveLabel.grid()

locationError = Label(root, text = "Error Msg of Path", fg = "red",font=("jost",10))
locationError.grid()

saveEntry = Button(root, width = 10,bg = "red", fg = "white", text = "Choose Path", command = openLocation)
saveEntry.grid()

emptySpace = Label(root, text = "")
emptySpace.grid()

downloadBtn = Button(root, text="Download", width=10, bg="red", fg="white", command = Download)
downloadBtn.grid()
root.mainloop()