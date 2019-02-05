

def main():

    d = {'one':1,'two':2,'three':3}
    print(d)

    for key in d:
        #print(key,d)
        #print(key,d[key])
        print(sorted(d.keys()))

    d2 = dict(five=5,six=6,seven=7)


    d2['eight'] = 8
    print(d2)
if __name__ == '__main__': main()


# student = {1: 'value1','key2' :'value2'}
#
# student['james'] = 'boby'
# student.update({1 : 'Eventbase'})
# print student
# print student.items()
# print student.keys()
# print student.values()
# print (student.get('key23'))