# Given the strings s1 and s2, not necessarily of the same length, create a new string consisting of alternating
# characters of s1 and s2 (that is, the first character of s1 followed by the first character of s2,
# followed by the second character of s1, followed by the second character of s2, and so on.
# Once the end of either string is reached, no additional characters are added.
# For example, if s1 contained "abc" and s2 contained "uvwxyz", then the new string should contain "aubvcw".
# Assign the new string to the variable s3.

# s1 = "ace"
# s2 = "bdfgh"
# s3 = ""
# l1 = len(s1)
# l2 = len(s2)
# # print(''.join(map(''.join, (zip(s1, s2))))
# out1 = ''.join(map(''.join, zip(s1, s2)))
# print(out1)

# i = [11, 22, 11]
# n = i.count(11)
# print(n)


# numbers = [1, 1, -1]
# sum1 = sum(i for i in numbers if i > 0)
# print(sum1)
# l1 = [ 1, 2, 1]
# has_dups = len(l1) != len(set(l1))
# print(has_dups)




# a = 1
# b = 2
#
# x = 1 if a > b else -1
# # Output is -1
# print(x)
#
# x = 1 if a > b else -1 if a < b else 0
# print(x)
#
# credits = 60
#
# a = "freshmon" if credits < 30 else "sophomore" if 30 >= credits < 60 else "junior" if 60 >= credits < 90 else "senior"
#
# print(a)

# if credits >= 90:
#     "senior"
# elif credits >= 60 and credits < 90:
#     "junior"
# elif credits >= 30 and credits < 60:
#     "sophomore"
# else:
#     "freshman"

# def month_name (number):
#     if number == 1:
#         return "jan"
#     elif number == 2:
#         return "feb"
#     elif number == 3:
#         return "mar"
#     elif number == 4:
#         return "apr"
#     elif number == 5:
#         return "may"
#     elif number == 6:
#         return "jun"
#     elif number == 7:
#         return "jul"
#     elif number == 8:
#         return "aug"
#     elif number == 9:
#         return "sep"
#     elif number == 10:
#         return "oct"
#     elif number == 11:
#         return "nov"
#     elif number == 12:
#         return "dec"
#
#
# print(month_name(3))

# month = 2
# a = "jan" if month == 1 else "feb" if month == 2 else "mar" if month == 3 else "apr" if month == 4 else "may" \
#     if month == 5 else "jun" if month == 6 else "jul" if month == 7 else "aug" if month == 8 else "sep" \
#     if month == 9 else "oct" if month == 10 else "nov" if month == 11 else "dec"


# # 51286
# n = 19
# distance = 2
# sum1 = 0
# i = 0
# a = 1
# while a < n:
#     sum1 = sum1 + a
#     a = a + distance
# print(sum1)

# # 51293
# m = 3
# n = 20
# triangulars = []
#
# for ele in range(m, n+1):
#     print(ele)
#     if ele == sum(list(range(1, ele))):
#         triangulars.append(ele)
# print(triangulars)

# number = 3
# for i in range(1,21):
#   number = number + i
#   print(number)
#
# s1 = "abc"
# s2 = "xyz"
# s3 = zip(s1, s2)
# print(s3)
# s1 = "abc"
# s2 = "xyz"
# s3 = ''.join(''.join(f for f in tup) for tup in zip(s1, s2))
# print(s3)

s1 = "abcdefgh"
s2 = "wxyz"

# def all_triangle_numbers(n):
#     for i in range(1, n + 1):
#         print("n = {0}, triangle = {1}".format(i, (i ** 2 + i)//2))
#
# all_triangle_numbers(10)
s3 = ""
# print(len(s1))
# print(len(s2))
# for i in range(min(len(s1), len(s2))):
#     s3 += s1[i] + s2[i]
#
# if len(s1) > len(s2):
#     s3 += s1[len(s2):]
# else:
#     s3 += s2[len(s1):]
# print(s3)
# t = ["cat", "dog", "cows"]
# i = 0
# four_letter_word_count = 0
# while i < len(t):
#     if len(t[i]) == 4:
#         four_letter_word_count += 1
#     i += 1
# print(four_letter_word_count)
#
#


#
# lst = [ 1, 3, 8, 7, 6, 2]
# max_dup = -1
# lst.sort()
# print(lst)
# for i in range(len(lst) - 1):
#     if lst[i] == lst[i+1]:
#         max_dup = lst[i]
# print(max_dup)

# def isTriangular(num):
#     s, n = 0, 1
#     while s <= num:
#         s += n
#         if s == num:
#             return True
#         n += 1
#     return False
#
#
# triangulars = []
# m = 3
# n = 20
#
# for ele in range(m, n + 1):
#     if isTriangular(ele):
#         triangulars.append(ele)
#
# print(triangulars)


# d1 = {2:3, 8:19, 6:4, 5:12}
# # d2 = {2:5, 4:3, 3:9}
# # d3 = {}
# # for k, v in d1.items():
# #     if v in d2.keys():
# #         d3[k] = d2[v]
# #
# # print(d3)

# weights = {12, 19, 6, 14, 22, 7}
# desired_weight = 18
# sl = sorted(weights)
# actual_weight = None
# for ele in sl:
#     if ele <= desired_weight:
#         actual_weight = ele
#     else:
#         break
# weights.remove(actual_weight)
# print(weights)
# print(actual_weight)

# weights = {12, 19, 6, 14, 22, 7}
# desired_weight = 18
# sl = sorted(weights)
# actual_weight = sl[min(range(len(sl)), key=lambda i: abs(sl[i] - desired_weight))]
# weights.remove(actual_weight)
#
# print(weights)
# print(actual_weight)
# def closest(lst, K):
#     return lst[min(range(len(lst)), key=lambda i: abs(lst[i] - K))]
#
#
# print(closest(sl, 18))


m = 2
n = 20
fib = []
f1, f2, f3 = 0, 1, 1

while f1 <= n:
    if f1 >= m:
        fib.append(f1)

    f1 = f2
    f2 = f3
    f3 = f1 + f2

print(fib)




