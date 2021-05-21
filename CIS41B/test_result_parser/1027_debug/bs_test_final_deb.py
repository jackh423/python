from bs4 import BeautifulSoup
import os
import glob

in_file_ext ="html"
all_file_names = [i for i in glob.glob('*.{}'.format(in_file_ext))]

print(all_file_names)
# file_ext_count = 0
# file_beg = "test_result"
# out_file =
# f1 = open(f"{file_beg}{file_ext_count}.csv", "w")
f1 = open("final_test_result3.csv", "w")
for file in all_file_names:
    print(file)
    # file_ext_count += 1
    f1.write(file+","+"Result\n")
    with open(file, "r") as f:
        contents = f.read()
        soup = BeautifulSoup(contents, 'lxml')
        for tb in soup.find_all(class_="results-table-row"):
            for row in tb.select('tbody tr')[:1]:
                x = []
                for td in row.find_all('td')[:2]:
                    x.append(td.text)
                # if x[1] == "Failed" or x[1] == "Skipped":
                # if x[1] == "Failed":
                if x[1] == "Failed" or x[1] == "Skipped" or x[1] == "Passed":
                    y = ",".join(x)
                    print(y)
                    f1.write(y+"\n")
        # f1.write("x,x\n")



