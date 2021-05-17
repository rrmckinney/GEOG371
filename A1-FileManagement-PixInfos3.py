# Now we can combine the functionality of the two code cells above, exploring pix file properties in a folder.
# In the IDLE version, the first two scripts (A1-FileManagement-PixInfos1.py, A1-FileManagement-PixInfos2.py)...
# ...are combined in the script A1-FileManagement-PixInfos3.py

# Importing the required packages
import os
import pci
from pci.api import datasource as ds
from pci.exceptions import *
import sys
import fnmatch

# The locale settings ensure Python is configured...
# ...the same way as PCI's C/C++ code
import locale

locale.setlocale(locale.LC_ALL, "")
locale.setlocale(locale.LC_NUMERIC, "C")

# ------ setting the input files -----
# User can pick the input folder containing the pix files (incl. subfolders)
InFolder = input(r"Select a directory containing your input imagery (e.g. C:\Users\yourusername\g371-env\Kitchener_L7) and hit enter: ")

# Setting up a file filter, so only pix files are considered
file_filter = "*.pix"

# Setting up the list that will contain the full pathnames of each file in the InFolder
input_files_list = []

# --- Creating the file list from the input folders and subfolders with loops ---
# os.walk searches a directory tree and produces the file names of the files found
# r is the main folder
# d is any subfolder
# f are image files (pix) within r
for r, d, f in os.walk(InFolder):
    for images in fnmatch.filter(f, file_filter):
        ##print(("Found valid input: "), images)
        input_files_list.append(os.path.join(r, images))      

# ---Looping over the valid pix files and generate the file properties
for images in input_files_list:
    
    # define the properties to print later
    with ds.open_dataset(images) as infile:
        name = infile.name
        rows = infile.width
        cols = infile.height
        chans = infile.chan_count

        # print the data dimensions
        print ('')
        print(('File: '), name)
        print(('rows '), rows)
        print(('columns '), cols)
        print(('channels '), chans)
