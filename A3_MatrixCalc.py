# Error matrices and related output are created with the MLR algorithm from the PCI API.
# See the PCI Help for detailed info on the MLR algorithm and its outputs.

import os
from pci.mlr import mlr
from pci.nspio import Report, enableDefaultReport

# CHANGE THE WORKING_DIR AND CLASSIFIED_IMAGE ACCORDING TO YOUR FILE/FOLDER NAMES
# set working directory and input file (the input file needs to be in that folder)
# input file that has the raster reference samples as layer 1, followed by all raster classifications
working_dir = r'C:\Path\to\your\workingfolder'
classified_image = working_dir + os.sep + 'YourInputFile.pix'


layers = (2,3,4,5)    # all classification layers to be used for matrix calculation

print ('Start processing layers...')
for x in layers:
    
    try:

        # creating separate txt files for each MLR output
        # folder 'MatrixFiles' will contain the MLR output txt files
        # L# (e.g.) L2 indicates layer 2
        print (x)
        rep_file = os.path.join(working_dir + os.sep + 'MatrixFiles' + os.sep + os.path.basename('MLR_report_L') + str(x) + '.txt')
        print (rep_file)
        
        Report.clear()
        enableDefaultReport(rep_file)
        
        file=classified_image
        units='KILO'
        dbic=[x]
        dbsa=[1]        # specifying layer 1 having the raster sample reference areas
        dbs1=[]
        matrix='YES'    # output error matrix set to yes
        mask=[]
        
        mlr(file, units, dbic, dbsa, dbs1, matrix, mask)
        
    finally:
        enableDefaultReport('term')  # this will close the report file

print ('All done. Check the working dir for the report files.')




