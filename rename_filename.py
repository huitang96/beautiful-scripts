#修改filename属性，并从文件名

import os
import os.path
import xml.dom.minidom
path = 'D:\\data\\testmap\\xml'
files = os.listdir(path)  # 得到文件夹下所有文件名称
s = []
count = 0
for xmlFile in files:  # 遍历文件夹
    if not os.path.isdir(xmlFile):  # 判断是否是文件夹,不是文件夹才打开
            name1 = xmlFile.split('.')[0]
            dom = xml.dom.minidom.parse(path + '\\' + xmlFile)
            root = dom.documentElement
            newfolder = root.getElementsByTagName('folder')
            newpath = root.getElementsByTagName('path')
            newfilename = root.getElementsByTagName('filename')
         #   newfolder[0].firstChild.data = 'VOCdevkit\VOC2012\JPEGImages'
     #       newpath[0].firstChild.data = 'VOCdevkit\VOC2012\JPEGImages' + '\\' + name1 + '.jpg'
            newfilename[0].firstChild.data = name1 + '.jpg'
            with open(os.path.join(path, xmlFile), 'w') as fh:
                dom.writexml(fh)
#                print('写入name/pose OK!')
            count = count + 1


