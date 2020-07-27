import cv2
import numpy as np
import gzip
import time

fn=input("输入文件名>>>")
print("解码中。。。")
t0=time.time()

pic=cv2.imread(fn,-1)

def main():
    content_=[]
    for n in np.nditer(pic):
        content_.append(n.tobytes())
    return b''.join(content_)

content=main()
print(time.time()-t0)

szzz=48
fnlll=48
length=int.from_bytes(content[:szzz+fnlll],"big")
final=content[szzz+fnlll:szzz+fnlll+length]
fn="_"+content[szzz:szzz+fnlll].decode().replace("\x00","")

with open(fn,"wb") as ffff:
    ffff.write(gzip.decompress(final))