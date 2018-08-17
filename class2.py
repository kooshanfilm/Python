class Duck:


    def __init__(self):
        print('constractor')

    def quack(self):
        print('Quaaack')

    def walk(self):
        print('walk like a duck')


def main():
    donald = Duck()
    donald.quack()
    donald.walk()


if __name__ == '__main__': main()
