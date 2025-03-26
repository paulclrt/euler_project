
def check_num(num):
    for i in range(1, 21, 1):
        #print(i, num%i)
        if num % i != 0:
            return False

    return True


i = 0
while True:
    i+=1
    if check_num(i):
        print(i)
        break
