# CaltechPreprocess       

## 0.Environment
```        
python3.6  
lxml==4.5.0
numpy==1.18.2
opencv-python==4.2.0.34
scipy==1.4.1
```           
      
## 1.download.sh下载数据集  
### windows下，在git Bash中运行
解压后，标签放到data目录下，图像文件放到data/images/目录下                
`
./download.sh
`            

## 2.run convert_seq_to_jpg     
### convert seq to jpg by this command(all seq):     
`python3 convert_seq_to_jpg.py`     
### image文件名格式如下：
```
data下文件夹名称_seq文件名_第几帧图像.jpg 
set00_V000_0.jpg        
```        
### image所在目录文件树：   
```           
└─data
    └─images
        └─set00
           │  V000.seq
           │  ...
           │  V014.seq
           │  
           └─images
                  set00_V000_0.jpg
                  set00_V000_1.jpg
                       ...
                  set00_V014_999.jpg
```      
 
## 3.run rename_jpg.py      
### change the image name by this command(all images):    
`
python3 rename_jpg.py
`       
### 并将图像复制到指定目录下:     
```
└─data
    └─images
        └─set00
           │  V000.seq
           │  ...
           │  V014.seq
           │  
           └─images
                  set00_V000_000000.jpg
                  set00_V000_000001.jpg
                       ...
                  set00_V014_000999.jpg
```     


```   
set00_V014_999.jpg
to
set00_V014_000999.jpg

```             

## 4.run vbb2voc.py     
### get label file(.xml) by this command(all vbb to xml):      
`
python3 vbb2voc.py
`   
### xml所在目录文件树：     
```
└─data
    └──VOCdevkit/VOC2007 
        └──Annotations
           └─set00_V000_000068.xml
                    ...
             set00_V014_000999.xml

```        
### xml文件内容参考     
```       
<annotation>
  <folder>VOC2014_instance/person</folder>
  <filename>set00_V000_000068.jpg</filename>
  <source>
    <database>Caltech pedestrian</database>
    <annotation>Caltech pedestrian</annotation>
    <image>Caltech pedestrian</image>
    <url>None</url>
  </source>
  <size>
    <width>640</width>
    <height>480</height>
    <depth>3</depth>
  </size>
  <segmented>0</segmented>
  <object>
    <name>person</name>
    <bndbox>
      <xmin>212.98989163622238</xmin>
      <ymin>141.3955255819699</ymin>
      <xmax>217.71129943876736</xmax>
      <ymax>150.27347293552876</ymax>
    </bndbox>
    <difficult>0</difficult>
    <occlusion>0</occlusion>
  </object>
</annotation>
```        

## 5.run find_xml_with_jpg.py     
### 找到xml对应的jpg文件使用如下命令：
`python3 find_xml_with_jpg.py`     
### image所在目录文件树：         
```      
└─data
    └──VOCdevkit/VOC2007 
        └──JPEGImages
           └─set00_V000_000068.jpg
                      ...
             set00_V014_000999.jpg

```     
       
## 6.visualize box run find_xml_with_jpg.py    
`python3 visualize_bbox.py`        
<img src="https://github.com/gmt710/CaltechPreprocess/blob/master/gif/visbox.gif" width="640" height="480"/>       
          
## 7.run generete_txt.py           
使用generete_txt.py生成训练集与测试集：         
`python3 generete_txt.py`          
输出：                       
```       
train and val size 61439
train size 53760
test size 60748
Time taken : 15.824258804321289 seconds
```         
             
## 8.final file structure        
data中的文件是下载下载的数据文件，由于文件过大，所以需要我们自己准备。         
```       
CaltechPreprocess
│  convert_seq_to_jpg.py
│  download.sh
│  file.txt
│  find_xml_with_jpg.py
│  generate_txt.py
│  README.md
│  rename_jpg.py
│  requirements.txt
│  vbb2voc.py
│  visualize_bbox.py
│  voc文件名.png
│  voc文件树.png
│      
├─data
│  ├─annotations
│  │  ├─set00
│  │  │      V000.vbb
│  │  │         ...
│  │  │      V014.vbb
│  │  │      
│  │  ├─set01
│  │  │  ...     
│  │  └─set10
│  │          
│  ├─images
│  │  ├─set00
│  │  │  │  V000.seq
│  │  │  │     ...
│  │  │  │  V014.seq
│  │  │  │  
│  │  │  └─images
│  │  ├─set01
│  │  │  ...
│  │  └─set10
│  │      
│  └─VOCdevkit/VOC2007
│      │  
│      ├─Annotations
│      │  │          
│      │  │         
│      │  └─set00_V000_000068.xml
│      │            ...
│      │    set00_V014_001910.xml
│      ├─JPEGImages
│      │   │   		
│      │   │  
│      │   └─ set00_V000_000068.jpg
│      │            ...
│      │      set00_V014_001910.jpg            
│      └─ImageSets
│          │  
│          └─Main
│              └─trainval.txt
│                train.txt
│                test.txt
│                val.txt
├─gif
│      org.gif
│      visbox.gif
│      
└─venv

```          
         
## reference           
1.[caltect_dataset_convert](https://github.com/DanLiu0623/caltect_dataset_convert)      
2.[Caltech行人数据集转为VOC数据集](https://www.jianshu.com/p/e6882c96ffad)     
3.[CaltechPestrain2VOC](https://github.com/shadowwalker00/CaltechPestrain2VOC)     
            
          