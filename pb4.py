def is_palindrom(num):
    mot = str(num)
    palindrom = True
    for i in range(0, int(len(mot)/2)):
        if mot[i] != mot[len(mot)-i-1]:
            return False
    return True


l = []
for i in range(1000, 0, -1):
    for j in range(1000, 0, -1):
        if is_palindrom(i*j):
            print(f"i: {i}, j: {j}, i*j: {i*j}")
            l.append(i*j)
            break

print(max(l))
