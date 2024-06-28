import pandas as pd

excel_path = 'afterPreprocessed.xlsx'

with open('filter_words_and.txt', 'r', encoding='utf-8') as file:
    my_words = [line.split() for line in file]  

df = pd.read_excel(excel_path, sheet_name='Sheet1')


def contains_all_terms(s, terms):
    return all(term in s for term in terms)


for terms in my_words:

    filtered_df = df[(df['processed_result'].apply(lambda x: contains_all_terms(x, terms)))]


    if not filtered_df.empty:

        new_sheet_name = f'Sheet_{"_".join(terms)}_and'

        with pd.ExcelWriter(excel_path, engine='openpyxl', mode='a') as writer:
            filtered_df.to_excel(writer, sheet_name=new_sheet_name, index=False)

print("Done")