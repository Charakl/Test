my_list = [100,200,300,199,99,9]


def extendList(list):
    a_list = [101, 202, 303]
    list.extend(a_list)
    return list


print(extendList(my_list))

for i, j in enumerate(my_list):
    print(my_list[i])



def sum_list(list):
    sum=0
    for index, item in enumerate(list):
        sum += list[index]

    return sum
print('the total is: ' + str(sum_list(my_list)))

def max_min_item(list):
    max=list[0]
    min=list[0]
    for index, item in enumerate(list):
        if list[index] > max:
            max = list[index]

        if list[index] < min:
            min = list[index]

    return [max,min]


mm = max_min_item(my_list)
print('the max item is: ' + str(mm[0]) + '\nthe min item is: ' + str(mm[1]))
