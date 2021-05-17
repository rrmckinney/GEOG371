# Principal Component Analysis (PCA)

# In order to run the PCA, the input file needs to be prepared first. 
# Using another module (PCIMOD), additional channels will be added that will be used for the PCA bands. 
# This needs to be run first before doing the actual PCA. 
# Look at the comments in the code to make the neccesary changes before running the code.

## You will also interact with the terminal for this part and use report information... 
## ...that you need to copy and paste from the terminal/shell window to a spreadsheet (e.g. Excel).

### If you do not get any output to the shell window, run the script within Focus - Tools | Python Scripting
### Copy/paste the code into the scripting window and run it with the Run icon.

# Using PCIMOD to add 6 32-bit unsigned channels to save PCA bands.

# Importing the module
from pci.pcimod import *

# Input file name, including file path - you need to change this accordingly
# Use the Kagoshima_L7multi_PCA.pix file with the correct path
file = r'C:\Path\To\Your\File\Kagoshima_L7multi_PCA.pix'
pciop = 'ADD' 	        # set parameter to ADD channels
pcival = [0, 0, 0, 6]   # set to add 6 32bit channels and no 8bit or 16bit signed or unsigned channels

try:pcimod(file, pciop, pcival)
except PCIException as e:print(e)
except Exception as e:print(e)

print("")
print("PCIMOD completed. Channels were added.")


# actual PCA

# Importing the module
from pci.pca import *

# Input file name, including file path - you need to change this accordingly
# Use the Kagoshima_L7multi_PCA.pix file with the added bands and the correct path
file	=	r'C:\Path\To\Your\File\Kagoshima_L7multi_PCA.pix'
dbic	=	[1,2,3,4,5,6]
eign	=	[1,2,3,4,5,6]	    # eigenchannels retained for output
dboc	=	[7,8,9,10,11,12]	# output to 6 new channels 7,8,9,10,11,12
midpoint	=	[]
devrange	=	[]
mask	=	[]
rtype	=	'LONG'	# default short report [changed to LONG]

pca( file, dbic, eign, dboc, midpoint, devrange, mask, rtype )

print('PCA calculation completed. Check result file in the output folder and information in the terminal window.')

