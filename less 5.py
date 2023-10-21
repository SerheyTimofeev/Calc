m = "0123456789"
print(m[2])
#######
m = "0123456789"
print(m[-2])
#######
m = "0123456789"
print(m[:5])
#######
m = "0123456789"
print(m[:-2])
#######
m = "0123456789"
print(m[::2])
#######
m = "0123456789"
print(m[1::2])
#######
m = "0123456789"
print(m[::-1])
#######
m = "0123456789"
print(m[::-2])
#######
m = "0123456789"
print(len(m))
#######
m = "hello world fdgjd hvhgvkc jhbgkhvkhgv"
print(m.count(" ") + 1)
########
m = "I dont understand"
print(len(m.split()))
#######
s = input()
ch = input()
index = -1
while True:
    index = s.find(ch, index + 1)
    if index == -1:
        break
    print(index)
#########
s = "hhfjsfhjhhhh"
print(s[0] + s[1:-2].replace("h", "H") + s[-1])