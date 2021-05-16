#
# import timeit
# import pdb
#
# quote = "Believe you can and you're halfway there."
# a_indexes = [i for i, ltr in enumerate(quote) if ltr == 'a']
# #print(a_indexes)
# # pdb.set_trace()
# # a_i = [quote.index(ia) for ia in quote if ia == 'a']
# # print(f"a_i: {a_i}")
# #pos = quote.find('a', 0)
# #print(f"pos: {pos}")
# #print(type(pos))
# #pos1 = quote.find('a', pos+1)
# #print(f"pos1: {pos1}")
# #pos2 = quote.find('a', pos1+1)
# #print(f"pos2: {pos2}")
# pos = 0
# index_list = []
# #print(len(quote))
# #pos = quote.find('a', pos)
# loop_count = 0
# #print(f"pos:{pos}")
# while pos <= len(quote):
#     # pdb.set_trace()
#     pos = quote.find('a', pos)
#     # print(pos)
#     if pos < 0:
#         break
#
#     index_list.append(pos)
#     pos += 1
#     loop_count += 1
#
#     #print(pos)
#     #print(index_list)
#
# print(index_list)
# print(loop_count)

# quote = "Believe you can and you're halfway there."
# pos = 0
# index_list = []
# while pos <= len(quote):
#     pos = quote.find('a', pos)
#     if pos < 0:
#         break
#     index_list.append(pos)
#     pos += 1
# print(index_list)

# Exam:
# Write code and process it function
# string
# Formatting  of data
# lists and order of things
# more methods on lists
# lists and true or false questions
# import copy about shallow copy and deep copy
# one of the lists assignment that we are doing


# Given the lists list1 and list2 that are of the same length,
# create a new list consisting of the first element of list1 followed by the first element of list2,
# followed by the second element of list1, followed by the second element of list2, and so on
# (in other words the new list should consist of alternating elements of list1 and list2).
# For example, if list1 contained [1, 2, 3] and list2 contained [4, 5, 6], then the new list should
# contain [1, 4, 2, 5, 3, 6]. Associate the new list with the variable list3.

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = []
for num in range(len(list1)):
    list3.append(list1[num])
    list3.append(list2[num])

print(list3)




