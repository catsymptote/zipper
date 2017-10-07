## Author: Catsymptote


#############
## Imports ##
#############

from tkinter import *
from tkinter import filedialog
from tkinter import Tk, Checkbutton, Label
from tkinter import StringVar, IntVar

import sys
import os

from lib import zipper



###################
## GUI functions ##
###################

def zipSingleFile():
    zipper.zipFile("testfolder\\testfile.txt", "testfilezip.zip", password_encryption.get(), entry_password.get())


def zipFolder():
    zipper.zipFolder("testfolder\\", "testfolderzip.zip", password_encryption.get(), entry_password.get())


def set_dir():
    global root_dir
    root_dir_tmp = filedialog.askdirectory() # Set the file directory
    if (root_dir_tmp != ""):
        root_dir = root_dir_tmp
        #file_duplication_finder.set_main_dir_out(dir_out_var)
        print("Output directory:\t" + str(root_dir))
        sys.stdout.flush()


def set_output_dir():
    global output_dir
    output_dir_tmp = filedialog.askdirectory() # Set the file directory
    if (output_dir_tmp != ""):
        output_dir = output_dir_tmp
        #file_duplication_finder.set_main_dir_out(dir_out_var)
        print("Output directory:\t" + str(output_dir))
        sys.stdout.flush()


def set_filename():
    global file_name
    file_name_tmp = filedialog.askopenfilename() # Set the file name
    if (file_name_tmp != ""):
        file_name = file_name_tmp
        #file_duplication_finder.set_main_dir_out(dir_out_var)
        print("Output directory:\t" + str(file_name))
        sys.stdout.flush()




#########################
## Window construction ##
#########################

# Start ----------
root_window = Tk()  # Window constructor / blank window
# Start ----------


##############
## Vaiables ##
##############

## Directories
output_dir = StringVar()
output_dir.set("D:\\Projects\\Python\\zipper\\output")
root_dir    = StringVar()
root_dir.set("D:\\Projects\\Python\\zipper\\testfolder")
file_name   = StringVar()
file_name.set("D:\\Projects\\Python\\zipper\\testfolder\\testfile.txt")
output_name = StringVar()
output_name.set("D:\\Projects\\Python\\zipper\\output\\testzip.zip")

## Password / encryption
password_encryption = BooleanVar()
#password_encryption = IntVar()
password = StringVar()


## Run buttons
button_1 = Button(
    root_window,
    text="Zip file",
    command=zipSingleFile
    #command=file_duplication_finder.copy_duplicates_from_1
)

button_2 = Button(
    root_window,
    text="Zip folder",
    command=zipFolder
)

button_1.grid(columnspan=1, row=0, column=0)
button_2.grid(columnspan=1, row=0, column=1)


## Browse buttons
button_browse_out = Button(
    root_window,
    text="Output folder",
    command=set_output_dir
)

button_browse_in = Button(
    root_window,
    text="Input folder",
    command=set_dir
)

button_browse_file = Button(
    root_window,
    text="File",
    command=set_filename
)

button_browse_out.grid(columnspan=1, row=1, column=0)
button_browse_in.grid(columnspan=1, row=2, column=0)
button_browse_file.grid(columnspan=1, row=3, column=0)


## Checkbuttons
checkbutton_password = Checkbutton(
    root_window,
    text="Encrypted",
    state=ACTIVE,
    #offvalue=False,
    #onvalue=True,
    #offvalue=0,
    #onvalue=0, # Makes it marked (true)
    variable=password_encryption
)

checkbutton_password.grid(columnspan=1, row=3, column=0)


## Entry
entry_password = Entry(
    root_window
)

entry_password.grid(columnspan = 2, row=3, column=1)


## Labels
label_out = Label(root_window, textvariable=output_dir)
label_in = Label(root_window, textvariable=root_dir)

label_out.grid(columnspan=3, row=1, column=2, sticky=W)
label_in.grid(columnspan=3, row=2, column=2, sticky=W)




# Stop ---------------
root_window.mainloop()
# Stop ---------------


print("-----<> Done <>-----")
#print(dir_in_1_var)
#print(dir_in_2_var)
#print(dir_out_var)
