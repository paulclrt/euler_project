def is_prime(num):
    is_prime = True
    for i in range(1, int(num/2)):
        if num % i == 0:
            is_prime= False
    return is_prime

con = 600851475143
count = 0
for i in range(1, con+1):
    if con % i == 0:
        print("count : ", count , "divisible: ", i)
        if is_prime(i) == True:
            print(i)
    if count % 10000000 == 0:
        print("at : ", count)
    count += 1
