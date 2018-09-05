

# here we want to have a list or array
# and then reverse our arra


class Reverse:

    def rever_number(self,my_list):
        my_array = my_list
        #print(len(my_array))
        array_len = len(my_array)

        for i in my_array:
            print(my_array[array_len-1])
            array_len -=1


    def rever_number_while(self):
        my_array = [1,2,5,4,3,2]
        arr_len = len(my_array) #4
        i = 0
        while(i < arr_len):
            print(my_array[arr_len - 1])
            arr_len -=1




def main():
    call = Reverse()
    #call.rever_number([1,2,3,4,5])
    call.rever_number_while()


if __name__ == '__main__': main()
