import cv2
import numpy as np
import os



def sad_calculation(alpha_path, sal_path):
    alpha = cv2.imread(alpha_path, 0) / 255.
    origin_pred_mattes = cv2.imread(sal_path, cv2.IMREAD_UNCHANGED)[:, :, 3] / 255.

    #done to avoid cuda out of error issue
    alpha = cv2.resize(alpha, (500,500))
    origin_pred_mattes = cv2.resize(origin_pred_mattes, (500, 500))

    assert(alpha.shape == origin_pred_mattes.shape)

    mse_diff = ((origin_pred_mattes - alpha) ** 2).sum()
    sad_diff = np.abs(origin_pred_mattes - alpha).sum()



    print(sad_diff)

    return sad_diff, mse_diff



if __name__ == '__main__':
    mse_diffs = 0
    sad_diffs = 0

    alpha_dir = '/home/ubuntu/kartik/datasets/test-dataset/annotations'
    sal_dir = '/home/ubuntu/kartik/GFM/samples/test_800_color'

    cnt = len(os.listdir(alpha_dir))

    for idx, alpha_path in enumerate(os.listdir(alpha_dir)):
        # sal_path = alpha_path.replace('.jpg', '_sal_fuse.png')
        print(idx)
        sal_path = alpha_path.replace('.jpg', '.png')
        alpha_path = os.path.join(alpha_dir, alpha_path)
        sal_path = os.path.join(sal_dir, sal_path)
        sad_diff, mse_diff = sad_calculation(alpha_path, sal_path)
        mse_diffs += mse_diff
        sad_diffs += sad_diff

    print('final sad is ')
    print(sad_diffs/cnt)

    # if args.testAlphaDir != '':
    #     logger.info("Eval-MSE: {}".format(mse_diffs / cnt))
    #     logger.info("Eval-SAD: {}".format(sad_diffs / cnt))
    # return sad_diffs / cnt


    pass