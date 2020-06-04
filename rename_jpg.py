import os
import glob
# import cv2 as cv

#set00_V014_001884.xml
# path = './data/images/set00'
# # print os.listdir(path)
# for folder in os.listdir(path):
# 	# print folder
# 	foldername = folder.split('\\')
# 	# print  os.listdir(os.path.join(path, folder))
# 	for file in os.listdir(os.path.join(path, folder)):
# 		dstname = foldername[0] + '_' + foldername[1] + '_' + file
# 		dst = os.path.join(path, dstname)
# 		src = os.path.join(path, folder, file)
# 		os.rename(src, dst)


if __name__ == '__main__':
    for dname in sorted(glob.glob('./data/images/set*')):
        print(dname)
        # 输出图片位置
        dname1 = os.path.split(dname)[1]
        # jpg_outdir = "./data/VOC2014_instance/JPEGImages/" +dname1+"/"
        jpg_outdir = "./data/images/" + dname1 + '/images/'
        if not os.path.exists(jpg_outdir):
            os.makedirs(jpg_outdir)
        for fn in sorted(glob.glob('{}/images/*.jpg'.format(dname))):
            print(fn)
            src_dir, src_name = os.path.split(fn)
            print(src_dir)
            src_name1 = src_name.split(".")[0]
            a0, a1, a2 = src_name1.split("_")
            a2 = a2.zfill(6)
            a = a0 + "_" + a1 + "_" + a2 + ".jpg"
            src_name = src_dir + "/" + src_name
            dst_name = jpg_outdir + a
            os.rename(src_name, dst_name)
