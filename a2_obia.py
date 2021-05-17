# Object-based image classification with Geomatica API
# Based on https://support.pcigeomatics.com/hc/en-us/articles/360046636572-Object-Analyst-Batch-Classification-in-Python-Geomatica-Banff-SP2
## Double-commented out sections is code for SVM classifier (includes rasterization), Random Trees (RT) classifier doesn't work with rasterization

# *** Importing modules ***
# *************************

from pci import algo        # for all the Object-Analyst calculations
##from pci.poly2ras import *  # for poly to raster conversion of segmentated polygon classifications (SVM only)
import os       # for file management
import glob     # for file management


# *** Setting up folders ***
# **************************

# Change folder paths accordingly
input_main = r"C:\Path\to\your\A2data\folder\G371_2020_A2_data"
input_initial = r"C:\Path\to\your\A2data\folder\G371_2020_A2_data\Initial_image_clip"
input_addtl = r"C:\Path\to\your\A2data\folder\G371_2020_A2_data\Additional_images_clip"
output_folder = r"C:\Path\to\your\A2data\folder\G371_2020_A2_data\Python_processing_clip"

# *** Defining input variables ***
# ********************************

# Initial Image - This image will be used to generate the training model
init_image = os.path.join(input_initial, "June2015clip.pix")
# Ground truth point file
ground_truth = os.path.join(input_main, "training_points_clip_a2.pix")
# Additional Images - The batch classification will be run images in this folder
add_images = input_addtl


# *** Defining output variables ***
# *********************************

# Intial segmentation containing the training sites ... to be created
init_seg = os.path.join(output_folder, "June2015clip_seg_OBIA.pix")
# Text file containing exported attribute names
fld = os.path.join(output_folder, "Training_SegAttr.txt")
# Training model
training_model = os.path.join(output_folder, "Training_model_clip.xml")


# ***Processing initial image***
# ******************************

print("Processing initial image:", os.path.basename(init_image))

# OASEG (OASEGSAR) - Segment an image
algo.oaseg(fili=init_image, filo=init_seg, segscale=[35], segshape=[0.5], segcomp=[0.5])

# OACALCATT (OACALCATTSAR) - Calculate object attributes
algo.oacalcatt(fili=init_image, dbic=[2, 3, 4, 5, 6], filv=init_seg, dbvs=[2], filo=init_seg, dbov=[2], statatt="MAX, MEAN",
               geoatt="REC", index="NDVI")

# OAGTIMPORT - Import ground-truth points into an existing segmentation
algo.oagtimport(gtfili=ground_truth, gtfldnme="Training", filv=init_seg, dbvs=[2],filo=init_seg, dbov=[2],
                samptype="Training", resrule="First")

# OAFLDNMEXP - Export names of attribute fields from Focus Object Analyst to a text file
algo.oafldnmexp(filv=init_seg, dbvs=[2], fldnmflt="ALL_OA", tfile=fld)


# Random Trees Classification: 2 code lines below
#OARTTRAIN - Object-based Random Trees training
algo.oarttrain(filv=init_seg, dbvs=[2], tfile=fld, trnmodel=training_model)

# OARTCLASS - Object-based Random Trees classifier
algo.oartclass(filv=init_seg, dbvs=[2], trnmodel=training_model, filo=init_seg, dbov=[2])


### SVM Classification - 2 code lines below
### OASVMTRAIN - Object-based SVM training
##algo.oasvmtrain(filv=init_seg, dbvs=[2], trnfld="Training", tfile=fld, kernel="RBF", trnmodel=training_model)
##
### OASVMCLASS - Object-based SVM classifier
##algo.oasvmclass(filv=init_seg, dbvs=[2], trnmodel=training_model, filo=init_seg, dbov=[2])

### Rasterizing the initial image (only for SVM)
##print ("Rasterizing initial image")
##poly2ras(fili = init_seg , dbvs = [2], filo = os.path.join(output_folder, "June2015clip_seg_ras_OBIA.pix"),
##         dboc = [], imgtyp = "Raster", fldnme = "Label", pixres = [30, 30], ftype = "PIX", foptions = "")


# *** Starting Batch Section ***
# ******************************

# Apply training model and classify additional image in batch
print("Processing additional images in batch...")
file_list = glob.glob(os.path.join(add_images, "*.pix"))

for image in file_list:
    print("Currently processing:", os.path.basename(image))
    add_seg = os.path.join(output_folder, os.path.basename(os.path.splitext(image)[0]) + '_seg_OBIA.pix')

    # OASEG (OASEGSAR) - Segment an image
    algo.oaseg(fili=image, filo=add_seg, segscale=[35], segshape=[0.5], segcomp=[0.5])

    # OACALCATT (OACALCATTSAR) - Calculate object attributes
    algo.oacalcatt(fili=image, dbic=[2,3,4,5,6], filv=add_seg, dbvs=[2], filo=add_seg, dbov=[2], statatt="MAX, MEAN",
                   geoatt="REC", index="NDVI")

    # OARTCLASS - Object-based Random Trees classifier
    algo.oartclass(filv=add_seg, dbvs=[2], trnmodel=training_model, filo=add_seg, dbov=[2])
    
##    # OASVMCLASS - Object-based SVM classifier
##    algo.oasvmclass(filv=add_seg, dbvs=[2], trnmodel=training_model, filo=add_seg, dbov=[2])
##
##    # POLY2RAS to create raster version of vector segmentations
##    print ("Rasterizing...")
##    add_seg_ras = os.path.join(output_folder, os.path.basename(os.path.splitext(image)[0]) + '_seg_ras_SVM.pix') # for output raster name
##    poly2ras(fili = add_seg , dbvs = [2], filo = add_seg_ras,
##             dboc = [], imgtyp = "Raster", fldnme = "Label", pixres = [30, 30], ftype = "PIX", foptions = "")

print("All done.")

