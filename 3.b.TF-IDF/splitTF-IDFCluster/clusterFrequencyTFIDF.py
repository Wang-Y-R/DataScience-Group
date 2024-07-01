import pandas as pd
import os
from collections import Counter

# 参数
directory = '.'
frequency_column = 'processed_result'
sheet_name = 'Sheet1'

# 获取当前目录下的所有xlsx文件
xlsx_files = [f for f in os.listdir(directory) if f.endswith('.xlsx')]

# 遍历当前目录下的所有xlsx文件
for filename in xlsx_files:
    # 构建文件的完整路径
    file_path = os.path.join(directory, filename)

    # 读取Excel文件的sheet1
    df = pd.read_excel(file_path, sheet_name=sheet_name)

    # 确保processed_result列存在
    if frequency_column in df.columns:
        # 对processed_result列进行词频统计
        text_data = ' '.join(df[frequency_column].str.lower())  # 将所有文本转换为小写并合并为一个字符串
        words = text_data.split()  # 分割字符串为单词列表
        word_counts = Counter(words)  # 计算词频

        # 将词频统计结果转换为DataFrame，并进行排序
        word_freq_df = pd.DataFrame(list(word_counts.items()), columns=['Word', 'Frequency'])
        word_freq_df = word_freq_df.sort_values(by='Frequency', ascending=False)

        # 将词频统计结果和原始数据保存到Excel的不同工作表
        with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists="overlay") as writer:
            df.to_excel(writer, sheet_name='Sheet1', index=False)
            word_freq_df.to_excel(writer, sheet_name='Word Frequency', index=False)

        print(f'Word frequency saved in {file_path}')
    else:
        print(f'processed_result column not found in {file_path}')

print('All files processed.')