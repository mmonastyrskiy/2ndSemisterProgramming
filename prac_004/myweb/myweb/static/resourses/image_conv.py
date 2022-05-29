from PIL import Image
import os
for path,directory,names in os.walk("img"):
    for name in names:
        if name.endswith("png"):
            im1 = Image.open(os.path.join(path,name))
            idx = name.split(".")[0]
            rgb_im = im1.convert('RGB')
            rgb_im.save(os.path.join(path,idx+".jpg"))
        elif name.endswith("jpeg"):
            idx = name.split(".")[0]
            os.rename(os.path.join(path,name),os.path.join(path,idx+".jpg"))
