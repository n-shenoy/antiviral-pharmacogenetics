import pandas as pd

df = pd.read_excel("41586_2019_1793_MOESM3_ESM.xlsx", 
                    sheet_name = 'S4g-Pharmacogenomic SNPs',
                    header = 2, index_col = [0,1])
print(df)

df.reset_index(level = [0,1], inplace = True)
df.drop(labels=0, axis=0, inplace=True)
print(df)

df.to_csv('allele_frequencies.csv', index = False)