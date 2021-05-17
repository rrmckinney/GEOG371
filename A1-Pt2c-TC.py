# Tassel Cap

# Importing the module
from pci.tassel import tassel

# Input file name, including file path - you need to change this accordingly
# Use the LT51960261989145KIS00_PIX.pix file with the correct path
fili = r'C:\Path\To\Your\File\LT51960261989145KIS00_PIX.pix'
visirchn = [1,2,3,4,5,6]
filo = r'C:\Path\To\Your\File\LT51960261989145KIS00_PIX_TC.pix'
ftype = 'PIX'
foptions =''
scaloffs = []
scalfact = []
datatype = '16S'

tassel(fili, visirchn, filo, datatype, scaloffs, scalfact, ftype, foptions)

print('TC calculation completed. Check results in the output folder.')
