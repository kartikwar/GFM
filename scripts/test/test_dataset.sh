#/bin/bash

###########################
## Arch and model_path 
###########################
# backbone: r34 | rosta: TT | model_path: models/pretrained/gfm_r34_tt.pth
# backbone: r34 | rosta: FT | model_path: models/pretrained/gfm_r34_ft.pth
# backbone: r34 | rosta: BT | model_path: models/pretrained/gfm_r34_bt.pth
# backbone: r34_2b | rosta: TT | model_path: models/pretrained/gfm_r34_2b_tt.pth
# backbone: d121 | rosta: TT | model_path: models/pretrained/gfm_d121_tt.pth
# backbone: r101 | rosta: TT | model_path: models/pretrained/gfm_r101_tt.pth

backbone='r34'
rosta='TT'
model_path='models/pretrained/gfm_r34_tt.pth'
dataset_choice='AM_2K'
test_choice='HYBRID'
pred_choice=3
test_result_dir='results/am2k_gfm_r34_tt/'
nickname='am2k_gfm_r34_tt'

python core/test.py \
	 --cuda \
     --backbone=$backbone \
     --rosta=$rosta \
     --model_path=$model_path \
     --test_choice=$test_choice \
     --dataset_choice=$dataset_choice \
     --pred_choice=$pred_choice \
     --test_result_dir=$test_result_dir \
     --logname=$nickname \