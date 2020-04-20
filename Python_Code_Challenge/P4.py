
print("Welcome to Fibonacci app")

num = int(raw_input("How many digit would you like to compute"))
fib = [1,1]
for i in range(num - 2):
    new_fib = fib[i] + fib[i+1]
    fib.append(new_fib)

print(fib)

golden = []
for i in range (len(fib) - 1):
    ratio = fib[i+1]/fib[i]
    golden.append(ratio)

print ("the golden ratio is " +  golden)