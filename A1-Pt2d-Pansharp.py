# Pansharpening

# Importing the module
from pci.pansharp import *

# Input file name, including file path - you need to change this accordingly
# Use the Kagoshima_L7multi.pix file with the correct path
fili = r"C:\Path\To\Your\File\Kagoshima_L7multi.pix"
dbic =	[1,2,3,4,5,6]       # the bands to be sharpened
dbic_ref = dbic
fili_pan =  r"C:\Path\To\Your\File\Kagoshima_L7pan.pix" # the PAN image
dbic_pan = [1]
srcbgd	= "ANY,0"	    # zero-valued pixels in any input image
enhance	= "YES" 	    # apply the color enhancement operation
resample = "CUBIC"          # uses cubic resampling when resampling MS image to high resolution OPTION2: change to BILIN
filo = r"C:\Path\To\Your\File\Kagoshima_L7pansharpCUBIC.pix" #output file
dboc =	[1,2,3,4,5,6]
ftype = "PIX"		    # the output file will be in PIX format
foptions = ""	            # output file can be tiled but set to none
poption	= "AVER"	    # unweighted averaging resampling

pansharp (fili, dbic, dbic_ref, fili_pan, dbic_pan, srcbgd, enhance, resample, filo, dboc, ftype, foptions, poption)
print('Pansharpening completed. Check results in the output folder.')
