python train.py --name depth_label_256 \
--label_nc 35 --loadSize 256 --fg --use_depth_as_labels \
--n_downsample_G 2 --num_D 1 \
--max_frames_per_gpu 3 --n_frames_total 6 \
--dataroot datasets/full_Cityscapes/
