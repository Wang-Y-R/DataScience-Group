import os
import pandas as pd
from zhipuai import ZhipuAI

# 设置API Key
api_key = "bdb681f6d86e26fa9256a759b6a5b3fa.cdo7Th4FhpV1UcRG"

analysis_column = 'result'

# 创建ZhipuAI客户端
client = ZhipuAI(api_key=api_key)

# 获取当前目录下所有的.xlsx文件
xlsx_files = [f for f in os.listdir('.') if f.endswith('.xlsx')]

# 遍历所有xlsx文件
for xlsx_file in xlsx_files:
    # 读取Excel文件
    df = pd.read_excel(xlsx_file, sheet_name='Sheet1')
    results = df[analysis_column].tolist()  # 获取result列的所有数据

    # 将result列中的所有内容使用换行符拼接为一个问题
    complete_question = "这是一份软件测试报告，请分析以下内容集中体现的问题：\n" + "\n".join(str(item) for item in results)

    # 准备发送给API的消息
    message = {
        "role": "user",
        "content": complete_question
    }

    # 发送请求并获取结果
    response = client.chat.completions.create(
        model="glm-4",  # 使用glm-4模型
        messages=[message],
        stream=False,
    )

    # 检查response是否包含choices，然后获取消息文本
    if response.choices and len(response.choices) > 0:
        response_message = response.choices[0].message.content if hasattr(response.choices[0].message, 'content') else response.choices[0].message
    else:
        response_message = "No response received."

    # 定义输出文件名，与Excel文件同名但扩展名为.txt
    output_filename = os.path.splitext(xlsx_file)[0] + '.txt'

    # 将响应结果写入到文本文件中
    with open(output_filename, 'w', encoding='utf-8') as file:
        file.write(response_message)

    print(f"Saved as {output_filename}")