num = [1, 10, 20, 50, 100, 110, 130, 150]
for i in num:
    if i > 100:
        print(i)
####################
num = [1, 10, 20, 50, 100, 110, 130, 150]
my_results = []
for i in num:
    if i > 100:
        my_results.append(i)
print(my_results)
##################
num = [1, 2, 4, 6]
if len(num) < 2:
    num.append(0)
else:
    num.append(num[-1] + num[-2])
print(num)
