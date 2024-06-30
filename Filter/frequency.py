import pandas as pd
from collections import Counter
import sys
import os

# 从命令行参数获取Excel文件路径
if len(sys.argv) > 1:
    excel_path = sys.argv[1]
else:
    raise ValueError("Please provide the Excel file path as a command line argument.")

sheet_name = 'Sheet1'

# 读取Excel文件
df = pd.read_excel(excel_path, sheet_name=sheet_name)

# 检查'processed_result'列是否存在
if 'processed_result' not in df.columns:
    raise ValueError("The 'processed_result' column is not found in the Excel file.")

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

# 从原文件路径中提取文件名（不包含扩展名）
base_name = os.path.splitext(os.path.basename(excel_path))[0]

# 构造新的Excel文件名
new_excel_name = f"WF_{base_name}.xlsx"

# 保存词频统计结果到Excel文件
word_freq_df_filtered.to_excel(new_excel_name, index=False)

print(f"Word frequency has been saved to {new_excel_name}")