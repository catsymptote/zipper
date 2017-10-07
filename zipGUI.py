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




##############
## Vaiables ##
##############

## Directories
output_dir  = "D:\\Projects\\Python\\zipper\\output"
root_dir    = "D:\\Projects\\Python\\zipper\\testfolder"
file_name   = "D:\\Projects\\Python\\zipper\\testfolder\\testfile.txt"
output_name = "D:\\Projects\\Python\\zipper\\output\\testzip.zip"

## Password / encryption
password_encryption = False
password    = "1234"



###################
## GUI functions ##
###################

"""
def get_directory():
    current_directory = filedialog.askdirectory()   # Set the file directory
    if (current_directory != ""):
        print (current_directory)
        sys.stdout.flush()


def change_dir_in_1():
    pass
    global dir_in_1
    global dir_in_1_var
    dir_in_1_var = filedialog.askdirectory()    # Set the file directory
    if (dir_in_1_var != ""):
        dir_in_1.set(dir_in_1_var)
        #file_duplication_finder.set_main_dir_1(dir_in_1_var)
        print("First input directory:\t" + str(dir_in_1_var))
        sys.stdout.flush()


def change_dir_in_2():
    pass
    global dir_in_2
    global dir_in_2_var
    dir_in_2_var = filedialog.askdirectory()    # Set the file directory
    if (dir_in_2_var != ""):
        dir_in_2.set(dir_in_2_var)
        #file_duplication_finder.set_main_dir_2(dir_in_2_var)
        print("Second input directory:\t" + str(dir_in_2_var))
        sys.stdout.flush()


def change_dir_out():
    pass
    global dir_out
    global dir_out_var
    dir_out_var = filedialog.askdirectory() # Set the file directory
    if (dir_out_var != ""):
        dir_out.set(dir_out_var)
        #file_duplication_finder.set_main_dir_out(dir_out_var)
        print("Output directory:\t" + str(dir_out_var))
        sys.stdout.flush()
"""

"""
def zipSingleFile():
    zipper.zipFile("testfile.txt", "testzap.zip", False, "secret")


def zipFolder():
    zipper.zipFolder("testfolder\\", "testzap.zip", False, "secret")
"""


def zipSingleFile():
    zipper.zipFile("testfolder\\testfile.txt", "testfilezip.zip", password_encryption, password)


def zipFolder():
    zipper.zipFolder("testfolder\\", "testfolderzip.zip", password_encryption, password)


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
    variable=password_encryption
)

checkbutton_password.grid(columnspan=1, row=0, column=2)

## Labels
"""

label_out = Label(root_window, textvariable=dir_out)

label_in_1.grid(columnspan=3, row=1, column=1, sticky=W)
label_in_2.grid(columnspan=3, row=2, column=1, sticky=W)
label_out.grid(columnspan=3, row=3, column=1, sticky=W)
"""


# Stop ---------------
root_window.mainloop()
# Stop ---------------


print("-----<> Done <>-----")
#print(dir_in_1_var)
#print(dir_in_2_var)
#print(dir_out_var)
