# Write a program to retrive the number of times a specific items appears



def num_times(arr,number):
    count = 0
    for i in arr:
        if i == number:
            count +=1
    print count



num_times([1, 3, 5, 3, 7, 9, 3],3)