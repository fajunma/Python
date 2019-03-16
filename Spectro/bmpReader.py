
from PIL import Image
img = Image.open('Demo.bmp')
img_array = img.load()

for i in range(7):
    t = []
    for j in range(10):
        t.append('{:0>3d}'.format(img_array[j, i][0]))
    print(t)


