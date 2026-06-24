#PROJECT- ROCK, PAPER, SCISSORS GAME
n=0
while n==0: #for (4.)
    
    #1.taking user input(rock paper scissors):
    print("ROCK, PAPER, SCISSORS! \n")
    print("Enter Rock, Paper or Scissors")
    user_input=input(":")
    user_input.lower

    #2.converting user input into integer:
    if "ro" in user_input:
        user_input=1
    elif "pa" in user_input:
        user_input=2
    elif "sci" in user_input:
        user_input=3
    else:
        print("Invaild option entered! \n Try Again")
        continue
    
   
    #3.computer functioning:
    import random
    comp_list=[1,2,3]
    computer= random.choice(comp_list) 

    #Deciding user won or lose:
    
    #Draw conditions:
    if computer==user_input:

        if computer==1:
            print("Ai: Rock  V/s  Rock :You") 
        elif computer==2:
            print("Ai: Paper  V/s  Paper :You") 
        elif computer==3:
            print("Ai: Scissors  V/s  Scissors :You") 
        print(f"Tie!")
    #Wining conditions:
    elif computer==1 and user_input==2:
        print("Ai: Rock  V/s  Paper :You \n You won!")
    elif computer==2 and user_input==3:
        print("Ai: Paper  V/s  Scissors :You \n You won!")
    elif computer==3 and user_input==1:
        print("Ai: Scissors  V/s  Rock :You \n You won!")
    #loosing conditions:
    elif computer==2 and user_input==1:
        print("Ai: Rock  V/s  Paper :You \n You lost!")
    elif computer==3 and user_input==2:
        print("Ai: Rock  V/s  Paper :You \n You lost!")
    elif computer==1 and user_input==3:
        print("Ai: Rock  V/s  Paper :You \n You lost!")

   #4.start the program again:
    repeat=input("Do you want to play again \ny/n:")
    repeat.lower
    if "y" in repeat:
        n=0
        print("")
    elif "n" in repeat:
        n=1
        print("")
    else:
        print("Entered value is invalid")
        n=1