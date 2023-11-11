# import os
#
#
# def get_folder_files(directory_name):
#     file_list = os.listdir(directory_name)
#     result_dict = {"filenames": [], "dirnames": []}
#     for file in file_list:
#         if os.path.isdir(file):
#             result_dict["dirnames"].append(file)
#         else:
#             result_dict["filenames"].append(file)
#     return result_dict
#
#
# #
# #
# dir_name = "../homework"
# res = get_folder_files(dir_name)
# # print(res)


# def get_ordering_files(filenames_dict, ordering=True):
#     filenames_dict["filenames"].sort(reverse=not ordering)
#     filenames_dict["dirnames"].sort(reverse=not ordering)
#     return filenames_dict
#
#
# f_names = get_ordering_files(res, True)
# print(f_names)

#
# def add_file_to_dict(filedict, filename):
#     if "." in filename and not filename.startswith("."):
#         filedict["filenames"].append(filename)
#     else:
#         filedict["dirnames"].append(filename)
#     return filedict
# dot = add_file_to_dict(res, "dot_file.txt")
# print(dot)
# dot2 = add_file_to_dict(res, "dot_file")
# print(dot2)
#
