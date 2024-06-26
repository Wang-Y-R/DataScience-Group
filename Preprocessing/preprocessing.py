#根据第一次分词结果, 增加了停用词列表一些词, 放在了my_stopwords.txt的最前面.
import pandas as pd
import jieba

with open('my_stopwords.txt', 'r', encoding='utf-8') as file:
    stopwords = set([line.strip() for line in file])

df = pd.read_excel('afterFusion.xlsx')

def process_text(text):
    if pd.isnull(text) or not isinstance(text, str):
        return ''
    
    words = jieba.cut(str(text))
    
    filtered_words = ' '.join([word for word in words if word not in stopwords])
    
    return filtered_words if filtered_words else ''


df['processed_result'] = df['result'].apply(process_text)

df.to_excel('afterPreprocessed.xlsx', index=False)