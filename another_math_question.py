class Reverse:

    def dict_pract(self):
        tel = {}
        #print(type(tel))
        tel['jadi'] = '0129'
        tel['b'] = '012'

        book = {'jadi':'00','james':'bob','K':'M'}
        #print(book)
        #print(tel)
        for i in book:
            #print(i,book[i])
            print()

        for k,v in book.items():
            print(k,v)

def main():
    call = Reverse()
    call.dict_pract()

if __name__ == '__main__': main()


