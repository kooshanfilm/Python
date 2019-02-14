



x = 0
my_list = [1,2,3,4]
l = len(my_list)
second ={}
while x < l:
    for num in my_list:
        if num in second:
            second[my_list[x]] = ""
        else:
            second[my_list[x]] = num
    x+=1


print second