from bs4 import BeautifulSoup


# def myfun(tag):
#     return tag.is_empty_element

f1 = open("test_result2.csv", "w")
# with open("indigo2_automation_test_report_10-26-2020_15-52-14.html", "r") as f:
# with open("indigo2_automation_test_report_10-26-2020_19-52-22.html", "r") as f:
with open("indigo2_automation_test_report_10-26-2020_18-52-16.html", "r") as f:
    contents = f.read()
    soup = BeautifulSoup(contents, 'lxml')
    # tags = soup.find_all(myfun)
    # tags = soup.find_all(class_="results-table-row")

    # tags = soup.find(class_="results-table-row")
    # print(tags)
    count = 0
    for tb in soup.find_all(class_="results-table-row"):
        for row in tb.select('tbody tr')[:1]:
            # print(row)
            # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            # c = 0
            x = []
            for td in row.find_all('td')[:2]:
                # print(td)
                # print(td.text)
                x.append(td.text)
            # if x[1] == "Failed" or x[1] == "Skipped":
            if x[1] == "Failed":
                y = ",".join(x)
                print(y)
                f1.write(y+"\n")
                # print("@@@@@@@@@@@@@@@")
                # c += 1
                # if c >= 2:
                #     # print("xxxx")
                #     break
            count += 1
            # print("+++++++++++++++++++++++++++++")
            # break
            # if count >= 1:
            #     # print("vvvv")
            #     break

    # print(count)


