while True:
    import random
    ######## rock paper scissor
    print("Welcome to rock paper scissor game: ")
    print("what would you chose:")
    print("1.Rock\n2.Paper\n3,Scissor")
    choice = int(input("Enter your choice:"))
    x = random.randint(1,3)


    if choice == x:
        print("tie")
    elif (choice == 1 and x == 3) or (choice == 2 and x == 1) or (choice == 3 and x == 20):
        print("You win!")
    else:
        print("you loose!!")