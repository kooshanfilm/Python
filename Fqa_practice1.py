
class Fqa:

    def number(self,number):
        sum_of_mult = 0
        for i in range(2, number):
            if (i % 5) == 0 or (i % 3) == 0:
                sum_of_mult = i + sum_of_mult
        print("Sum of total number", sum_of_mult)

def main():

    call = Fqa()
    call.number(1000)


if __name__ == '__main__':main()








