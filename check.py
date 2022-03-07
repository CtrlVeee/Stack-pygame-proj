a = [1, 3, 4, 5]
b = [2, 1, 7, 5]

compare = ['','','','']

for count, val in enumerate(b):
    print(count)
    if val in a:
        compare[count] = '!'
        if a[count] == val:
            compare[count] = '/'
        print(True)
    else:
        compare[count] = 'x'
        print(False)
print(compare)