import pandas as pd

# 读取筛选词文件
with open('filter_words_or.txt', 'r', encoding='utf-8') as file:
    my_words = [line.split() for line in file]

# 读取原始Excel文件
excel_path = 'afterPreprocessed.xlsx'
df = pd.read_excel(excel_path, sheet_name='Sheet1')

# 修改函数，使其检测到任意一个词出现
def contains_any_term(s, terms):
    return any(term in s for term in terms)

# 遍历筛选词列表
for terms in my_words:
    # 筛选包含任意一个词的行
    filtered_df = df[df['processed_result'].apply(lambda x: contains_any_term(x, terms))]

    # 如果筛选结果不为空
    if not filtered_df.empty:
        # 生成新的Excel文件名
        new_excel_name = f'afterFiltered_{"_".join(terms)}.xlsx'
        # 将筛选结果写入新的Excel文件
        filtered_df.to_excel(new_excel_name, index=False, header=True)

print("Done")