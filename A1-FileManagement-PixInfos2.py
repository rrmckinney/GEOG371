# This code looks at some image info for one image.

# Importing the packages
import os
import pci
from pci.api import datasource as ds

# Get the path to any folder that contains pix files (example provided in code below)
# Change the code accordingly to use a file that you can access.
input_pix = os.path.join('C:\Users\yourusername\g371-env\Kitchener_L7', 'L71018030_03020020810_radiance_sub.pix')

# Open the dataset
with ds.open_dataset(input_pix) as dataset:
    rows = dataset.width
    cols = dataset.height
    chans = dataset.chan_count
    
# print the data dimensions
print ('')
print('File: ', input_pix)
print('rows ', rows)
print('columns ', cols)
print('channels ', chans)
