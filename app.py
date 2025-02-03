import pandas as pd
ds = pd.read_csv('assets/real_estate.csv', sep=';')
df = pd.DataFrame(ds)
new_df = df.groupby(['level5']).count()
loc_max = new_df.loc[new_df['isNew'].idxmax()]
print(loc_max)