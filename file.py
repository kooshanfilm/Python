def main():
    buffersize = 5000
    infile = open('newfile.txt','r')
    outfile = open('new.txt','w')
    buffer = infile.read(buffersize)
    while len(buffer):
        outfile.write(buffer)
        print('.')
        buffer = infile.read(buffersize)
    print('done')



if __name__ == '__main__':main()
