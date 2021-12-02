"""
Bridging Composite and Real: Towards End-to-end Deep Image Matting [IJCV-2021]
Base Configurations class.

Copyright (c) 2021, Jizhizi Li (jili8515@uni.sydney.edu.au)
Licensed under the MIT License (see LICENSE for details)
Github repo: https://github.com/JizhiziLi/GFM
Paper link (Arxiv): https://arxiv.org/abs/2010.16188

"""

########## Root Paths and logging files paths
REPOSITORY_ROOT_PATH = ''
TRAIN_PATH = '/home/ubuntu/kartik/datasets/background-knockout-dataset-v15/'
VAL_PATH = '/home/ubuntu/kartik/datasets/test-dataset'
BG20K_DATASET_ROOT_PATH = ''
COCO_DATASET_ROOT_PATH = ''

TRAIN_LOGS_FOLDER = REPOSITORY_ROOT_PATH+'logs/train_logs/'
TEST_LOGS_FOLDER = REPOSITORY_ROOT_PATH+'logs/test_logs/'

# ######### Paths of datasets
DATASET_PATHS_DICT={
'AM2K':{
	'TRAIN':{
		'ROOT_PATH':TRAIN_PATH+'good_annos/',
		'ORIGINAL_PATH':TRAIN_PATH+'good_annos/fg/',
		'MASK_PATH':TRAIN_PATH+'good_annos/alpha/',
		'FG_PATH':TRAIN_PATH+'good_annos/fg/',
		'BG_PATH':TRAIN_PATH+'good_annos/bg/',
		'FG_DENOISE_PATH':'' + 'train/fg_denoise/',
		'SAMPLE_NUMBER':1800,
		'SAMPLE_BAGS':5
		},
	'VALIDATION':{
		'ROOT_PATH':VAL_PATH,
		'ORIGINAL_PATH':VAL_PATH+'images/',
		'MASK_PATH':VAL_PATH+'annotations/',
		'TRIMAP_PATH':''+'validation/trimap/',
		'SAMPLE_NUMBER':200,
		'SAMPLE_BAGS':1
		}
	},
'BG20K':{
	'TRAIN':{
		'ROOT_PATH': BG20K_DATASET_ROOT_PATH,
		'ORIGINAL_PATH': BG20K_DATASET_ROOT_PATH+'train/',
		'ORIGINAL_DENOISE_PATH': BG20K_DATASET_ROOT_PATH+'train_denoise/',
		},
	'TESTVAL':{
		'ROOT_PATH': BG20K_DATASET_ROOT_PATH,
		'ORIGINAL_PATH': BG20K_DATASET_ROOT_PATH+'testval/',
		}
	},
'COCO':{
	'TRAIN':{
	'ROOT_PATH': COCO_DATASET_ROOT_PATH,
	'ORIGINAL_PATH': COCO_DATASET_ROOT_PATH+'train_bg/',
		}
	}
}

########## Parameters for training, 
# might need a little playing around as well to 
# get the right config
CROP_SIZE = [640, 960, 1280]
# CROP_SIZE = [320, 480, 640]
RESIZE_SIZE = 320
TRAIN_DEBUG_FOLDER = REPOSITORY_ROOT_PATH+'results/debug/'

########## Parameters for testing
MAX_SIZE_H = 1600
MAX_SIZE_W = 1600
SHORTER_PATH_LIMITATION=1080
# SAMPLES_ORIGINAL_PATH = REPOSITORY_ROOT_PATH+'samples/original/'
SAMPLES_ORIGINAL_PATH = '/home/ubuntu/kartik/datasets/test-dataset/images/'
SAMPLES_RESULT_ALPHA_PATH = REPOSITORY_ROOT_PATH+'samples/test_800_alpha/'
SAMPLES_RESULT_COLOR_PATH = REPOSITORY_ROOT_PATH+'samples/test_800_color/'