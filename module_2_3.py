my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while len(my_list) > i:
    if my_list[i] > 0:
        print(my_list[i])
    elif my_list[i]< 0:
        break
    i += 1