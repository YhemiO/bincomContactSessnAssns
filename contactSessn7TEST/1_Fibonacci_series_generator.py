def fibSeqGen():
    n2 = 1
    n3 = 1
    while True:
        n1 = n2
        n2 = n3
        n3 = n1 + n2
        yield n1
a = fibSeqGen()
while True:
    try:
        x = int(input('Enter a range of Fib Sequence to Generate (1 - 100): '))
        if 1 <= x <= 100:
            for i in range(x):
                print(next(a), end=" ")
            break
        else:
            print("Your input is invalid. Please enter a number between 1 and 100.")
    except ValueError:
        print("Your input is invalid. Please enter a valid integer.")

