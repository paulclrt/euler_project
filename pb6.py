def sum_of_squares():
    sum = 0
    for i in range(0, 101):
        sum+=i**2
    return sum

def square_of_sum():
    sum = 0
    for i in range(0, 101):
        sum+=i
    sum=sum**2
    return sum

diff = square_of_sum() -  sum_of_squares()
print(diff)
