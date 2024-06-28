from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
import numpy as np

# 加载Sentence-Bert模型
model = SentenceTransformer('all-MiniLM-L6-v2')

# 准备句子数据
sentences = [
    "洗发水","Hello"
]

# 提取句子向量
sentence_embeddings = model.encode(sentences)
print(sentence_embeddings)
# 使用K-means聚类
num_clusters = 5
kmeans = KMeans(n_clusters=num_clusters)
kmeans.fit(sentence_embeddings)
clusters = kmeans.labels_

# 打印聚类结果
for i, sentence in enumerate(sentences):
    print(f"Sentence: '{sentence}' - Cluster: {clusters[i]}")