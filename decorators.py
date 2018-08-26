class Duck:
    def __init__(self,**kwargs):
        self.properties = kwargs

    def quack(self):
        print('quaccck')

    def walk(self):
        print('this is walk')

    def get_properties(self):
        return self.properties

    def get_proterty(self, key):
        return self.properties.get(key,None)

    @property
    def color(self):
        return self.properties.get('color',None)

    @color.setter
    def color(self,c):
        self.properties['color'] = c

    @color.deleter
    def color(self):
        del self.properties['color']


def main():
    donald = Duck(color = 'blue')
    donald.color = 'blue'
    print(donald.color)



if __name__ == '__main__': main()
