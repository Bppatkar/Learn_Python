input_data = int(input("Enter any number: "))

isPrime = True

if input_data > 1:
    for i in range(2, input_data):
        if (input_data % i) == 0:
            isPrime = False
            break

print(isPrime)
