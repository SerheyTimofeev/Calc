import datetime
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
#             result.append({"date": my_split[0]})
#         return result
# print(get_dates_authors("authors.txt"))

#############

def get_dates_authors(file_name: str) -> list:
    with open(file_name, 'r') as my_file:
        data = my_file.readlines()
        result =[]
        list_for_replace = ["st", "nd", "rd", "th"]
        for i in data:
            my_split = i.split("-")
            if len(my_split) < 2:
                continue
            splited_date = my_split[0].strip()
            day = splited_date.split(" ")[0]
            result_str = splited_date.split(" ")[1:]

            for n in list_for_replace:
                day = day.replace(n, "")

            result_str.insert(0, day)

            if len(result_str) < 3:
                continue
            result_str = " ".join(result_str)

            formated_date = datetime.datetime.strptime(result_str.strip(), "%d %B %Y").date().strftime("%d/%m/%Y")
            result.append({"date_original": splited_date, "date_modified": formated_date})
        return result

print(get_dates_authors("authors.txt"))
