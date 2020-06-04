# -*- coding:utf-8 -*-
"""
generate_txt.py
将Caltech行人数据集set00-set05分为训练集(trainval 61439)，
set06-set10分为测试集(test 60748)

划分为trainval,train,val,test.
trainval按照4:1将数据划分为train,val
"""
#
import os
import random
import time
import glob

xmlfilepath = "./data/VOCdevkit/VOC2007/Annotations"
saveBasePath = "./data/VOCdevkit/VOC2007/ImageSets/Main"
if not os.path.exists(saveBasePath):
    os.makedirs(saveBasePath)

ftrainval = open(os.path.join(saveBasePath, 'trainval.txt'), 'w')
ftest = open(os.path.join(saveBasePath, 'test.txt'), 'w')
ftrain = open(os.path.join(saveBasePath, 'train.txt'), 'w')
fval = open(os.path.join(saveBasePath, 'val.txt'), 'w')

total_xml = os.listdir(xmlfilepath)
num = len(total_xml)      #xml文件的数量
trainval_percent = 1
train_percent = 0.8



if __name__ == '__main__':
    num_trainval = 0
    num_train = 0
    num_val = 0
    num_test = 0
    # Start time
    start = time.time()
    for fn in sorted(glob.glob('{}/*.xml'.format(xmlfilepath))):
        print(fn)
        src_dir, src_name = os.path.split(fn)
        name = os.path.splitext(src_name)[0] + '\n'
        if int(src_name[3:5]) <= 5:
            ftrainval.write(name)
            num_trainval = num_trainval + 1
            if (num_trainval // int(train_percent*10)) % int(train_percent*10):
                ftrain.write(name)
                num_train = num_train + 1
            else:
                fval.write(name)
                num_val = num_val + 1
        else:
            ftest.write(name)
            num_test = num_test + 1

    ftrainval.close()
    ftrain.close()
    fval.close()
    ftest.close()

    # End time
    end = time.time()
    seconds = end - start
    print("train and val size {} \ntrain size {}\ntest size {}"
          .format(num_trainval, num_train, num_test))
    print("Time taken : {0} seconds".format(seconds))

