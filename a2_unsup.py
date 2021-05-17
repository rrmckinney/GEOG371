# unsupervised classifications KCLUS and ISOCLUS
# KCLUS result will be channel 1 ... rename manually after running
# ISOCLUS result will be channel 2 ... rename manually after running

# specifying the input file - need to change path
in_file = r"C:\Path\to\your\A2data\folder\G371_2020_A2_data\Initial_image_clip\June2015clip.pix"

# Using PCIMOD to add channels to save classification outputs...
# ...used for unsupervised and supervised classifications

# Importing the module
from pci.pcimod import *

file = in_file
pciop = 'ADD' 	        # set parameter to ADD channels
pcival = [7, 0, 0, 0]   # set to add 7 8-bit channels 

try:pcimod(file, pciop, pcival)
except PCIException as e:print(e)
except Exception as e:print(e)

print("")
print("PCIMOD completed. Channels were added.")



# starting KCLUS module

from pci.kclus import kclus

file	=	in_file
dbic	=	[9,-14]	# input channels
dboc	=	[1]	# output channel
mask	=	[]	# process entire image
numclus	=	[16]	# requested number of clusters
seedfile	=	''	#  automatically generate seeds
maxiter	=	[20]	# no more than 20 iterations
movethrs	=	[0.01]

kclus( file, dbic, dboc, mask, numclus, seedfile, maxiter, movethrs)

print("")
print ('KCLUS done.')


# starting ISOCLUS module

from pci.isoclus import *

file	=	in_file	# input file
dbic	=	[9,-14]	# input channels
dboc	=	[2]	# output channel
mask	=	[]	# process entire channel
numclus	=	[10]	# request 10 clusters
maxclus	=	[20]	# at most 20 clusters
minclus	=	[5]	# at least 5 clusters
seedfile	= "" 	# automatically generate seeds
maxiter	=	[20]	# no more than 20 iterations
movethrs	=	[0.01]
siggen	=	"NO"	# no signature generation
samprm	=	[5]     # minimum sample threshold
stdv	=	[10.0]  # standard deviation
lump	=	[1.0]   # lumping parameter
maxpair	=	[5]	# no more than 5 cluster center pairs clumped in one iteration
backval	=	[]	# no background value
nsam	=	[]	# default number of samples

isoclus( file, dbic, dboc, mask, numclus, maxclus, minclus, seedfile, maxiter,
         movethrs, siggen, samprm, stdv, lump, maxpair, backval, nsam )

print("")
print ('ISOCLUS done.')
