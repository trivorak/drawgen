import os
from tkinter import *
  
# import filedialog module
from tkinter import filedialog
selectedFile = ""
filedump = "~/Desktop/input.txt" 
scriptLocation = "~/git/midigen/research/drawcolorlines.py"
actualFileName = ""
scaleVal = 8
# Function for opening the 
# file explorer window
def browseFiles():
	global selectedFile, actualFileName
	filename = filedialog.askopenfilename(initialdir = "~/",title = "Select a File",filetypes = (("all files", "*.*"),("PNG Files", "*.png*")))
	selectedFile = filename
	actualFileName = '"'+os.path.splitext(os.path.basename(selectedFile))[0]+'"'
	if selectedFile == "":
		return

	# Change label contents
	# label_file_explorer.configure(text="File Opened: "+os.path.basename(selectedFile))
	# Enable Process button
	button_process.configure(state=ACTIVE)
	  
def processFile():
	# Set Variables
	filestringer = "'" + selectedFile + "'"
	# Run Hex Dump / Only works in linux currently
	os.system("xxd -p " + filestringer + " " +filedump)
	# Change Label 
	# label_file_explorer.configure(text="Processed: "+os.path.basename(selectedFile),fg="red")
	# Enable Script button
	button_script.configure(state=ACTIVE)

def runScript():
	os.system("cd ~/Desktop && python3 " + scriptLocation + " " + str(scaleVal)+ " " + actualFileName)
	# label_file_explorer.configure(text="Script Complete", fg="green")
																								  
# Create the root window
window = Tk()
  
# Set window title
window.title('Picture Import')
  
# Set window size
window.geometry("200x200")
window.resizable(False,False)
  
#Set window background color
window.config(background = "white")
  
# Create a File Explorer label
# label_file_explorer = Label(window, anchor="center")

# Setup Buttons
button_explore = Button(window,text = "Browse Files",command = browseFiles) 
button_process = Button(window, text = "Process",command = processFile, state=DISABLED)
button_script = Button(window, text= "Script", command = runScript, state=DISABLED)
button_exit = Button(window, text = "Exit",command = exit) 
  
# Grid method is chosen for placing
# the widgets at respective positions 
# in a table like structure by
# specifying rows and columns
# label_file_explorer.grid(column = 0, row = 1)
button_explore.grid(column = 0, row = 2)
button_process.grid(column = 0, row = 3)
button_script.grid(column = 0, row = 4)
button_exit.grid(column = 0,row = 5)
  
# Let the window wait for any events
window.mainloop()
