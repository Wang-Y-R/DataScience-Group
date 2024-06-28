import pandas as pd

# 指定Excel文件路径
excel_path = 'afterPreprocessed.xlsx'

# 读取Excel文件
xls = pd.ExcelFile(excel_path)

# 读取'Sheet1'工作表
df_sheet1 = pd.read_excel(xls, 'Sheet1')

# 读取词汇文件并按行分割，每行是一个词列表
with open('filter_words_or.txt', 'r', encoding='utf-8') as file:
    words_per_line = [line.strip().split() for line in file.readlines()]

# 创建一个空的DataFrame，用于存储符合条件的行
result_df = pd.DataFrame()

# 遍历每行的词列表
for words in words_per_line:
    # 使用布尔索引过滤包含任一词汇的行
    filtered_df = df_sheet1[df_sheet1['processed_result'].str.contains('|'.join(words), na=False)]
    # 将过滤后的DataFrame与之前的result_df合并
    result_df = pd.concat([result_df, filtered_df])

# 为每个词列表创建一个新的工作表
for i, words in enumerate(words_per_line, start=1):
    # 创建新的工作表名称
    new_sheet_name = f'Sheet_{i}_or'
    # 将包含这些词的行写入新的工作表
    with pd.ExcelWriter(excel_path, engine='openpyxl', mode='a') as writer:
        result_df[(result_df['processed_result'].str.contains('|'.join(words), na=False))].to_excel(writer, sheet_name=new_sheet_name, index=False)

print("Done.")