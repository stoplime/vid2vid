import os
from sewar.full_ref import mse, rmse, psnr, ssim, uqi, msssim, ergas, scc, rase, sam, vifp
import cv2
import numpy as np
import tqdm
import pprint

PATH = os.path.abspath(os.path.dirname(__file__))

gt_img_path = "/home/stoplinux/Pictures/Depth_turing_car/epoch002_real_image.png"
pred_img_path = "/home/stoplinux/Pictures/Depth_turing_car/epoch002_fake_image.png"

metrics = {
    "mse": mse,
    "rmse": rmse,
    "psnr": psnr,
    "ssim": ssim,
    "uqi": uqi,
    # "msssim": msssim,
    "ergas": ergas,
    "scc": scc,
    "rase": rase,
    "sam": sam,
    "vifp": vifp
}

metric_keys = list(metrics.keys())

results = {}
    
    
if __name__ == "__main__":
    gt_img = cv2.imread(gt_img_path, -1)
    pred_img = cv2.imread(pred_img_path, -1)
    print("gt_img", gt_img.shape)
    print("pred_img", pred_img.shape)

    for metric in metric_keys:
        print(metric)
        results[metric] = metrics[metric](gt_img, pred_img)
    
    pprint.pprint(results)
