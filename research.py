path = "NES"
c = [0, 0]
my_list = [[0, 0]]
for i in path:
    print(i)
    if i == "N":
        c[0] += 1
        c[1] += 1
    # if i == "S":
    #     c[0] -= 1
    #     c[1] -= 1
    # if i == "W":
    #     c[1] -= 1
    if i == "E":
        c[1] += 1
    my_list.append(c)
print(my_list)