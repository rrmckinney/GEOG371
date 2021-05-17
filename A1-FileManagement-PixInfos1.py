# This script lets you choose a folder and searches it for any pix files and prints the list of files it finds.
# This script would still execute without the Geomatica API, as it does not use its functionality.

# Importing packages for extracting file names, getting stats, etc.
import sys
import os
import fnmatch

# User directions and information.
print(r"Select a directory containing your input imagery (e.g. C:\Users\yourusername\g371-env\Kitchener_L7) and hit enter.")
print("")

# User can pick the input folder containing the pix files (incl. subfolders)
InFolder = input('Please type in the input folder path (can contain subfolders)' )
print("Input folder is ", InFolder)

# Setting up a file filter, so only pix files are considered
file_filter = "*.pix"

# Setting up the list that will contain the full pathnames of each file in the InFolder
input_files_list = []

# --- Creating the file list from the input folder and subfolders with loops ---
# os.walk searches a directory tree and produces the file names of the files found.
# r is the main folder.
# d is any subfolder.
# f are image files (pix) within r
for r, d, f in os.walk(InFolder):
	for file in fnmatch.filter(f, file_filter):
		print("Found valid input: ", file)
		input_files_list.append(os.path.join(r, file))
