import os
import cv2
import glob

if __name__ == '__main__':
	vis_flag = 0
	xml_path = './data/VOCdevkit/VOC2007/Annotations/'
	out_path = './data/VOCdevkit/VOC2007/JPEGImages/'

	if not os.path.exists(out_path):
		os.makedirs(out_path)
	for file in os.listdir(xml_path):
		print(file.strip('.xml'))
		filename = file.strip('.xml') + '.jpg'
		filename1 = file.strip('.xml')[0:5]
		img_path = './data/images/' + filename1 + '/images/'
		print(img_path)
		img = cv2.imread(os.path.join(img_path, filename))
		# if img is None:
		# 	break
		cv2.imwrite(os.path.join(out_path, filename), img)
		if vis_flag:
			cv2.imshow('img', img)
			cv2.waitKey(1)
# #指定set**
# import os
# import cv2
# path = './data/VOC2014_instance/annotations/set00/bbox/'
# img_path = './data/VOC2014_instance/JPEGImages/set00/'
# out_path = './data/VOC2014_instance/JPEGImages/'
# if not os.path.exists(out_path):
# 	os.makedirs(out_path)
# # print os.listdir(path)
# vis_flag = 0
#
# for file in os.listdir(path):
# 	print(file.strip('.xml'))
# 	filename = file.strip('.xml') + '.jpg'
# 	print(filename)
# 	img = cv2.imread(os.path.join(img_path, filename))
# 	cv2.imwrite(os.path.join(out_path, filename), img)
# 	if vis_flag:
# 		cv2.imshow('img',img)
# 		cv2.waitKey(1)

