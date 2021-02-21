import glob

import camelot
import pandas as pd

path = r'Docs'
all_files = glob.glob(path + "/*.pdf")

for file in all_files:

    tables = camelot.read_pdf(file, pages='all')
    tabela = list()
    name = file.split('.')[-2]
    name = name.split('\\')[-1]

    for i, tb in enumerate(tables):
        tabela.append(tables[i].df)
    colunas = ['Nº', 'AUTOR', 'EMENTA/PARECER']
    dataframe = pd.concat([*tabela])
    dataframe = dataframe.drop_duplicates()
    dataframe = dataframe.iloc[2:]
    dataframe.columns = colunas
    dataframe.to_csv(f'{path}/result/{name}.csv', encoding='utf-8-sig', sep=',', index=False, header=1)
