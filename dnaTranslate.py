def bytes_to_dna(data: bytes) -> str:
    """将字节数据转换成 DNA 碱基序列"""
    # 将字节数据转换成二进制字符串
    binary_str = "".join(f"{b:08b}" for b in data)
    # 将二进制字符串按两位分组
    groups = [binary_str[i:i+2] for i in range(0, len(binary_str), 2)]
    # 将每组二进制数转换成对应的 DNA 碱基
    dna = "".join(
        "A" if group == "00" else
        "C" if group == "01" else
        "G" if group == "10" else
        "T" for group in groups
    )
    return dna

def dna_to_bytes(dna: str) -> bytes:
    """将 DNA 碱基序列转换成字节数据"""
    # 将 DNA 碱基序列转换成二进制数字符串
    binary_str = "".join(
        "00" if base == "A" else
        "01" if base == "C" else
        "10" if base == "G" else
        "11" for base in dna
    )
    # 将二进制数字符串转换成字节数据
    data = bytes(int(binary_str[i:i+8], 2) for i in range(0, len(binary_str), 8))
    return data

def complement_dna(dna_strand):
    # 建立碱基互补对应关系的字典
    base_pairs = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    
    # 建立空字符串，用于存储互补的碱基序列
    complement_strand = ''
    
    # 遍历DNA单链的碱基序列
    for base in dna_strand:
        # 根据碱基互补对应关系，查找互补的碱基
        complement_base = base_pairs[base]
        # 将互补的碱基加入互补的碱基序列中
        complement_strand += complement_base
    
    # 返回互补的碱基序列
    return complement_strand
