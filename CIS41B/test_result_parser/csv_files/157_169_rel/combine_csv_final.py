import os
import glob
import pandas as pd

# os.chdir("/Users/jakkus/PycharmProjects/CIS41B/test_result_parser/csv_files/157_169_rel")

os.chdir("/Users/jakkus/PycharmProjects/CIS41B/test_result_parser/1027_debug")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

# combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
# export to csv
combined_csv.to_csv("157_169_combined_csv.csv", index=False, encoding='utf-8-sig')


