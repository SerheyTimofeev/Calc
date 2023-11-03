# my_list = ["first", "second", "loop"]
# new_list = []
#
# for index, value in enumerate(my_list):
#     if index % 2 != 0:
#         new_list.append(value[::-1])
#     else:
#         new_list.append(value)
#
# print(new_list)
# ###############
# my_list = ["app", "loop"]
# new_list = []
#
# for i in my_list:
#     if i.startswith("a"):
#         new_list.append(i)
#
# print(new_list)
#
# new_list = [i for i in my_list if i.startswith("a")]
# print(new_list)
# ################
#
# my_list = ["app", "loop", "oppA"]
# new_list = []
# for i in my_list:
#     if "a" in i.lower():
#         new_list.append(i)
# print(new_list)
#
# people = [
#     {"name": "John", "age": 2},
#     {"name": "Jack", "age": 4},
#     {"name": "Serg", "age": 3}
# ]
# min_age_people = []
# min_range_name = []
# all_people_age = []
# min_age = min([i["age"] for i in people])
# for person in people:
#     if person["age"] == min_age:
#         min_age_people.append(person["name"])
# print(min_age_people)
#
# min_range = min([len(i["name"]) for i in people])
# for person in people:
#     if len(person["name"]) == min_range:
#         min_range_name.append(person["name"])
#
# print(min_range_name)
#
#
# all_age = sum([i["age"] for i in people])
# avg_age = all_age // len(people)
# print(avg_age)
#
#
my_dict_1 = {
    "key": "value2",
    "key1": "value1",
    "key2": "value3",
}
my_dict_2 = {
    "key": "value1",
    "keys1": "value2",
    "keys2": "value3",
}
#
# keys_1 = set(my_dict_1.keys())
# keys_2 = set(my_dict_2.keys())
# same_keys = keys_1.intersection(keys_2)
# print(same_keys)
#
# diff_keys = keys_1.difference(keys_2)
# print(diff_keys)
#
# result_dict = {key: value for key, value in my_dict_1.items() if key in diff_keys}
# print(result_dict)
#
# union_dict = my_dict_1.copy()
# for key, value in my_dict_2.items():
#     if union_dict.get(key):
#         union_dict[key] = [union_dict[key], value]
#     else:
#         union_dict[key]=value
# print(union_dict)
