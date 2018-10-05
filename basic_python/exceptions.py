import re


def main():
    try:
        for line in readfile('xloop.py'):
            print(line.strip())

    except IOError as e:
        print('worng file agian')

    except ValueError as e:
        print('bad file name', e)


def readfile(filename):

    if filename.endswith('.py'):
        fh = open(filename)
        return fh.readlines()
    else:
        raise ValueError('wrong file extention')


if __name__ == '__main__': main()
