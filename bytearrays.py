


def main():
    fin = open('generatior.py','r',encoding='utf_8')
    fout = open('newfile.txt','w')
    outbytes = bytearray()
    for line in fin:
        for c in line:
            if ord(c) > 127:
                outbytes += bytes('&#0000')
            else:outbytes.append(ord(c))

    outstr = str(outbytes,encoding='utf_8')
    print(outstr,file=fout)
    print('done')

if __name__ == '__main__': main()
