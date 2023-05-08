import os
from PIL import Image, ImageDraw
from os import listdir


def get_mult(x, y, x1, y1):  # x, y - size of the original image; x1, y1 - minimum required image size
    n = 1
    while x * n < x1 or y * n < y1:
        n += 1
    return n


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
    data = im.getdata()
    x, y = im.size
    n = get_mult(x, y, x_need, y_need)
    newdata = []
    im1 = Image.new('RGBA', (int(x) * n, int(y) * n), (255, 255, 255, 0))
    pixels, pixels1 = im.load(), ImageDraw.Draw(im)
    for i in range(y):
        for _ in range(n):
            for j in range(x):
                newdata += [data[i * x + j]] * n

    # save new image
    im1.putdata(newdata)
    im1.save(f"Output images/{images}")
    print(images)
