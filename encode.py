from PIL import Image
import numpy as np
import os
import math
import gzip

fn=input("输入文件名>>>")
print("加密中。。。")
szzz=48
fnlll=48
fnnn=os.path.basename(fn).encode("utf8")
if len(fnnn)<fnlll:
    fnnn+=b"\x00"*(fnlll-len(fnnn))
else:
    raise Exception("文件名太长啦")

with open(fn,"rb") as f:
    fffff=gzip.compress(f.read(),9)
    fsize=len(fffff)
    _fs=fsize+szzz+fnlll
    size=int(math.sqrt(_fs//4+(1 if _fs%4 else 0)))+1
    pic=np.zeros((size,size,4),dtype=np.uint8)
    content=fsize.to_bytes(szzz,"big")+fnnn+fffff
    ln=0
    col=0
    rgba=-1
    for b in content:
        if rgba<3:
            rgba+=1
        else:
            rgba=0
            if col<size-1:
                col+=1
            else:
                col=0
                if ln<size-1:
                    ln+=1
                else:
                    raise Exception("出大问题了QAQ")
        pic[ln][col][rgba]=b
    Image.fromarray(pic.astype('uint8')).save("result.png")