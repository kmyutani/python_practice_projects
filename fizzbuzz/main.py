import time
# --------------- FizzBuzz Function ---------------


def fizz_buzz(num_range):
    for n in range(1, num_range+1):
        time.sleep(0.5)
        if (n % 3 == 0) and (n % 5 == 0):
            print("FizzBuzz")
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        else:
            print(n)

# --------------- FizzBuzz Main ---------------

# Prompts the user for a number to fizzbuzz
number = int(input("Enter a number to FizzBuzz: "))
# Executes the fizz buzz function
fizz_buzz(number)
