def is_prime(num):
    for i in range(2, int(num/2)+1, 1):
        if num % i == 0:
            return False
    return True

prime_counter = 0
num_test = 1
while prime_counter != 10002:
    if is_prime(num_test):
        if prime_counter >= 9999:
            print(f"prime {prime_counter}: ", num_test) 
        prime_counter += 1
    num_test +=1
    
    
