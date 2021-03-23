import numpy as np
import os
import imageio
import cv2
from tqdm import tqdm
from PIL import Image
#from skimage.transform import resize
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import re
import shutil
#from boundary_morph import bwmorph_thin 
'''
It can also handel distributing the xml files
'''
numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

op_dir = 'E:/MIA/PanNuke/splitsv2/'
data_dir = 'E:/MIA/PanNuke/processed/'


test_split = 0.20
val_split = 0.1

all_dir = os.listdir(data_dir)
for d in all_dir:
    img_dir = data_dir + '/{}/images/'.format(d)
    sem_dir = data_dir + '/{}/sem_masks/'.format(d)
    inst_dir = data_dir + '/{}/inst_masks/'.format(d)
    
    img_list = sorted(os.listdir(img_dir), key=numericalSort)# This will get all the file names in the folder
    sem_list = sorted(os.listdir(sem_dir), key=numericalSort)# This will get all the file names in the folder
    inst_list = sorted(os.listdir(inst_dir), key=numericalSort)
    
    print('\rTotal Images Found in {}  ='.format(d), len(img_list))
    #print('\rTotal Sem_masks Found =', len(sem_list))
    #print('\rTotal Inst_masks Found =', len(inst_list))
    
    train_val_img, test_img, train_val_sem, test_sem, train_val_inst,  test_inst = \
        train_test_split(img_list, sem_list, inst_list, test_size=test_split, random_state=42)
    
    train_img, val_img, train_sem, val_sem, train_inst, val_inst = \
        train_test_split(train_val_img, train_val_sem, train_val_inst, test_size=val_split, random_state=42)
    print('='*40)
    print('Training Images   =', len(train_img))
    print('Testing Images    =', len(test_img))
    print('Validation Images =', len(val_img))
    print('/'*40)

    temp_img = [test_img, train_img, val_img]
    temp_sem_mask = [test_sem, train_sem, val_sem]
    temp_inst_mask = [test_inst, train_inst, val_inst]
    folder = ['test', 'train', 'val']
    '''
    0:  flag for grayscale
    1:  flag for RGB
    -1: flag for unchanged data
    '''
    #print('\nWait untill 3 bars are 100%...\n')
    for z in range(3):
        
        img_paths = [os.path.join(img_dir, fname) for fname in temp_img[z]]
        sem_mask_paths = [os.path.join(sem_dir, fname) for fname in temp_sem_mask[z]]
        inst_mask_paths = [os.path.join(inst_dir, fname) for fname in temp_inst_mask[z]]
        i = 0
        for imgpath, semgtpath, instgtpath in tqdm(zip(img_paths, sem_mask_paths, inst_mask_paths), total = len(temp_img[z]), desc='Moving {} data to new dir'.format(folder[z])):
        
            
            '''
            for reading image and xml file uncomment following lines
            '''
            shutil.copy2(imgpath, (op_dir + folder[z] + '/images/'))
            shutil.copy2(semgtpath , (op_dir + folder[z] + '/sem_masks/'))
            shutil.copy2(instgtpath, (op_dir + folder[z] + '/inst_masks/'))
            
            i = i+1
    #print('\rDone processing {} images'.format(folder[z]))
#%%
# Save splits in text file
f_name = ['test', 'train', 'val']
for i in range(3):
    
    file = open('D:/cw_projects/{}.txt'.format(f_name[i]), 'w')
    
    for ele in temp_img[i]:
        file.write(ele + '\n')
    file.close()
