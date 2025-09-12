bankrob = False
nobankrob = False
terminating = False
if input("Welcome to your new life, to begin you get home from school and are confronted with a choice. Do you do your homework or not?(yes/no)\n").lower() == "yes":
    math_hw = input("Do you know all of the answers to your math homework?(yes/no)\n").lower() == "yes"
    english_hw = input("Do you write your english essay as well?(yes/no)\n").lower() == "yes"
    if math_hw and english_hw:
        print("Congratulations!! when you get to school the next day you are awarded 100 million dollars!!!!!")
        if input("Do you drop out of school now?(yes/no)\n").lower() == "yes":
            print("With your hundred million you live pretty dang well for a couple of years, however like most people who come upon lots of money, you don't save it well and it eventually runs out. You are now homeless.")
            if input("Do, you rob a bank for more money?(yes/no)\n").lower() == "yes":
                bankrob = True
            else:
                nobankrob = True
        else:
            print("You're so honorable, with this goodness in you, you end up becoming a wealthy charatitable man, and live happily and die with a good legacy.")
    elif not(math_hw or english_hw):
        print("Luckily for you school gets canceled the next day.")
        input("Do you do your homework now?(yes/no)\n")
        print("Russia bombs the United States becuase you didn't solve the math problems quick enough to help the government protect the country. The world goes into nuclear fallout.")
    elif math_hw and not(english_hw):
        print("Your essay was due two days ago, when you go into school your teacher gets really mad.")
        if input("Do you apologize?(yes/no)\n").lower() == "yes":
            print("Your teacher reveales themselves to be Zues, and becuase you were nice to him, you get to become the god of math homework, and live in eternal joy as your sadistic self watches highschool kids struggle with their homework.")
        else:
            terminating = True
    elif not(math_hw) and english_hw:
        print("Becuase of this one homework assignment you decide to become and english major, unfortunately becuase of this you are now homeless.")
        if input("Do you rob a bank to get some money?(yes/no)\n").lower() == "yes":
            bankrob = True
        else:
            nobankrob = True
else:
    print("You hear a knock on the door.")
    if input("Do you answer it?(yes/no)\n").lower() == "yes":
        print("When you open the door Arnold Schwarzenegger, the terminator is standing there.")
        if input("Do you invite him in for tea?(yes/no)\n").lower() == "yes":
            print("He tells you to get him whatever.")
            tea = input("Do you get earl grey tea, black tea, or green tea for him?(earl grey/black/green)\n").lower()
            if tea == "earl grey":
                print("Arnold loves your choice, and because of that, he decides not to kill you. However, becuase of this you end up starting the robot war and the earth is nuked and split into millions of pieces.")
            elif tea == "black":
                print("Arnold doesn't like your choice, but he respects it. He takes you to the future and you end up becoming a general that figthts robots. But they don't exist becuase you didn't invent them. You are then stuck in a paradox and live in immesurable pain.")
            elif tea == "green":
                print("Arnold really hates your choice. But you did let him in for tea, so you just get put in prison for your life and you don't know why. But, you are happy(somehow)")
        else:
            terminating = True
    else:
        terminating = True
if terminating == True:
    print("Thats too bad! The terminator comes in and eliminates you becuase you are the one that invents robots in the the future and ruins humanity. Sorry.")
if bankrob == True:
    print("While you are robbing the bank, a cop comes in to deposit some moeny and arrests you.")
    if input("Do you try to break out of jail?(yes/no)\n").lower() == "yes":
        print("Somehow, you meet a really handy cellmate and together you break out and move to Rwanda so the government can't track you and live together happily ever after.")
    else:
        print("You live out the rest of your years in jail, until you die, and then you go to hell and are tortured for eternity.")
if nobankrob == True:
    print("Becuase you decided to not rob the bank, and angel comes down and blesses you with a good life as you are a good person at heart.")