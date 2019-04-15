python test.py --name baseline_256 \
--label_nc 35 --loadSize 256 --n_scales_spatial 3 \
--fg --n_downsample_G 2 --use_single_G \
--dataroot datasets/Cityscapes_turning_car/ \
--custom_model checkpoints/baseline_256/latest_net_G0.pth
