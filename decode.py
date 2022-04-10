from PIL import Image
import numpy as np
import gzip

Image.MAX_IMAGE_PIXELS=None #解除像素数上限以读取大图片

input_file_name=input("输入文件>>>")
output_directory=(lambda s:"./" if not s else s)(input("输出目录（不填默认当前目录）>>"))
print("解码中。。。")

pic=np.array(Image.open(input_file_name))
content=pic.tobytes()
del pic

size_bytes_length=48
filename_length=48
main_content_addr=size_bytes_length+filename_length

output_file_name="_"+content[size_bytes_length:main_content_addr].decode().replace("\x00","")

length=int.from_bytes(content[:main_content_addr],"big")
main_content=content[main_content_addr:main_content_addr+length]

with open(output_directory+output_file_name,"wb") as f:
    f.write(gzip.decompress(main_content))