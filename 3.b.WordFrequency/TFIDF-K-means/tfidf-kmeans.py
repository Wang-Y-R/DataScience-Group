import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score
from collections import Counter

df = pd.read_excel('afterPreprocessed.xlsx')

words = [word for line in df['processed_result'] for word in line.split()]
word_freq = Counter(words)
standard = 20
high_freq_words = [word for word, freq in word_freq.items() if freq > standard]

# 构建TF-IDF矩阵
vectorizer = TfidfVectorizer(vocabulary=high_freq_words)
tfidf_matrix = vectorizer.fit_transform(df['processed_result'])

# 确定最佳聚类数
silhouette_scores = []
min_c = 2
max_c = 12
for n_clusters in range(min_c,max_c):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42).fit(tfidf_matrix)
    score = silhouette_score(tfidf_matrix, kmeans.labels_)
    silhouette_scores.append((n_clusters, score))

best_n_clusters = max(silhouette_scores, key=lambda x: x[1])[0]

# 执行K-means聚类
kmeans_best = KMeans(n_clusters=best_n_clusters, random_state=42)
kmeans_best.fit(tfidf_matrix)
df['cluster'] = kmeans_best.labels_

# 使用PCA进行降维
pca = PCA(n_components=2)  # 降维到2维
tfidf_pca = pca.fit_transform(tfidf_matrix.toarray())

# 绘制散点图
plt.figure(figsize=(10, 8))
colors = ['r', 'g', 'b', 'y', 'c', 'm', 'orange', 'purple', 'brown', 'pink']
for i in range(best_n_clusters):
    cluster_data = tfidf_pca[df['cluster'] == i]
    plt.scatter(cluster_data[:, 0], cluster_data[:, 1], s=50, c=colors[i % len(colors)], label=f'Cluster {i}')

plt.title('PCA of TF-IDF vectors with K-means Clustering')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend()
plt.grid(True)

# 保存散点图到本地
plt.savefig('clustering_plot.png')

# 显示散点图
plt.show()

# 将TF-IDF矩阵和聚类结果输出到Excel
tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out())
tfidf_df.to_excel('tfidf_matrix.xlsx', index=False)
df.to_excel('clustered_data.xlsx', index=False)

print("Done.")
