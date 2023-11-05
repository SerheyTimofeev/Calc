import random
import string
# def revers(my_list):
#     new_list = []
#
#     for index, value in enumerate(my_list):
#         if index % 2 != 0:
#             new_list.append(value[::-1])
#         else:
#             new_list.append(value)
#     return new_list
#
#
# print(revers(["Nick", "Sergio", "Jack"]))


################

# def first_a(my_list):
#     new_list = []
#
#     for i in my_list:
#         if i.startswith("a"):
#             new_list.append(i)
#
#     return new_list
#
#
# print(first_a(["afro", "key"]))

###############
# def all_a(my_list):
#     new_list = []
#
#     for i in my_list:
#         if "a" in i.lower():
#             new_list.append(i)
#     return new_list
#
#
# print(all_a(["apple", "Nickolas", "free"]))

##############

# def str_and_int(my_list):
#     result = []
#     for i in my_list:
#         if type(i) == str:
#             result.append(i)
#     return result
#
#
# print(str_and_int(["fjdkhfsd", 23]))

###############

# def one_time(my_str):
#     new = []
#     for i in set(my_str):
#         if my_str.count(i) < 2:
#             new.append(i)
#     return new
#
# print(one_time("hhhhhooopl"))


##############

# def my_intersection(my_str_1, my_str_2):
#
#     new_set_1 = set(my_str_1)
#     new_set_2 = set(my_str_2)
#     result = list(new_set_1.intersection(new_set_2))
#     return result
#
#
# print(my_intersection("12312425", "123245409"))

#################

# def intersection_one_time(my_str_1, my_str_2):

#     new_set_1 = {i for i in my_str_1 if my_str_1.count(i) < 2}
#     new_set_2 = {i for i in my_str_2 if my_str_2.count(i) < 2}
#     result = list(new_set_1.intersection(new_set_2))
#     return result
#
#
# print(intersection_one_time("loop", "loop"))

##################


# def create_email(domains, names):
#     name = random.choice(names)
#     domen = random.choice(domains)
#     number = random.randint(100, 999)
#     letters = string.ascii_lowercase
#     rand_string = ''.join(random.choice(letters) for i in range(random.randint(5, 7)))
#
#     return f"{name}{number}@{rand_string}.{domen}"
#
# names = ["king", "miller", "kean"]
# domains = ["net", "com", "ua"]
#
# e_mail = create_email(domains, names)
#
# print(e_mail)
