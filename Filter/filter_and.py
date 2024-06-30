import pandas as pd

# 读取筛选词文件
excel_path = 'afterPreprocessed.xlsx'
with open('filter_words_and.txt', 'r', encoding='utf-8') as file:
    my_words = [line.strip().split() for line in file if line.strip()]

# 读取原始Excel文件
df = pd.read_excel(excel_path, sheet_name='Sheet1')

# 检测所有词是否都出现
def contains_all_terms(s, terms):
    return all(term in s for term in terms)

# 遍历筛选词列表
for terms in my_words:
    # 筛选包含所有词的行
    filtered_df = df[df['processed_result'].apply(lambda x: contains_all_terms(x, terms))]

    # 如果筛选结果不为空
    if not filtered_df.empty:
        # 生成新的Excel文件名
        new_excel_name = f'afterFiltered_{"_".join(terms)}.xlsx'
        # 将筛选结果写入新的Excel文件
        filtered_df.to_excel(new_excel_name, index=False)

print("Done")