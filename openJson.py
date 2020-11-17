import json
# fileName = 'detection_val.json'
# savePath = 'test/'
fileName = 'detection_train.json'
savePath = 'train/'
# fileName = 'detection_all.json'

with open(fileName) as f:
    f = json.load(f)
    # print(f.keys())
    # dict_keys(['images', 'annotations', 'categories']
    images = f['images']
    # {'file_name': '118024.jpg', 'height': 2336, 'width': 4160, 'id': 7578, 'scene': 'None'}
    annotations = f['annotations']
    # {'image_id': 7578, 'category_id': 4, 'id': 60756, 'bbox': [2356.0, 29.0, 1059.0, 2288.0], 'iscrowd': 0, 'area': 2422992.0, 'ignore': 0, '_ignore': 0}
    categories  = f['categories']
    # {'supercategory': 'normal', 'id': 1, 'name': 'door'}
    # just select one


    # 1. set the category_id

    for cat in categories:
        category_id = cat['id']
        new_json_name = savePath+cat['name'] + '.json'
        
        newJson = {}
        category=[cat]
        newJson['categories'] = categories        

        # 2. Use category_id add annotations and images
        imgs = []
        annotation = []
        for img in images:
            imgID = img['id']
            # decide this imgID has right categories
            imgIDflag = False 
            for ann in annotations:
                if ann['image_id'] == imgID and ann['category_id'] == category_id:
                    annotation.append(ann)
                    # print('annotation')
                    # print(ann)
                    imgIDflag = True
            if imgIDflag:
                imgs.append(img)
                # print('images')
                # print(img)
        newJson['images'] = imgs
        newJson['annotations'] = annotation

        # print(str(cat['id'])+' '+cat['name']+ ' ' +str(len(imgs)) + ' ' + str(len(annotation)))
        print('%-5s'% str(cat['id']) + '%-20s'%cat['name'] + '%-10s'%str(len(imgs)) + '%-10s'%str(len(annotation)))
        file = open(new_json_name, 'w', encoding='utf-8')
        json.dump(newJson, file)
        print('save '+ new_json_name)
    print('Done')


'''
annotations  
    'images_id'   对应 'images'   中的ID
    'category_id' 对应 'category' 中的ID
'''
