# coding:utf-8
# 下面代码包含json格式的ground-truth和predict画框

# --------------------------------------------------------------ground-truth 
from pycocotools.coco import COCO
import cv2
import json
categories = [{"id": 0, "name": "pedestrian"},
            {"id": 1, "name": "people"},
            {"id": 2, "name": "bicycle"},
            {"id": 3, "name": "car"},
            {"id": 4, "name": "van"},
            {"id": 5, "name": "truck"},
            {"id": 6, "name": "tricycle"},
            {"id": 7, "name": "awning-tricycle"},
            {"id": 8, "name": "bus"},
            {"id": 9, "name": "motor"} ]   

def select(json_path, outpath, image_path):
    json_file = open(json_path)
    infos = json.load(json_file)
    images = infos["images"]
    annos = infos["annotations"]
    assert len(images) == len(images)
    for i in range(len(images)):
        im_id = images[i]["id"]
        im_path = image_path + images[i]["file_name"]
        img = cv2.imread(im_path)
        for j in range(len(annos)):
            if annos[j]["image_id"] == im_id:
                x, y, w, h = annos[j]["bbox"]
                x, y, w, h = int(x), int(y), int(w), int(h)
                x2, y2 = x + w, y + h
                category_id = categories[annos[j]["category_id"]]['name']
                # import pdb; pdb.set_trace()
                cv2.putText(img, category_id, (x,y-5), cv2.FONT_HERSHEY_DUPLEX , 0.6, (0,0,0))
                # object_name = annos[j][""]
                img = cv2.rectangle(img, (x, y), (x2, y2), (255, 0, 0), thickness=2)
                img_name = outpath + images[i]["file_name"]
                cv2.imwrite(img_name, img)
                # continue
        # print(i)

if __name__ == "__main__":
    # imageidFile = ''
    json_path = '/home/htang/datasets/visdrone2020/coco/VisDrone2019-DET-val/VisDrone2019-DET_val_coco.json'
    image_path = '/home/htang/datasets/visdrone2020/coco/VisDrone2019-DET-val/images/'
    outpath = '/home/htang/datasets/visdrone2020/coco/VisDrone2019-DET-val/checkjson/'
    select(json_path, outpath, image_path)

# --------------------------------------------------------------------------predict
'''
from pycocotools.coco import COCO
import cv2
import json
import os
categories = [{"id": 1, "name": "pedestrian"},
            {"id": 2, "name": "people"},
            {"id": 3, "name": "bicycle"},
            {"id": 4, "name": "car"},
            {"id": 5, "name": "van"},
            {"id": 6, "name": "truck"},
            {"id": 7, "name": "tricycle"},
            {"id": 8, "name": "awning-tricycle"},
            {"id": 9, "name": "bus"},
            {"id": 10, "name": "motor"} ]   

def select(json_path, outpath, image_path):
    json_file = open(json_path)
    infos = json.load(json_file)
    for i in range(len(infos)):
        out_path = outpath + infos[i]["image_id"] + ".jpg"
        im_path = image_path + infos[i]["image_id"] + ".jpg"
        # import pdb; pdb.set_trace()
        if infos[i]["score"] > 0.5:
            if os.path.exists(out_path):
                img = cv2.imread(out_path)
            else:
                img = cv2.imread(im_path)
            x, y, w, h = infos[i]["bbox"]
            x, y, w, h = int(x), int(y), int(w), int(h)
            x2, y2 = x + w, y + h
            category_id = categories[infos[i]["category_id"] - 1]['name']
            cv2.putText(img, category_id, (x,y-5), cv2.FONT_HERSHEY_DUPLEX , 0.6, (0,0,0))
            img = cv2.rectangle(img, (x, y), (x2, y2), (255, 0, 0), thickness=2)
            cv2.imwrite(out_path, img)


if __name__ == "__main__":
    # imageidFile = ''
    json_path = '/home/htang/datasets/visdrone2020/coco/VisDrone2019-DET-val/VisDrone2019-DET_val_coco.json'
    image_path = '/home/htang/datasets/visdrone2020/coco/VisDrone2019-DET-val/images/'
    outpath = '/home/htang/datasets/visdrone2020/coco/VisDrone2019-DET-val/checkjson/'
    select(json_path, outpath, image_path)
'''