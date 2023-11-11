# m = "0123456789"
# print(m[2])
# #######
# m = "0123456789"
# print(m[-2])
# #######
# m = "0123456789"
# print(m[:5])
# #######
# m = "0123456789"
# print(m[:-2])
# #######
# m = "0123456789"
# print(m[::2])
# #######
# m = "0123456789"
# print(m[1::2])
# #######
# m = "0123456789"
# print(m[::-1])
# #######
# m = "0123456789"
# print(m[::-2])
# #######
# m = "0123456789"
# print(len(m))
# #######
# m = "hello world fdgjd hvhgvkc jhbgkhvkhgv"
# print(m.count(" ") + 1)
# ########
# m = "I dont understand"
# print(len(m.split()))
# #######
# s = input()
# ch = input()
# index = -1
# while True:
#     index = s.find(ch, index + 1)
#     if index == -1:
#         break
#     print(index)
# #########
# s = "1234hh567"
# start_index = s.find("h")
# end_index = s.rfind("h")
# print(start_index)
# print(end_index)
# if start_index == -1 or start_index == end_index:
#     print(s)
# else:
#     print(s[:start_index + 1] + s[start_index + 1:end_index].replace("h", "H") + s[end_index:])