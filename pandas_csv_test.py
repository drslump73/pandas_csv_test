# CSV Example

# sep=;
# ;HOG;HOG;HOG;Day 1;Day 1;Day 1;Day 2;Day 2;Day 2;Day 3;Day 3;Day 3; ...
# date;ios;android;total;ios;android;total;ios;android;total;ios;android;total; ...
# 2017/07/25;12,758;4,771;17,529;4,334;1,798;6,132;2,670;1,201;3,871;2,241;1,029;3,270; ...
#

import pandas as pd

df = pd.read_csv('./test.csv',sep=';',header=2,thousands=',')

del_cols = []
for i in range(1, len(df.columns)):
    if (i % 3 != 0):
        del_cols.append(i)

df = df.drop(df.columns[del_cols],axis=1)
df = df.drop(df.columns[0], axis=1)

df = df.drop(df.columns[len(df.index):], axis=1)

column_sums = []

for i in range(len(df.columns)):
    column_sums.append(int(df[df.columns[i]].sum()))
    
','.join([str(v) for v in column_sums])

first_column = [int(v) for v in df[df.columns[0]].tolist()]
','.join([str(v) for v in first_column])