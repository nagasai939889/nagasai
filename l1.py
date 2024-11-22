def is_prime(num):
    # Check for numbers less than 2 (not prime)
    if num <= 1:
        return False
    # Check for factors from 2 to the square root of num
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Input from the user
number = int(input("Enter a number: "))

# Check and display if the number is prime or not
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")