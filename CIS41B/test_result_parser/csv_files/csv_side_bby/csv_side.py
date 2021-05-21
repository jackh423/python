# # Read files
# data_1 = pd.read_csv(file1.csv)
# data_2 = pd.read_csv(file2.csv)
# data_3 = pd.read_csv(file3.csv)
#
# # Assuming the name A for the first column of each csv is not a typo
# data_2.rename(columns={'A': 'B'})
# data_3.rename(columns={'A': 'C'})
#
# # Order columns
# new_columns = []
# for i in range(len(data_1.columns):
#     new_columns.extend([data_1.columns[i], data_2.columns[i], data_3.columns[i]])
#
# # Concatenate dataframes
# data_out = pd.concat([data_1, data_2, data_3], axis=1)
#
# # Reorder columns
# data_out = data_out[new_columns]

import pandas as pd
data1 = pd.read_csv("test_result.csv")
data2 = pd.read_csv("test_result2.csv")
result = pd.merge(data1, data2, on='ID')
# result.columns = ['ID', 'Status', 'ID', 'Status']
result.columns = ['ID', 'Status', 'Status']
result[['ID', 'Status', 'Status']]
result.to_csv("combine1.csv", index=False)
