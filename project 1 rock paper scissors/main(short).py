#PROJECT- ROCK, PAPER, SCISSORS GAME
n=0
while n==0: #for (4.)
    
    #1.taking user input(rock paper scissors):
    print("ROCK, PAPER, SCISSORS! \n")
    print("Enter Rock, Paper or Scissors")
    user_input=input(":")
    user_input.lower

    #2.converting user input into integer:
    if "r" in user_input:
        user_input=1
    elif "p" in user_input:
        user_input=2
    elif "s" in user_input:
        user_input=3
    else:
        print("Invaild option entered! \n Try Again")
        continue
    
   
    #3.computer functioning:
    import random
    comp_list=[1,2,3]
    computer= random.choice(comp_list) 
    comp_dict={1:"Rock",2:"Paper",3:"Scissors"}

    #Deciding user won or lose:
    
    #Draw conditions:
    if computer==user_input:
        print(f"Ai: {comp_dict[computer]}  V/s  {comp_dict[user_input]}:You") 
        print(f"Tie!")
    
    #Wining conditions:
    elif (computer-user_input)==2 or (computer-user_input)==-1: 
        print(f"Ai: {comp_dict[computer]}  V/s  {comp_dict[user_input]}:You \n You won!")
    
    #loosing conditions:
    elif (computer-user_input)==-2 or (computer-user_input)==1: 
        print(f"Ai: {comp_dict[computer]}  V/s  {comp_dict[user_input]}:You \n You lost!")
    

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