import pandas as pd
from collections import Counter

# 指定Excel文件路径
excel_path = 'afterPreprocessed.xlsx'

# 读取Excel文件
xls = pd.ExcelFile(excel_path)

# 通过命令行输入指定工作表名称
sheet_name = input("请输入要统计词频的工作表名称: ")

# 读取指定的工作表
df = pd.read_excel(excel_path, sheet_name=sheet_name)

# 假设processed_result列已经是分词后的结果
# 将分词结果合并为一个列表，每个元素是一个分词后的词语
words_list = df['processed_result'].sum().split()

# 使用Counter统计词频
word_freq = Counter(words_list)

# 将统计结果转换为DataFrame
word_freq_df = pd.DataFrame(list(word_freq.items()), columns=['词语', '词频'])

# 按词频从大到小排序
word_freq_df = word_freq_df.sort_values(by='词频', ascending=False)

# 生成新工作表的名称
new_sheet_name = f"{sheet_name}_词频统计结果"

# 将词频统计结果写入新的工作表
with pd.ExcelWriter(excel_path, engine='openpyxl', mode='a') as writer:
    word_freq_df.to_excel(writer, sheet_name=new_sheet_name, index=False)

print("Done.")