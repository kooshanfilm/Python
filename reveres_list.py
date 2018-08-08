def main():
    s = 'koushan'
    d = [12,10]

    list_lenght = len(d) - 1
    print ('this is list length {}'.format(list_lenght))

    while list_lenght >= 0:
        print(d[list_lenght],',',end='')
        list_lenght = list_lenght - 1
        #print('this is list length {}'.format(list_lenght))




if __name__ == '__main__': main()
