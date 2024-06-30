import pandas as pd
from collections import Counter
import os
from pathlib import Path
import sys

# 从命令行参数获取文件夹路径
if len(sys.argv) > 1:
    folder_path = sys.argv[1]
else:
    raise ValueError("Please provide the folder path as a command line argument.")

# 确保WF文件夹存在
WF_path = os.path.join(folder_path, 'WF')
os.makedirs(WF_path, exist_ok=True)

# 遍历文件夹中的所有Excel文件
for file_name in os.listdir(folder_path):
    if file_name.endswith('.xlsx') or file_name.endswith('.xls'):
        excel_path = os.path.join(folder_path, file_name)
        sheet_name = 'Sheet1'  # 假设每个Excel文件的第一个工作表名称为Sheet1

        # 读取Excel文件
        df = pd.read_excel(excel_path, sheet_name=sheet_name)

        # 检查'processed_result'列是否存在
        if 'processed_result' not in df.columns:
            print(f"The 'processed_result' column is not found in {file_name}, skipping.")
            continue

        # 对每个单元格中的词语进行去重
        df['unique_words'] = df['processed_result'].apply(lambda x: set(x.split()))

        # 提取所有去重后的词语并进行词频统计
        all_unique_words = [word for words in df['unique_words'] for word in words]
        word_counts = Counter(all_unique_words)

        # 将词频统计结果转换为DataFrame
        word_freq_df = pd.DataFrame(list(word_counts.items()), columns=['词语', '词频'])

        # 按词频降序排序
        word_freq_df = word_freq_df.sort_values(by='词频', ascending=False)

        word_freq_df_filtered = word_freq_df[word_freq_df['词频'] >= 20]

        # 构造新的Excel文件名
        new_excel_name = f"WF_{os.path.splitext(file_name)[0]}.xlsx"
        new_excel_path = os.path.join(WF_path, new_excel_name)

        # 保存词频统计结果到Excel文件
        word_freq_df_filtered.to_excel(new_excel_path, index=False)

        print(f"Word frequency for {file_name} has been saved to {new_excel_path}")