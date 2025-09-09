bankrob = False
terminating = False
if input("Welcome to your new life, to begin you get home from school and are confronted with a choice. Do you do your homework or not?(yes/no)\n") == "yes":
    math_hw = input("Do you know all of the answers to your math homework?(yes/no)\n") == "yes" and :
    english_hw = input("Do you write your english essay as well?(yes/no)\n") == "yes":
    if math_hw and english_hw:
        print("Congratulations!! when you get to school the next day you are awarded 100 million dollars!!!!!")
        if input("Do you drop out of school now?(yes/no)\n") == "yes":
            print("With your hundred million you live pretty dang well for a couple of years, however like most people who come upon lots of money, you don't save it well and it eventually runs out. You are now homeless.")
            if input("Do, you rob a bank for more money?(yes/no)\n") == "yes":
                bankrob = True
            else:
                print("Becuase you decided to not rob the bank, and angel comes down and blesses you with a good life as you are a good person at heart.")
        else:
            print("You're so honorable, with this goodness in you, you end up becoming a wealthy charatitable man, and live happily and die with a good legacy.")
    elif not(math_hw and english_hw):
        print("Luckily for you school gets canceled the next day.")
        if input("Do you do your homework now?(yes/no)\n") == "yes":
            
