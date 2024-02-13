import os
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw
import modules.input as inp
import modules.process as strprocess

# Init Variables
selectedFile = ""
actualFileName = ""
SCALE = 10


def browseFiles():
    global selectedFile, actualFileName
    filename = filedialog.askopenfilename(initialdir="~/", title="Select a File")
    selectedFile = filename
    actualFileName = '"' + os.path.splitext(os.path.basename(selectedFile))[0] + '"'
    if selectedFile == "":
        return

    # Change label contents
    # label_file_explorer.configure(text="File Opened: "+os.path.basename(selectedFile))
    # Enable Process button
    button_process.configure(state=ACTIVE)

def processFile():
    # Set Variables
    # filestringer = '"' + selectedFile + '"'
    inputFileHex = inp.returnhex(selectedFile)
    inputFileHex = inp.returnlistlength(inputFileHex, 2)
    loomHexFile = strprocess.loomvaluesprep(inputFileHex, SCALE)
    # Run Hex Dump / Only works in linux currently
    # Enable Script button
    runScript(loomHexFile)


def runScript(inputlist):
    im = Image.new("RGB", (255 * SCALE, 255 * SCALE), (255, 255, 255))
    draw = ImageDraw.Draw(im)
    draw.polygon(xy=inputlist, outline=(0, 0, 0))
    im.show()

# Create the root window
window = Tk()

# Set window title
window.title('Picture Import')

# Set window size
window.geometry("200x200")
window.resizable(False, False)

# Set window background color
window.config(background="white")

# Create a File Explorer label
# label_file_explorer = Label(window, anchor="center")

# Setup Buttons
button_explore = Button(window, text="Browse Files", command=browseFiles)
button_process = Button(window, text="Process", command=processFile, state=DISABLED)
button_exit = Button(window, text="Exit", command=exit)

# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
# label_file_explorer.grid(column = 0, row = 1)
button_explore.grid(column=0, row=2)
button_process.grid(column=0, row=3)
button_exit.grid(column=0, row=5)

# Let the window wait for any events
window.mainloop()

# Draw File
