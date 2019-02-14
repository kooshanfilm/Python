def missing_element(f_list,s_list):

    missing_arr = []
    for i in f_list:
        if i in s_list:
            pass
        else:
            missing_arr.append(i)
    missing = missing_arr[0]
    return missing



print missing_element([1,2,3,4],[1,2,3])