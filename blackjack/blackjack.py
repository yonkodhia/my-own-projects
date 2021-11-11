import random
i = 0
deck = [1,2,3,4,5,6,7,8,9,10]*4


hand = [random.choice(deck), random.choice(deck)]
cpuhand = [random.choice(deck), random.choice(deck)]

hit = ["hit", "Hit" , "h"]
stand = ["stand" , "Stand"]
hs = ["hit" , "stand"]

def cpuTurn() :
    cpuchoice = random.choice(hs)
    if cpuchoice == "hit":
        print("\nCPU: \"hit me .\"\n")
        deal = random.choice(deck)
        cpuhand.append(deal)
        if sum(cpuhand) > 21 :
            print("the CPU busted ! you won !")
            print(f"your hand: {sum(hand)}\n CPU hand : {sum(cpuhand)}")
        if sum(cpuhand) == 21 :
            print("the CPU hit 21 ! you lose")
            print(f"your hand: {sum(hand)}\n CPU hand : {sum(cpuhand)}")
        if cpuchoice == "stand" :
            print("\nCPU: \"i'm standing.\"\n")

while i < 3 :
    choice = input("your current hand is {sum(hand) \n hit or stand? }")
    if choice in hit :
        deal = random.choice(deck)

        hand.append(deal)
        i += 1
        if sum(hand) > 21 :
         print("you lost !")
         print(f"your hand: {sum(hand)}\n CPU hand: {sum(cpuhand)}")
         break; 
        if sum(hand) == 21:
            print("you hit 21! you win !")
            print(f"your hand: {sum(hand)}\n CPUhand: {sum(cpuhand)}")
            break; 
cpuTurn()


if choice in stand :
    i += 1
    cpuTurn()


      
