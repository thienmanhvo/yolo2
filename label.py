from datetime import datetime

import glob2
import math
import os
import numpy as np
from shutil import copyfile
import re
import cv2


# os.walk("crohme")
#
# dir_list = next(os.walk("crohme"))[1]
#
# print(dir_list)


# now = now.replace(":", "_")
# now = now.replace("-", "_")
# now = now.replace(" ", "_")
# now = now.replace(".", "_")


def label():
    a = -1
    dirs = next(os.walk("crohme"))[1]
    for dir in dirs:
        a = a + 1
        b = 0
        for filename in os.listdir(f"crohme/{dir}"):
            b = b + 1
            if (filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png")) and b <= 250:
                extention = filename[-3:]
                now = re.sub('[^0-9]', '_', str(datetime.now()))
                copyfile(f"crohme/{dir}/{filename}", f"data/{filename[:-4]}_{str(now)}.{extention}")
                with open(f"data/{filename[:-4]}_{str(now)}.txt", "w") as f:
                    f.write(f"{a} 0.511111 0.511111 0.977778 0.977778")


def ImgToGray():
    for filename in os.listdir(f"thien"):
        img = cv2.imread(f'thien/{filename}')
        bw_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(f'thienGray/{filename}', bw_img)


def GrayToThreash():
    for filename in os.listdir(f"thien"):
        img = cv2.imread(f'thien/{filename}', 0)
        bw_img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
        cv2.imwrite(f'thienGray/{filename}', bw_img)


ImgToGray()


def class_yolo():
    dirs = next(os.walk("data/crohme"))[1]
    with open(f"data/class.txt", "w") as f:
        for data in dirs:
            f.writelines(f'{data}\n')


def copy():
    dirs = next(os.walk("crohme"))[1]
    for dir in dirs:
        b = 0
        for filename in os.listdir(f"crohme/{dir}"):
            b = b + 1
            if (filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(
                    ".png") or filename.endswith(".txt")) and b <= 500:
                extention = filename[-3:]
                now = re.sub('[^0-9]', '_', str(datetime.now()))
                # print(f'{filename[:-4]}_{str(now)}.{extention}')
                copyfile(f"crohme/{dir}/{filename}", f"data/{filename[:-4]}_{str(now)}.{extention}")


def count():
    a = 0
    for filename in os.listdir(f"data"):
        a = a + 1
    print(a)


def count_in_crohme():
    dirs = next(os.walk("crohme"))[1]
    a = 0
    for dir in dirs:
        for filename in os.listdir(f"crohme/{dir}"):
            if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(
                    ".png") or filename.endswith(".txt"):
                a = a + 1
    print(a)


def copy2():
    dirs = next(os.walk("crohme"))[1]
    for dir in dirs:
        for filename in os.listdir(f"crohme/{dir}"):
            if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(
                    ".png") or filename.endswith(".txt"):
                extention = filename[-3:]
                now = re.sub('[^0-9]', '_', str(datetime.now()))
                # print(f'{filename[:-4]}_{str(now)}.{extention}')
                copyfile(f"crohme/{dir}/{filename}", f"data/{filename[:-4]}_{str(now)}.{extention}")

# copy()
# label()
