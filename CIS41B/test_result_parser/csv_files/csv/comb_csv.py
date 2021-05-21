import os

# csv_header = 'Timestamp,Client IP,Web Service,Status,Good,Bad'
csv_header = 'case_id, status'
csv_out = 'consolidated.csv'

csv_dir = os.getcwd()

dir_tree = os.walk(csv_dir)
for dirpath, dirnames, filenames in dir_tree:
   pass

csv_list = []
for file in filenames:
   if file.endswith('.csv'):
      csv_list.append(file)

csv_merge = open(csv_out, 'w')
csv_merge.write(csv_header)
csv_merge.write('\n')

print(csv_list)
for file in csv_list:
   csv_in = open(file)
   for line in csv_in:
      if line.startswith(csv_header):
         continue
      print(line)
      csv_merge.write(line)
   csv_in.close()
csv_merge.close()
print('Verify consolidated CSV file : ' + csv_out)