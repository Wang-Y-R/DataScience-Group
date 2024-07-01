import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score
from collections import Counter

excel_path = 'afterPreprocessed.xlsx'
sheet_name = 'Sheet1'
target_column = 'processed_result'
frequency_standard = 10
min_cluster = 2
max_cluster = 15
saved_matrix = f'TFIDFMatrix{frequency_standard}.xlsx'


df = pd.read_excel(excel_path, sheet_name=sheet_name)

words = [word for line in df[target_column] for word in line.split()]
word_freq = Counter(words)
high_freq_words = [word for word, freq in word_freq.items() if freq > frequency_standard]

# 构建TF-IDF矩阵
print('Building TF-IDF Matrix.')
vectorizer = TfidfVectorizer(vocabulary=high_freq_words)
tfidf_matrix = vectorizer.fit_transform(df[target_column])

# 确定最佳聚类数
silhouette_scores = []
for n_clusters in range(min_cluster,max_cluster):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42).fit(tfidf_matrix)
    score = silhouette_score(tfidf_matrix, kmeans.labels_)
    silhouette_scores.append((n_clusters, score))

best_n_clusters = max(silhouette_scores, key=lambda x: x[1])[0]

saved_cluster = f'TF-IDFClusterData{best_n_clusters}.xlsx'
saved_plot = f'TF-IDFClusterData{best_n_clusters}.png'

# 执行K-means聚类
print('Performing K-means clustering.')
kmeans_best = KMeans(n_clusters=best_n_clusters, random_state=42)
kmeans_best.fit(tfidf_matrix)
df['cluster'] = kmeans_best.labels_

# 使用PCA进行降维
pca = PCA(n_components=2)  # 降维到2维
tfidf_pca = pca.fit_transform(tfidf_matrix.toarray())

# 绘制散点图
print('Drawing a scatter plot.')
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
plt.savefig(saved_plot)

# 显示散点图
plt.show()

# 将TF-IDF矩阵和聚类结果输出到Excel
tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out())
tfidf_df.to_excel(saved_matrix, index=False)
df.to_excel(saved_cluster, index=False)

print("Done.")
