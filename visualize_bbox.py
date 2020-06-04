#-*- coding:utf-8 -*-
import os, glob
from lxml import etree


def visualize_bbox(xml_file, img_file):
    import cv2
    tree = etree.parse(xml_file)
    # load image
    image = cv2.imread(img_file)
    # get bbox
    for bbox in tree.xpath('//bndbox'):
        coord = []
        for corner in bbox.getchildren():
            coord.append(int(float(corner.text)))
        print(coord)
        # draw rectangle
        # coord = [int(x) for x in coord]
        cv2.rectangle(image, (coord[0], coord[1]), (coord[2], coord[3]), (0, 0, 255), 2)
    # visualize image
    cv2.imshow("img", image)
    cv2.waitKey(1)


def vis_org():
    import cv2
    test_file = open('./2007_test.txt')
    lines = test_file.readlines()
    for line in lines:
        print(line.split()[0])
        img_file = line.split()[0]
        image = cv2.imread(img_file)
        cv2.imshow("img", image)
        cv2.waitKey(1)

    # for img_file in sorted(glob.glob('{}/*.jpg'.format("./data/VOCdevkit/VOC2007/JPEGImages/"))):
    #     # img_file = "./data/VOCdevkit/VOC2007/JPEGImages/set00_V000_000258.jpg"
    #     image = cv2.imread(img_file)
    #     cv2.imshow("img", image)
    #     cv2.waitKey(1)


def vis_single():
    xml_file = "./data/VOCdevkit/VOC2007/Annotations/set00_V000_000258.xml"
    img_file = "./data/VOCdevkit/VOC2007/JPEGImages/set00_V000_000258.jpg"
    visualize_bbox(xml_file, img_file)


def vis_batch():
    for xml_file in sorted(glob.glob('{}/*.xml'.format("./data/VOCdevkit/VOC2007/Annotations/"))):
        filename = os.path.splitext(os.path.split(xml_file)[1])[0]
        img_file = "./data/VOCdevkit/VOC2007/JPEGImages/" + str(filename) + ".jpg"
        print(img_file)
        visualize_bbox(xml_file, img_file)


if __name__ == '__main__':
    vis_flag = 1
    vis_orgflag = 1
    if vis_orgflag:
        vis_org()
    else:
        if vis_flag:
            vis_batch()
        else:
            vis_single()
