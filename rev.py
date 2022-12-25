import random
import time

random.seed(time.time())

# 获取用于生成伪随机数的梅森旋转算法函数的逆函数
def inverse_mt19937(output):
    # 将伪随机数转换为二进制字符串
    output_binary = bin(output)[2:]
    # 补充到32位
    output_binary = '0' * (32 - len(output_binary)) + output_binary
    # 解码二进制字符串为整数
    state = [int(output_binary[i:i+32], 2) for i in range(0, len(output_binary), 32)]
    # 返回种子值
    return state[0]

# 生成伪随机数序列
random_sequence = [random.randint(0, 2**32-1) for _ in range(10)]

# 反推种子值
seed = inverse_mt19937(random_sequence[0])

# 验证反推的种子值是否正确
while True:
    print(seed)
    if seed == random_sequence[0]:
        print('Success!')
        break
    else:
        seed = inverse_mt19937(seed)
        
