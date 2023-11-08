# def domains(domen: str) -> list:
#     """Read domains from file and return list of domains"""
#     my_file = open(domen, 'r')
#     data = my_file.read()
#     my_list = data.replace(".", "").split("\n")
#     my_file.close()
#
#     return my_list
#
# file_domains = "domain.txt"
# print(domains(file_domains))

########################################################################


# def get_lastnames(file_name: str) -> list:
#     """Read names from file and return list of last names"""
#     my_file = open(file_name, 'r')
#     data = my_file.readlines()
#     last_names = []
#     for i in data:
#         last_names.append(i.split("\t")[1])
#     my_file.close()
#
#     return last_names
# print(get_lastnames("names.txt"))

######################################################


# def get_dates_authors(file_name: str) -> list:
#     with open(file_name, 'r') as my_file:
#         data = my_file.readlines()
#         result =[]
#         for i in data:
#             my_split = i.split("-")
#             if len(my_split) < 2:
#                 continue
#             result.append({"data": my_split[0]})
#         return result
# print(get_dates_authors("authors.txt"))

#########


