list1 = ['1', '2', '3']
list2 = ['a', 'b', 'c']
list3 = []
index = 0
loops = None

if len(list1) == len(list2):
    loops = len(list1)
else:
    print("Error")

for _ in range(loops):
    list3.append(list1[index])
    list3.append(list2[index])
    index += 1

print(list3)
