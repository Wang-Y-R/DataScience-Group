import os

# 获取当前目录下的所有md文件
md_files = [f for f in os.listdir('.') if f.endswith('.md')]

# 创建或覆盖clusters.md文件
with open('clusters.md', 'w', encoding='utf-8') as clusters_file:
    # 遍历md文件列表
    for md_file in md_files:
        # 读取md文件内容
        with open(md_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # 获取文件名（不包含扩展名）并创建二级标题
        title = os.path.splitext(md_file)[0]
        header = f'## {title}\n'

        # 将标题添加到文件内容的开头
        new_content = [header] + lines

        # 将新内容写入clusters.md
        clusters_file.writelines(new_content)
        clusters_file.write('\n')  # 添加空行以分隔不同的文件内容

print('All md files have been processed and merged into clusters.md')