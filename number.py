import math

def check_prime(n):
    if n <= 1:
        return "Not a prime number"
    for i in range(2, int(math.sqrt(n)) +1):
        if  n % i ==0:
            return "Not a prime number"
        
        return "prime number"

    print(check_prime(8))
    
