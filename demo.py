import random
deck = []
for x in range(16):
    deck.append(x+1)
#print(deck)
bet = random.sample(deck, k=4)
#print(random.sample(deck, k=len(deck)))
print(bet)


def compare(data):
    answer = False
    for item in bet:
        if item == data:
            answer = True
    return answer

def demo():
    loop = True
    while loop:
        guess = input("Enter guess: ")
        try:
            guess = int(guess)
            if guess >= len(deck) or guess <= 0:
                print(f"Must be within 1-{len(deck)}")
            else:
                #print("guess is within the range")
                if compare(guess) == True:
                    print("your guess was True")
                    print("Program ended")
                    break
                else:
                    print("Wrong Answer")
        except:
            print("Please enter a number")