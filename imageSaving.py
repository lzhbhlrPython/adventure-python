import hashlib
import base64
import json
import os
from PIL import Image

# 打开二进制文件，将她的哈希校验值和base64值和格式以json格式储存到内存
def save_to_memory(file_path):
    # 打开文件
    with open(file_path, 'rb') as f:
        file_content = f.read()
        # 计算哈希值
        file_hash = hashlib.sha256(file_content).hexdigest()
        # 将文件内容转换为 base64 编码
        file_base64 = base64.b64encode(file_content).decode()
        # 获取文件后缀名
        file_format = os.path.splitext(file_path)[1][1:]
        # 将信息储存在内存中
        data = {'hash': file_hash, 'base64': file_base64, 'format': file_format}
        return json.dumps(data)


def save_to_image(data, image_path):
    # 将数据转换为字节流
    data_bytes = base64.b64encode(json.dumps(data).encode())
    # 补齐字节流
    num_padding = 3 - len(data_bytes) % 3
    if num_padding != 3:
        data_bytes += b'\x00' * num_padding
    # 将字节流转换为像素点
    pixels = [(data_bytes[i], data_bytes[i+1], data_bytes[i+2]) for i in range(0, len(data_bytes), 3)]
    # 补齐图片使它成为一个正方形
    size = int(len(pixels)**0.5)
    if size**2 < len(pixels):
        size += 1
    # 创建新图像
    img = Image.new('RGB', (size, size))
    # 填充像素点
    img.putdata(pixels)
    # 保存图像到本地
    img.save(image_path)




def read_from_image(image_path):
    # 读取图像
    img = Image.open(image_path)
    # 遍历像素点
    pixels = img.getdata()
    # 获取字节流
    file_bytes = b''.join([bytes(p) for p in pixels])
    # 去除末尾的空像素
    while file_bytes[-1:] == b'\x00':
        file_bytes = file_bytes[:-1]
    # 将字节流转换为 base64 编码
    file_base64 = file_bytes.decode()
    file=base64.b64decode(file_base64).decode() 
    #去除file首尾的引号,并去除中间的`\`
    file=file[1:-1]
    file=file.replace('\\','')
    # 将信息转换为 JSON 格式
    data = json.loads(file)
    return data





def save_to_file(data, file_path):
    # 获取文件内容的 base64 编码
    file_base64 = data['base64']
    # 将 base64 编码转换为字节流
    file_bytes = base64.b64decode(file_base64)
    # 检验哈希是否正确
    if hashlib.sha256(file_bytes).hexdigest() != data['hash']:
        return False
    # 自动添加文件后缀名
    file_path = file_path if file_path.endswith(data['format']) else file_path + '.' + data['format']
    # 将字节流保存到新文件中
    with open(file_path, 'wb') as f:
        f.write(file_bytes)
    return True

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 4:
        print('Usage: python3 imageSaving.py <input file> <output file> <mode>')
        exit(0)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    mode = sys.argv[3]
    if mode == 'binary':
        data = save_to_memory(input_file)
        save_to_image(data, output_file)
        print('Image saved successfully')
    elif mode == 'image':
        data = read_from_image(input_file)
        if save_to_file(data, output_file):
            print('File saved successfully')
    else:
        print('Unknown mode: {}'.format(mode))

