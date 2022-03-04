import random
deck = []
for x in range(16):
    deck.append(x+1)
#print(deck)
bet = random.sample(deck, k=4)
win_data = ['/','/','/','/']
#print(random.sample(deck, k=len(deck)))
print(bet)


def compare(data):
    answer = False
    for item in bet:
        if item == data:
            answer = True
    return answer

def compare(inValue, genData):
    a = genData
    b = inValue
    
    compare = ['','','','']

    for count, val in enumerate(b):
        #print(count)
        if val in a:
            compare[count] = '!'
            if a[count] == val:
                compare[count] = '/'
            #print(True)
        else:
            compare[count] = 'x'
            #print(False)
    #print(compare)
    return compare

def main():
    loop = True
    noSpace = ''
    noStr = True
    newData = []
    while loop:
        data = input("Enter guess: ")
        #separate into diff values
        splits = data.split(' ')
        for val in splits:
                noSpace += val
        noComma = noSpace.split(',')

        #check if 4 values
        if len(noComma) == 4:
            #check if all int
            for val in noComma:
                try:
                    num = int(val)
                    newData.append(num)
                    
                except:
                    noStr = False
            if not noStr:
                print('please enter digits')
                #resets data
                noStr = True
                noSpace = ''
                newData = []
            else:
                #compare inputs to the generated bet
                result = compare(newData, bet)
                print(result)
                if result == win_data:
                    print("you guessed it right!\nYou won!!")
                    print("program ended")
                    loop=False
                    break
                else:
                    #resets data
                    noStr = True
                    noSpace = ''
                    newData = []
                    print('wrong guess, try again')
        else:
            #resets data
            noStr = True
            noSpace = ''
            newData = []
            print('please enter 4 digits\nseparated by commas\spaces')
main()