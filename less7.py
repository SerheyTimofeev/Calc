# num = 1000
# co = 0
#
# for i in str(num):
#     if i == "0":
#         co += 1
# print(co)

# new = [i for i in str(num) if i == "0"]
# print(len(new))

##############

# num = 100500
# co = 0

# for i in str(num)[::-1]:
#     if i == "0":
#         co += 1
#     else:
#         break
# print(co)

##############
# my_list_1 = [1, 2, 3, 4, 5]
# my_list_2 = [5, 5, 32, 62, 2, 4, 5, 4]
# my_result = list(my_list_1[::2] + my_list_2[::2])
# print(my_result)
#
# my_result2 = []
# my_result2.extend(my_list_1[::2])
# my_result2.extend(my_list_2[::2])
# print(my_result2)
# ################

# my_list = [1, 2, 3, 4, 5]
# new_list = my_list[1:].copy()
# new_list.append(my_list[0])
# print(new_list)

#################

# my_list = [1, 2, 3, 4, 5]
# charm = my_list.pop(0)
# my_list.append(charm)
# print(my_list)

##################

# my_str = "k 78 hh 65 kj 80"
# my_list = my_str.split(" ")
# sum = 0
# for i in my_list:
#     if i.isdigit():
#         sum += int(i)
#     else:
#         continue
# print(sum)

#################

# my_list = [2, 4, 1, 5, 3, 9, 0, 7]
# count = 0
# for index, value in enumerate(my_list):
#     # print(index, value)
#     if index == 0 or index == len(my_list)-1:
#         continue
#     if value > my_list[index-1] + my_list[index+1]:
#         count += 1
# print(count)

###################

# my_list = [1, "dfdsa", 2, "32312"]
# result = []
# for i in my_list:
#     if type(i) == str:
#         result.append(i)
# print(result)

####################

# my_str = "gygygpo"
# new = []
# for i in my_str:
#     if my_str.count(i) < 2:
#         new.append(i)
# print(new)

#list comprehension

# new = [i for i in my_str if my_str.count(i) < 2]
# print(new)

#################

# my_str_1 = "123456789012"
# my_str_2 = "12345670"
# new_set_1 = set(my_str_1)
# new_set_2 = set(my_str_2)
# result = list(new_set_1.intersection(new_set_2))
# print(result)

##################

# my_str_1 = "aaaasdf1"
# my_str_2 = "asdfff2"
# new_set_1 = {i for i in my_str_1 if my_str_1.count(i) < 2}
#
# new_set_2 = {i for i in my_str_2 if my_str_2.count(i) < 2}
# result = list(new_set_1.intersection(new_set_2))
# print(result)

