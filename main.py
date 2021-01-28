# import glob2
# import math
# import os
# import numpy as np
#
# files = []
# for ext in ["*.png", "*.jpeg", "*.jpg"]:
#     image_files = glob2.glob(os.path.join("data/", ext))
#     files += image_files
#
# print(len(files))
# nb_val = math.floor(len(files) * 0.2)
# rand_idx = np.random.randint(0, len(files), nb_val)
#
# # Tạo file train.txt
# a = 0
# for idx in np.arange(len(files)):
#         a = a + 1
# print(a)
#
# a = 0
# # Tạo file vali.txt
# for idx in np.arange(len(files)):
#     if idx in rand_idx:
#         a = a + 1
#
# print(a)

# import glob2
# import numpy as np
# import os
#
# all_files = []
# for ext in ["*.png", "*.jpeg", "*.jpg"]:
#     images = glob2.glob(os.path.join("data/", ext))
#     all_files += images
#
# rand_idx = np.random.randint(0, len(all_files), 20)
#
# a = 0
# # Create train.txt
# for idx in np.arange(len(all_files)):
#     a = a + 1
# print(a)
#
# a = 0
# # Create valid.txt
# for idx in np.arange(len(all_files)):
#     if idx in rand_idx:
#         a = a + 1
# print(a)

# import glob2
# import numpy as np
# import os
#
# all_files = []
# for ext in ["*.png", "*.jpeg", "*.jpg"]:
#     images = glob2.glob(os.path.join("data/", ext))
#     all_files += images
#
# rand_idx = np.random.randint(0, len(all_files), 20)
#
# # Create train.txt
# with open("train.txt", "w") as f:
#     for idx in np.arange(len(all_files)):
#         # if idx not in rand_idx:
#         f.write(all_files[idx] + '\n')
#
# # Create valid.txt
# with open("valid.txt", "w") as f:
#     for idx in np.arange(len(all_files)):
#         if idx in rand_idx:
#             f.write(all_files[idx] + '\n')


# Step 6. Tạo file train.txt và val.txt
import glob2
import math
import os
import numpy as np

files = []
for ext in ["*.png", "*.jpeg", "*.jpg"]:
    image_files = glob2.glob(os.path.join("thienGray/", ext))
    for img in image_files:
        if os.path.exists(img[:-3] + "txt"):
            files.append(img)

# files = []
# for ext in ["*.png", "*.jpeg", "*.jpg"]:
#     image_files = glob2.glob(os.path.join("thienGray/", ext))
#     files += image_files


nb_val = math.floor(len(files) * 0.2)
rand_idx = np.random.choice(len(files), size=nb_val, replace=False)
train_idx = [x for x in np.arange(len(files)) if x not in rand_idx]

print(rand_idx)
print(train_idx)

print(len(files))
print(len(train_idx))
print(len(rand_idx))

# Tạo file train.txt
with open("train.txt", "w") as f:
    for idx in np.arange(len(files)):
        if (os.path.exists(files[idx][:-3] + "txt")):
            f.write(files[idx] + '\n')

# Tạo file vali.txt
with open("val.txt", "w") as f:
    for idx in np.arange(len(files)):
        if (idx in rand_idx) and (os.path.exists(files[idx][:-3] + "txt")):
            f.write(files[idx] + '\n')
