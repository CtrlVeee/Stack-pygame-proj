data = '1, 2, 4,5'
noSpace = ''
noStr = True
splits = data.split(' ')
print(splits)
for val in splits:
    noSpace += val
print(noSpace)
noComma = noSpace.split(',')
print(noComma)
newData = []
for val in noComma:
    try:
        num = int(val)
        newData.append(num)
    except:
        noStr = False
        break

if not noStr:
    print('value has a string')
elif noStr:
    print('all ints checked')
    print(newData)