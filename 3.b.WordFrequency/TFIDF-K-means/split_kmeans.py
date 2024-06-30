import pandas as pd
import os

# 指定参数
subfolder_name = 'split_cluster'
excel_path = 'clustered_data.xlsx'
cluster_column = 'cluster'
saved_column = ['result', 'processed_result']

# 如果子文件夹不存在，创建它
if not os.path.exists(subfolder_name):
    os.makedirs(subfolder_name)

# 读取Excel文件
df = pd.read_excel(excel_path)

# 确定聚类的数量
unique_clusters = df[cluster_column].unique()

# 为每个聚类创建一个新的Excel文件在子文件夹中
for cluster_id in unique_clusters:
    # 筛选出属于当前聚类的行，并保留result和processed_result列
    cluster_df = df[df[cluster_column] == cluster_id][saved_column]

    # 定义新文件的名称和路径
    new_file_name = f'{subfolder_name}/{cluster_column}_{cluster_id}.xlsx'

    # 保存到Excel
    cluster_df.to_excel(new_file_name, index=False)

    print(f'Saved as {new_file_name}')

print('Done.')