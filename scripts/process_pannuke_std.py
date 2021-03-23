import numpy as np
import matplotlib.pyplot as plt
import cv2
from PIL import Image
from skimage.segmentation import find_boundaries
import os, glob
from tqdm import trange, tqdm
import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 300

data_dir = 'E:/MIA/PanNuke/data/' # location to extracted folds
output_dir = 'C:/Users/Talha/Desktop/Folds/' # location to save op data 

os.chdir(data_dir)
folds = os.listdir(data_dir)

def get_boundaries(raw_mask):
    '''
    for extracting instance boundaries form the goundtruth file
    '''
    bdr = np.zeros(shape=raw_mask.shape)
    for i in range(raw_mask.shape[-1]-1): # because last chnnel is background
        bdr[:,:,i] = find_boundaries(raw_mask[:,:,i], connectivity=1, mode='thick', background=0)
    bdr = np.sum(bdr, axis = -1)
    return bdr.astype(np.uint8)

for i, j in enumerate(folds):
    
    # get paths
    print('Loading Data for {}, Wait...'.format(j))
    img_path =data_dir + j + '/images/fold{}/images.npy'.format(i+1)
    type_path = data_dir + j + '/images/fold{}/types.npy'.format(i+1)
    mask_path = data_dir + j + '/masks/fold{}/masks.npy'.format(i+1)
    print(40*'=', '\n', j, 'Start\n', 40*'=')
    
    # laod numpy files
    masks = np.load(file=mask_path, mmap_mode='r') # read_only mode
    images = np.load(file=img_path, mmap_mode='r') # read_only mode
    types = np.load(file=type_path) 
    
    # creat directories to save images
    try:
        os.mkdir(output_dir + j)
        os.mkdir(output_dir + j + '/images')
        os.mkdir(output_dir + j + '/sem_masks')
        os.mkdir(output_dir + j + '/inst_masks')
    except FileExistsError:
        pass
        
    
    for k in trange(images.shape[0], desc='Writing files for {}'.format(j), total=images.shape[0]):
        
        raw_image =  images[k,:,:,:].astype(np.uint8)
        raw_mask = masks[k,:,:,:]
        sem_mask = np.argmax(raw_mask, axis=-1).astype(np.uint8)
        # swaping channels 0 and 5 so that BG is at 0th channel
        sem_mask = np.where(sem_mask == 5, 6, sem_mask)
        sem_mask = np.where(sem_mask == 0, 5, sem_mask)
        sem_mask = np.where(sem_mask == 6, 0, sem_mask)

        tissue_type = types[k]
        instances = get_boundaries(raw_mask)
        
        # # for plotting it'll slow down the process considerabelly
        # fig, ax = plt.subplots(1, 3)
        # ax[0].imshow(instances)
        # ax[1].imshow(sem_mask)
        # ax[2].imshow(raw_image)
        
        # save file in op dir
        Image.fromarray(sem_mask).save(output_dir + '/{}/sem_masks/sem_{}_{}_{:05d}.png'.format(j, tissue_type, i+1, k)) 
        Image.fromarray(instances).save(output_dir +'/{}/inst_masks/inst_{}_{}_{:05d}.png'.format(j, tissue_type, i+1, k)) 
        Image.fromarray(raw_image).save(output_dir +'/{}/images/img_{}_{}_{:05d}.png'.format(j, tissue_type, i+1, k)) 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        