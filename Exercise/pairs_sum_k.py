# give an integer array and a number k, output all pairs that sum up to k
#(1,3,2,5,46,6,7,4)
# (1,4)(3,2)


def sum_of_numbers(my_list,k):
    x = 0
    lent = len(my_list)
    while x < lent:
        for i in my_list:
            sum = my_list[x] + i
            if sum == k:
                print (my_list[x],i)
        x+=1


print sum_of_numbers([1,3,2,5,46,6,7,4],5)



