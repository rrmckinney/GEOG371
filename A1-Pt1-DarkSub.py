from pci.drsub import *

# input file name, including file path - you need to change these accordingly
fili	=	'C:\Path\To\Your\File\L71018030_03020020810_radiance_sub.pix' 
# output file name, including path - you need to change these accordingly
filo	=	'C:\Path\To\Your\File\L71018030_03020020810_radiance_sub_DARK_idle.pix'
# rectangular window (Xoffset, Yoffset, Xsize, Ysize) with the dark pixels
#  you can keep the 10x10 window size but need to change the 
#  offsets with your recorded dark pixel coordinates (integer values only)
dbiw	=	[999, 666, 10, 10]
drtype	=	'global'

drsub( fili, filo, dbiw, drtype )
