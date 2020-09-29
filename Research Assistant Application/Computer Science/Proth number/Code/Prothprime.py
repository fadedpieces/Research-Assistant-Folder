# My code demonstrating how to find if a number is proth and proth prime


# function to check if a number is a power of 2
def is_a_power_of_2(x):
    return x and (not (x & (x - 1)))


# function to  check if the number is Proth
def checkifproth(x):
    # create variable used to test proth theorem
    k = 1  # starting from 1 to use only odd numbers

    while k < (x // k):

        # check if k can divide x or not
        if x % k == 0:

            # next check if (x/k) is a power of 2
            if is_a_power_of_2(x // k):
                print("Number is proth")
                return True
        k = k + 2

    print("Number is not proth")
    return False


# function to check if Proth number is prime

def checkifprothprime(p):
    import math
    a = 1
    power = (p - 1) / 2

    # while loop used to test proth theorem for varies values of a
    while a < p:
        # check if 'a power p' is divisible by p
        if ((math.pow(a, power)) + 1) % p == 0:
            print("number is a prime proth!!")
            return True
            break
        a = a + 1


    # if proth number is not proth prime return false
    return False



# driver code

# random list of odd number for testing
list_of_numbers = [3, 5, 7, 9, 11, 15, 17, 41]

# checking if the numbers in the list are proth prime or not
for n in list_of_numbers:
    print(str(n) + "")
    if checkifproth(n-1):
        if checkifprothprime(n):
            print("")

        else:
            print("number is not prime proth")
