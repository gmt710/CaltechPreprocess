import os
import glob
import cv2 as cv


# 保存图片以指定名字到指定位置
def save_img(dname, fn, i, frame):
    cv.imwrite('{}/{}_{}_{}.jpg'.format(
        out_dir, os.path.basename(dname),
        os.path.basename(fn).split('.')[0], i), frame)


if __name__ == '__main__':
    # seq文件位置
    for dname in sorted(glob.glob('./data/images/set*')):
        # 输出图片位置
        out_dir = dname + '/images/'
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        for fn in sorted(glob.glob('{}/*.seq'.format(dname))):
            cap = cv.VideoCapture(fn)
            i = 0
            while True:
                # ret为标志位，bool型，是否读到数据，frame为视频帧图像数据
                ret, frame = cap.read()
                if not ret:
                    break
                save_img(dname, fn, i, frame)
                i += 1
            print(fn)
