

# [1,5,3,7,9] >> [1,3,5,7,9]
# [1,3,


def sort_arr(my_list):

    min = my_list[0]  # 1
    sorted_list = []
    arr_l = len(my_list)
    x = 0
    while x < arr_l:
        for i in my_list:
            if i < min:
                to_be_removed =  my_list.index(i)
                min = i
                sorted_list.append(min)
                my_list.pop(to_be_removed)
        x+=1

    print sorted_list

sort_arr([5,4,3,2])
