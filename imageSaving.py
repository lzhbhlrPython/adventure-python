import hashlib
import base64
import json
from PIL import Image

Image.MAX_IMAGE_PIXELS = 2300000000

# 打开二进制文件，将她的哈希校验值和base64值和格式以json格式储存到内存
def save_to_memory(file_path):
    # 打开文件
    with open(file_path, 'rb') as f:
        file_content = f.read()
        # 计算哈希值
        file_hash = hashlib.sha256(file_content).hexdigest()
        # 将文件内容转换为 base64 编码
        file_base64 = base64.b64encode(file_content).decode()
        # 将信息储存在内存中
        data = {'hash': file_hash, 'base64': file_base64, 'format': 'binary'}
        return json.dumps(data)

def save_to_image(data, image_path):
    # 从内存中获取信息
    data = json.loads(data)
    # 将 base64 编码转换为字节流
    file_bytes = base64.b64decode(data['base64'])
    # 补齐字节流
    num_padding = 3 - len(file_bytes) % 3
    if num_padding != 3:
        file_bytes += b'\x00' * num_padding
    # 将字节流转换为像素点
    pixels = [(file_bytes[i], file_bytes[i+1], file_bytes[i+2]) for i in range(0, len(file_bytes), 3)]
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
    # 将字节流转换为 base64 编码
    file_base64 = base64.b64encode(file_bytes).decode()
    # 将信息转换为 JSON 格式
    data = {'hash': '', 'base64': file_base64, 'format': 'binary'}
    return json.dumps(data)

def save_to_file(data, file_path):
    # 从 JSON 格式中获取信息
    data = json.loads(data)
    # 将 base64 编码转换为字节流
    file_bytes = base64.b64decode(data['base64'])
    # 去除末尾的空像素
    while file_bytes[-1:] == b'\x00':
        file_bytes = file_bytes[:-1]
    # 将字节流保存到新文件中
    with open(file_path, 'wb') as f:
        f.write(file_bytes)
    # 计算新文件的哈希值
    new_hash = hashlib.sha256(file_bytes).hexdigest()
    # 检验哈希是否正确
    if new_hash == data['hash']:
        return True
    else:
        return False


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
    elif mode == 'image':
        data = read_from_image(input_file)
        save_to_file(data, output_file)
    else:
        print('Unknown mode: {}'.format(mode))
