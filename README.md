[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FMr-TalhaIlyas%2FPrerpcessing-PanNuke-Nuclei-Instance-Segmentation-Dataset&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

# Pre-process PanNuke Dataset for Nuclei Instance Segmentation and Classification

PanNuke is an H&E stained image set, containing 7,904 256 × 256 patches from a total of 19 different tissue types. The nuclei are classified into neoplastic,
inflammatory, connective/soft tissue, dead, and epithelial cells. 
The dataset is divided into three folds where;

* Fold 1 contains 2,657 images
* Fold 2 contains 2,524 images
* Fold 3 contains 2,723 images

More info [here](https://jgamper.github.io/PanNukeDataset/)

You can download the dataset form [here](https://warwick.ac.uk/fac/sci/dcs/research/tia/data/pannuke)

Access the paper[here](https://arxiv.org/pdf/2003.10778.pdf)


Sample image form original repo

![alt text](https://github.com/Mr-TalhaIlyas/Prerpcessing-PanNuke-Nuclei-Instance-Segmentation-Dataset/blob/master/screens/img1.png)

Three different dataset splits are then made based on these three folds. Tow folds of data
are used for training/validation and one for testing set.


## Preporcessing 

After downloading the data you will get 3 `.zip` files namely `fold1`, `fold2` and `fold3`.
The data is stored as `numpy` arrays. After extracting directory structure is as follows,

```
📦Fold 1
 ┣ 📂images
 ┃ ┗ 📂fold1
 ┃ ┃ ┣ 📜images.npy
 ┃ ┃ ┗ 📜types.npy
 ┣ 📂masks
 ┃ ┣ 📂fold1
 ┃ ┃ ┗ 📜masks.npy
 ┃ ┣ 📜by-nc-sa.md
 ┃ ┗ 📜README.md
 ┗ 📜README.md
# Fold 2 and 3 also have similar structure
```

### Method 1

If you want to use the official splits than run the `process_pannuke_std.py` script form `scripts` dir. 
Just specify input output paths as follows

```python
data_dir = '../PanNuke/data/' # location to extracted folds
output_dir = '../Folds/' # location to save op data 
```
this script will create a dir containing the three folds. the data will be converted form `.npy` and saved in `.png` format. Each fold will be structured as follows

```
📦Fold 1
 ┣ 📂images
 ┣ 📂inst_masks
 ┗ 📂sem_masks
```
inside each `dir` the files will be named as follows, respectively;

```
img_Colon_2_01594.png

inst_Adrenal_gland_2_01041.png

sem_Bile-duct_2_01420.png
```
* The first word `inst` means this mask contains instance information in form of boundaries
	1. `sem` means its semantic mask
	2. `img` means its H&E image
* Next word is the `Adrenal_gland` is the tissue type
* The nexr `2` represents this image is form 2nd fold of original dataset
* The last number `01041` represents the iamge number

### Method 2

In this method I split the dataset tissue wise. So the data will be saved in 19 directories depending upon the tissue.
To generate this data run the `process_pannuke.py` script form `scripts` dir. 
Just specify input output paths as follows

```python
data_dir = '../PanNuke/data/' # location to extracted folds
output_dir = '../processed/' # location to save op data 
```
this script will create a dir containing the 19 sub-dir as follows
```
📦processed2
 ┣ 📂Adrenal_gland
 ┣ 📂Bile-duct
 ┣ 📂Bladder
 ┣ 📂Breast
 ┣ 📂Cervix
 ┣ 📂Colon
 ┣ 📂Esophagus
 ┣ 📂HeadNeck
 ┣ 📂Kidney
 ┣ 📂Liver
 ┣ 📂Lung
 ┣ 📂Ovarian
 ┣ 📂Pancreatic
 ┣ 📂Prostate
 ┣ 📂Skin
 ┣ 📂Stomach
 ┣ 📂Testis
 ┣ 📂Thyroid
 ┗ 📂Uterus
```
and the data will be converted form `.npy` and saved in `.png` format. Each tissue dir will be structured as follows;

```
 📂Uterus
 ┃ ┣ 📂images
 ┃ ┣ 📂inst_masks
 ┃ ┗ 📂sem_masks
```
The nomenclature of files is same as in Method 1.

### Custom Splits
Now the data is saved in dir now you can split dataset into `train`, `val` and `test` splits. For that run the spliy_pannuke.py` script form `scripts` dir. 
specify the input/output directories and the split ratio i.e. how much of the data would like to use for `val` and `test`.

```python
op_dir = '../splits/' # output dir for splits
data_dir = '../processed/' # dir containing the tissue wise splits Method 2


test_split = 0.20 # 20% of total data
val_split = 0.1   # 10% of total data
```

now the `op_dir` will have following structure

```
📦splits
 ┣ 📂test
 ┃ ┣ 📂images
 ┃ ┣ 📂inst_masks
 ┃ ┗ 📂sem_masks
 ┣ 📂train
 ┃ ┣ 📂images
 ┃ ┣ 📂inst_masks
 ┃ ┗ 📂sem_masks
 ┗ 📂val
 ┃ ┣ 📂images
 ┃ ┣ 📂inst_masks
 ┃ ┗ 📂sem_masks
```
#### Note: This script will split the data tissue wise i.e. 10% of images from each tissue type will be used for `val` and 20% for `test`.

If you run the script wiht above values then the splits are as follows;

```
Total Images Found in Adrenal_gland  = 437
========================================
Training Images   = 314
Testing Images    = 88
Validation Images = 35
////////////////////////////////////////
Total Images Found in Bile-duct  = 420
========================================
Training Images   = 302
Testing Images    = 84
Validation Images = 34
////////////////////////////////////////
Total Images Found in Bladder  = 146
========================================
Training Images   = 104
Testing Images    = 30
Validation Images = 12
////////////////////////////////////////
Total Images Found in Breast  = 2351
========================================
Training Images   = 1692
Testing Images    = 471
Validation Images = 188
////////////////////////////////////////
Total Images Found in Cervix  = 293
========================================
Training Images   = 210
Testing Images    = 59
Validation Images = 24
////////////////////////////////////////
Total Images Found in Colon  = 1440
========================================
Training Images   = 1036
Testing Images    = 288
Validation Images = 116
////////////////////////////////////////
Total Images Found in Esophagus  = 424
========================================
Training Images   = 305
Testing Images    = 85
Validation Images = 34
////////////////////////////////////////
Total Images Found in HeadNeck  = 384
========================================
Training Images   = 276
Testing Images    = 77
Validation Images = 31
////////////////////////////////////////
Total Images Found in Kidney  = 134
========================================
Training Images   = 96
Testing Images    = 27
Validation Images = 11
////////////////////////////////////////
Total Images Found in Liver  = 224
========================================
Training Images   = 161
Testing Images    = 45
Validation Images = 18
////////////////////////////////////////
Total Images Found in Lung  = 184
========================================
Training Images   = 132
Testing Images    = 37
Validation Images = 15
////////////////////////////////////////
Total Images Found in Ovarian  = 146
========================================
Training Images   = 104
Testing Images    = 30
Validation Images = 12
////////////////////////////////////////
Total Images Found in Pancreatic  = 195
========================================
Training Images   = 140
Testing Images    = 39
Validation Images = 16
////////////////////////////////////////
Total Images Found in Prostate  = 182
========================================
Training Images   = 130
Testing Images    = 37
Validation Images = 15
////////////////////////////////////////
Total Images Found in Skin  = 187
========================================
Training Images   = 134
Testing Images    = 38
Validation Images = 15
////////////////////////////////////////
Total Images Found in Stomach  = 146
========================================
Training Images   = 104
Testing Images    = 30
Validation Images = 12
////////////////////////////////////////
Total Images Found in Testis  = 196
========================================
Training Images   = 140
Testing Images    = 40
Validation Images = 16
////////////////////////////////////////
Total Images Found in Thyroid  = 226
========================================
Training Images   = 162
Testing Images    = 46
Validation Images = 18
////////////////////////////////////////
Total Images Found in Uterus  = 186
========================================
Training Images   = 133
Testing Images    = 38
Validation Images = 15
////////////////////////////////////////
```
