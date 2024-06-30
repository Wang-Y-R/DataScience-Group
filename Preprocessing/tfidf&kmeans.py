import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import LabelEncoder
from collections import Counter

df = pd.read_excel('afterPreprocessed.xlsx')

words = []
for line in df['processed_result']:
    words.extend(line.split())

word_freq = Counter(words)

# 筛选词频大于标准的词语
standard = 20
high_freq_words = [word for word, freq in word_freq.items() if freq > standard]

# 构建TF-IDF矩阵
vectorizer = TfidfVectorizer(vocabulary=high_freq_words)
tfidf_matrix = vectorizer.fit_transform(df['processed_result'])

# 确定最佳聚类数
silhouette_scores = []
min_c = 2
max_c = 11
for n_clusters in range(min_c, max_c):  # 尝试2到10个聚类
    kmeans = KMeans(n_clusters=n_clusters, random_state=42).fit(tfidf_matrix)
    score = silhouette_score(tfidf_matrix, kmeans.labels_)
    silhouette_scores.append((n_clusters, score))

# 选择具有最高轮廓系数的聚类数
best_n_clusters = max(silhouette_scores, key=lambda x: x[1])[0]

# 根据最佳聚类数重新执行K-means聚类
kmeans_best = KMeans(n_clusters=best_n_clusters, random_state=42)
kmeans_best.fit(tfidf_matrix)
df['cluster'] = kmeans_best.labels_

# 将TF-IDF矩阵转换为DataFrame
tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out())

# 将TF-IDF矩阵和聚类结果输出到Excel
tfidf_df.to_excel('tfidf_matrix.xlsx', index=False)
df.to_excel('clustered_data.xlsx', index=False)

print("Done.")