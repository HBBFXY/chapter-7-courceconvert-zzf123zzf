import keyword

# 读取原文件内容
with open('random_int.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 获取Python所有保留字（关键字）
keywords = set(keyword.kwlist)
result = []
i = 0
n = len(content)

while i < n:
    # 识别单词（由字母、数字、下划线组成）
    if content[i].isalpha():
        start = i
        # 提取完整单词（包含字母、数字、下划线）
        while i < n and (content[i].isalnum() or content[i] == '_'):
            i += 1
        word = content[start:i]
        # 非保留字则将小写转为大写
        if word not in keywords:
            word = word.upper()
        result.append(word)
    else:
        # 非字母字符直接保留
        result.append(content[i])
        i += 1

# 拼接处理后的内容
new_content = ''.join(result)

# 保存到新文件
with open('random_int_converted.py', 'w', encoding='utf-8') as f:
    f.write(new_content)# 在这个文件中编写代码实现题目要求的功能
import keyword  # 建议使用这个库处理关键字
reserved_words = set(keyword.kwlist)

# 以下内容自行完成
