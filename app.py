from PIL import Image ,ImageEnhance,ImageFilter
import os
path='./imges'
pathOut='/editImages'
for filename in os.listdir(path):
    img=Image.open(f'{path}/{filename}')
    edit=img.filter(ImageFilter.SHARPEN).convert('L').rotate(-90)
    clean_name=os.path.splitext(filename)[0]
    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')
