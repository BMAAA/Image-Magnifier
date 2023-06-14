import os
from PIL import Image, ImageDraw
from os import listdir

x_need, y_need = [int(i) for i in input().split()]
# get files from
folder_dir = "Input images"
if not os.path.exists("Input images") or \
        list(filter(lambda i: i.endswith(".png") or i.endswith(".jpg") or i.endswith(".jpeg"),
                    os.listdir(folder_dir))) == []:  # Check files in "Input images" folder
    _ = input("There are no images in the 'Input Images' folder!\nPress 'Enter' to exit. ")
    exit()
for images in list(filter(lambda i: i.endswith(".png") or i.endswith(".jpg") or i.endswith(".jpeg"),
                          os.listdir(folder_dir))):
    # working with image
    im = Image.open(folder_dir + "/" + images)
    x, y = im.size
    n = get_mult(x, y, , y_need)
    n = min(x_need // x, y_need // y)
    im1 = Image.new('RGBA', (int(x) * n, int(y) * n), (255, 255, 255, 0))
    data = im.getdata()
    newdata = []
    for i in range(y):
        for _ in range(n):
            for j in range(x):
                newdata += [data[i * x + j]] * n

    # save new image
    im1.putdata(newdata)
    im1.save(f"Output images/{images}")
    print(images)
