import pandas as pd
from collections import Counter
import sys
import os

# Obtain Excel file path from command line parameters
if len(sys.argv) > 1:
    excel_path = sys.argv[1]
else:
    raise ValueError("Please provide the Excel file path as a command line argument.")

sheet_name = 'Sheet1'
frequency_column = 'processed_result'

# read
df = pd.read_excel(excel_path, sheet_name=sheet_name)

# check
if frequency_column not in df.columns:
    raise ValueError("The target column is not found in the Excel file.")

df['unique_words'] = df[frequency_column].apply(lambda x: set(x.split()))

all_unique_words = [word for words in df['unique_words'] for word in words]
word_counts = Counter(all_unique_words)

word_freq_df = pd.DataFrame(list(word_counts.items()), columns=['Word', 'Frequency'])

word_freq_df = word_freq_df.sort_values(by='Frequency', ascending=False)

word_freq_df_filtered = word_freq_df[word_freq_df['Frequency'] >= 20]

base_name = os.path.splitext(os.path.basename(excel_path))[0]

new_excel_name = f"WF_{base_name}.xlsx"

word_freq_df_filtered.to_excel(new_excel_name, index=False)

print(f"Word frequency has been saved to {new_excel_name}")