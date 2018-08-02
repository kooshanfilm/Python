

try:
    fh = open('xloop.py')
    for line in fh.readlines():
        print(line)
except IOError as e:
    print('something bad as {} happend'.format(e))

print("OK lets start")