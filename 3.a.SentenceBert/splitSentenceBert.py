import pandas as pd
import os

# 指定参数
subfolder_name = 'splitSentenceBertCluster'
excel_path = 'sentenceBertResult14.xlsx'
cluster_column = 'finalGroup'
saved_column = ['id','category','severity','recurrent','fusionResult', 'preProcessedResult']

if not os.path.exists(subfolder_name):
    os.makedirs(subfolder_name)

df = pd.read_excel(excel_path)

# 确定聚类的数量
unique_clusters = df[cluster_column].unique()

print('Splitting.')

# 为每个聚类创建一个新的Excel文件在子文件夹中
for cluster_id in unique_clusters:
    # 筛选出属于当前聚类的行，并保留result和processed_result列
    cluster_df = df[df[cluster_column] == cluster_id][saved_column]

    # 定义新文件的名称和路径
    new_file_name = f'{subfolder_name}/cluster_{cluster_id}.xlsx'

    # 保存到Excel
    cluster_df.to_excel(new_file_name, index=False)

    print(f'Saved as {new_file_name}')

print('Done.')