import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# 读取Excel文件
df = pd.read_excel('afterPreprocessed.xlsx')

# 假设分词后的结果存储在'processed_result'列
if 'processed_result' not in df.columns:
    raise ValueError("Excel文件中没有找到'processed_result'列，请检查列名是否正确。")

# 使用TfidfVectorizer生成TF-IDF矩阵
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df['processed_result'])

# 将TF-IDF矩阵转换为DataFrame
tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out())

# 将TF-IDF矩阵保存为Excel文件
tfidf_df.to_excel('tfidf_matrix.xlsx', index=True)  # 设置index=True以保存行索引