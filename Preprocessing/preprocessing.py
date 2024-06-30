import pandas as pd
import jieba

def process_and_filter(text):

    min = 5

    if not isinstance(text, str):
        text = str(text)

    if pd.isnull(text) or text == '':
        return None
    words = [word for word in jieba.cut(text) if word not in stopwords]

    if len(words) < min:
        return None
    return ' '.join(words)


try:
    with open('my_stopwords.txt', 'r', encoding='utf-8') as file:
        stopwords = set([line.strip() for line in file])
except FileNotFoundError:
    print("Stopwords not found")
    stopwords = set()


df = pd.read_excel('afterFusion.xlsx')


df['processed_result'] = df['result'].apply(process_and_filter)


df = df.dropna(subset=['processed_result'])


df.to_excel('afterPreprocessed.xlsx', index=False)