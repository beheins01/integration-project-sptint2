#Integration Project
#Create Your Own Adventure
#Ben Heins
#Computer Science
#This is a story telling program where your choices have consiquences!
#The story changes depending on the choices you make.
#so be careful becuase one wrong choice may be your last...






print("Welcome to the story! Today you will be participating in my Integration Project!")
print("This project is a create your own adventure. I Hope You Enjoy!")
print("AND REMEMBER YOUR CHOICES HAVE CONSIQUENCES!")

answer = input("Would you like to play? (yes/no) ")

if answer.lower().strip() == "yes":
#"answer" - checks the answer  "lower" - makes sure the answer is in all lower case "strip" - gets rid of any white space or spaces (From W3Schools)

    import time      
    time.sleep(1.5)
#The last two lines of code delay the next line for 3 seconds  (From W3Schools)

    print("Calibration is underway please help by putting in your real life age.")
    print("(This is completely confidential)")

    age = input()
    print("Your age is "+ age)

    print("Now I just need to make sure I can do some easy math.")
    print("(Give me some numbers so I can do a math problem that involes (+,-,*,//))")
    print("For example ( (((12+2)*4)//6)-4) ) NO MORE THAN 5 NUMBERS!")

    a1 = input("Value a: ")
    b1 = input("Value b: ")
    c1 = input("Value c: ")
    d1 = input("Value d: ")
    e1 = input("Value e: ")

    a = int(a1)
    b = int(b1)
    c = int(c1)
    d = int(d1)
    e = int(e1)

    outcome = a+b*c//d-e
    print("Outcome = ", outcome)

    name = input("Please enter your name: ")
    x = 0
    while (x <20):
        print(name)
        x = x +2

    print("Now I am gonna need 3 numbers from you.")
    def smallnumber (num1, num2):
        if num1<num2:
            smallest = num1
        else:
            smallest = num2
        return smallest
    def main():
        choice1 = int(input("Please enter a number: "))
        choice2 = int(input("Please enter another number: "))

        smallerNumber = int(input("Enter a number: "))
        print("One of the numbers is", smallerNumber)

    main()

    my_list = [1,2,3,4]
    def append_list(my_list):
        my_list.append(12)

    append_list(my_list)
    print(my_list)

    

    print("Great! Now its time to select a role!")
    answer = input("Are you a Hunter or the Warlock? (hunter/warlock)")

    if answer.lower().strip() == "hunter":
        
        print("Welcome Hunter! Now I need to know a bit about you.")
        answer = input("Are you a Boy or a Girl? (boy/girl)")

        if answer.lower().strip() == "boy":
            answer = input("What is your age? (has to be above 18!!)")

            if int(answer) < 18:
                print("Sorry, go back to your parents you are not ready.")
                print("Try again when you are older.")

            elif int(answer) >= 18 and int(answer) <= 23:
                print("You are a new hunter!")
                answer = input("Do you want to continue? (yes/no)")

                if answer.lower().strip() == "yes":

                    print("Great! Welcome to Camp Prust!")
                    print("I hope you can make yourself comfortable here.")
                    
                    import time      
                    time.sleep(1.5)
                    
                    print("We need food and supplies can you do one")
                    answer = input("Where would you rather go? (woods/settlement)")

                    if answer.lower().strip() == "woods":
                        print("Great! You are going to help us get some food!")
                        print("The people from Camp Prust love meats and berries,")
                        print("beware though Ogres wander in the woods at night.")
                        print("While hunting one of your fellow hunters get severely hurt,")
                        print("you only have 1 hour before it becomes dark.")
                        print("There is just enough time to get out of the woods.")
                        print("Sadly if you want to save the hunter you must stay during the night")

                        answer = input("What do you do? (leave him/help him)")

                        if answer.lower().strip() == "leave him":
                            print("You decided to leave the fellow hunter.")
                            print("As you leave you hear the hunters scream,")
                            print("it pierces your ears and the guilt sets in.")
                            print("You bring the food back to Prust.")
                            print("Some of the people realize the missing person.")
                            print("You see the family of the hunter in the distance.")
                            print("They comfront you and ask what happened.")

                            answer = input("How do you tell them he died? (left him/with honor)")

                            if answer.lower().strip() == "left him":
                                print("HOW COULD YOU!")
                                print("He trusted you with his life and you betrayed him.")
                                print("The people of Prust seem to be turning against you.")
                                print("Leave Prust and never return you traitor,")
                                print("you hear in the crowd.")
                                print("We will kill you if you stay here,")
                                print("you hear from another member of the crowd")
                                print("Adventurer I fear you are in danger here,")
                                print("and you have to leave, I am sorry.")
                                print("As you leave Prust you keep the food you gathered.")
                                print("10 days later")
                                print("You find yourself in the desert,")
                                print("you realize that you are running low on food and water.")
                                print("There is no oasis near by and you start to realize,")
                                print("this could be your last couple days but you must move forward.")
                                print("4 days later")
                                print("You have officially run out of food and water,")
                                print("You start to hallucinate and see things.")
                                print("In the distance you see a cactus and a lizard.")
                                print("The cactus has water in it which can help,")
                                print("the lizard would be good food.")

                                answer = input("Which do you choose? (lizard/cactus)")

                                if answer.lower().strip() == "lizard":
                                    print("You walk over to the lizard and kill it.")
                                    print("You make a fire and start to cook it.")
                                    print("As you cook it you go over to the cactus,")
                                    print("when you get to the cactus you cut it open and drink the water.")
                                    print("You then set up camp and sleep so that you can continue on.")
                                    print("The next day you see a town in the desert.")
                                    print("You have no clue who is in the town.")

                                    answer = input("Should you enter the town? (yes/no)")

                                    if answer.lower().strip() == "yes":
                                        print("You enter the town and the people of the town are very welcoming.")
                                        print("They offer you food, water, and shelter.")
                                        print("They only ask you help take out a druid that has been terrorizing their town.")
                                        print("The druid is a millenia old and very wise.")

                                        answer = input("Will you help the town? (yes/no)")
                                        
                                

                                    elif answer.lower().strip() == "no":
                                        print("You continue on your journey.")
                                        print("A couple days later you realize that you still need food.")
                                        print("You continue and find a dead animal on the ground.")
                                        print("Due to the lack of food you go and take the animal.")
                                        print("As you eat the animal there is a coyote that wants the food.")
                                        print("It sneaks up behind you and attacks and you were not ready.")
                                        print("The coyote ends up killing you for food.")
                                        print("GAME OVER! YOU DIED!")

                                        ################# END OF PATH #################
                                        
                                    

                                    
                                elif answer.lower().strip() == "cactus":
                                    print("You do to the cactus and cut it open and drink the water.")
                                    print("After you drink the water you look for the lizard.")
                                    print("The lizard is gone and now you have no food.")
                                    print("A long time later")
                                    print("30 days ago starvation set in,")
                                    print("You have yet to find any food.")
                                    print("4 days later")
                                    print("GAME OVER! YOU DIED! :(")

                                    ################# END OF PATH #################
                                    

                        elif answer.lower().strip() == "help him":
                            print("Thank you adventurer!")
                            print("We have to be quiet in order to escape,")
                            print("if we are not the Ogres will find us and eat us.")
                            print("The only way out is the way we came so we must hurry.")
                            print("You take the hunter and help him through the woods,")
                            print("You start to get close to the exit,")
                            print("you put him on his horse and he rides off to Prust.")
                            print("Thats when you hear something behind you,")
                            print("then everything goes black.")
                            print("You awaken at a Ogre village.")
                            print("There is a fire in front of you and you are tied to a log.")
                            print("You have none of your weapons and you start to look around,")
                            print("for something to get yourself free.")
                            print("You see a knife near your feet and the fire is behind you.")

                            answer = input("How will you escape? (cut out/ burn the rope)")

                            if answer.lower().strip() == "cut out":
                                print("You reach for the knife and grab it.")
                                print("You had no clue but it was a trap,")
                                print("The Ogres wanted you to grab the knife.")
                                print("They now decide to put you over the fire.")
                                print("You now have no way out and end up burning alive.")
                                print("GAME OVER! YOU DIED! :(")
                                
                                ################# END OF PATH #################
                                
                                
                            elif answer.lower().strip() == "burn the rope":
                                print("You start to wiggle towards the fire.")
                                print("The Ogres have no idea of what you doing.")
                                print("You get close to the fire and the rope starts to burn.")
                                print("In order to burn the rope, you must burn your hands.")
                                print("You take the sacrafice and burn your hands.")
                                print("After a bit you are free and sneak away.")
                                print("You make your way out of the woods,")
                                print("then you have to start wrapping your hands in cloth")
                                print("in order to protect them from futher harm.")
                                print("You escaped but lost your share of food because of the Ogres.")
                                print("Your hourse is gone and you must walk back to Prust.")
                                print("6 days later")
                                print("You arrived in Prust and you are greeted with open arms.")
                                print("You see the hunter you saved and he asks what happened to your hands.")
                                print("You explain to the crowd what happened and that you lost the food.")
                                print("They said that they are not worried about the food,")
                                print("They are more worried about your hands and healing them.")
                                print("They say that there is a healer in town who can help,")
                                print("or you can learn how to heal your hand.")

                                answer = input("What do you want to do? (healer/by yourself)")

                                if answer.lower().strip() == "healer":
                                    print("Welcome adventurer...")

                                    import time      
                                    time.sleep(1.5)

                                    print("You see a hooded figure in front of you.")
                                    print("I see your hand is severly burned.")
                                    print("I have two choices for you...")
                                    print("The first one is the double-edged potion.")
                                    print("The second is an herb that takes a while to work.")

                                    answer = input("Which one do you want? (herb/potion)")

                                    if answer.lower().strip() == "herb":
                                        print("4444")
                                    elif answer.lower().strip() == "potion":
                                        print("3333")
                                    
                                elif answer.lower().strip() == "by yourself":
                                    print("You know some basic healing strategies.")
                                    print("The most basic potion I know is the green potion.")
                                    print("This potion heals you but takes a day to work.")
                                    print("Or I could let myself heal over time.")

                                    answer = input("How should I heal myself? (over time/ green potion)")

                                    if answer.lower().strip() == "over time":
                                        print("9999")
                                    elif answer.lower().strip() == "green potion":
                                        print("6666")
                            
                                  

                    elif answer.lower().strip() == "settlement":
                        print("Cool! You are going to get our supplies!")
                        print("You need to make your way to Numenthorn.")
                        print("There you will find supplies that were stolen from us.")
                        print("The commoners there can be hostile so bring your weapons.")
                        print("You reach your Numenthorn and it is quiet.")
                        print("It looks like everyone left and in hurry.")
                        print("You hear a roar and look behind you and realize what scared them.")

                        import time
                        time.sleep(1)

                        print("A giant Basilisk is staring right at you.")
                        print("HURRY YOU MUST CHOOSE WHAT TO DO! (attack/hide)")

                        answer = input("What do you do?")
                                             

            elif int(answer) > 23 and int(answer) <= 50:
                print("Welcome experienced Hunter!")
                answer = input ("Are you ready to go? (yes/no)")

                if answer.lower().strip() == "yes":

                    print("Great! Welcome to Camp Prust!")
                    print("I hope you can make yourself comfortable here.")

                    import time      
                    time.sleep(1.5)
                    
                    print("We need food and supplies can you do one")
                    answer = input("Where would you rather go? (woods/settlement)")

                    if answer.lower().strip() == "woods":
                        print("Great! You are going to help us get some food!")
                        print("The people from Camp Prust love meats and berries,")
                        print("beware though Ogres wander in the woods at night.")
                        print("While hunting one of your fellow hunters get severely hurt,")
                        print("you only have 1 hour before it becomes dark.")
                        print("There is just enough time to get out of the woods.")
                        print("Sadly if you want to save the hunter you must stay during the night")

                        answer = input("What do you do? (leave him/help him)")

                        if answer.lower().strip() == "leave him":
                            print("You decided to leave the fellow hunter.")
                            print("As you leave you hear the hunters scream,")
                            print("it pierces your ears and the guilt sets in.")
                            print("You bring the food back to Prust.")
                            print("Some of the people realize the missing person.")
                            print("You see the family of the hunter in the distance.")
                            print("They comfront you and ask what happened.")

                            answer = input("How do you tell them he died? (left him/with honor)")

                            if answer.lower().strip() == "left him":
                                print("HOW COULD YOU!")
                                print("He trusted you with his life and you betrayed him.")
                                print("The people of Prust seem to be turning against you.")
                                print("Leave Prust and never return you traitor,")
                                print("you hear in the crowd.")
                                print("We will kill you if you stay here,")
                                print("you hear from another member of the crowd")
                                print("Adventurer I fear you are in danger here,")
                                print("and you have to leave, I am sorry.")
                                print("As you leave Prust you keep the food you gathered.")
                                print("10 days later")
                                print("You find yourself in the desert,")
                                print("you realize that you are running low on food and water.")
                                print("There is no oasis near by and you start to realize,")
                                print("this could be your last couple days but you must move forward.")
                                print("4 days later")
                                print("You have officially run out of food and water,")
                                print("You start to hallucinate and see things.")
                                print("In the distance you see a cactus and a lizard.")
                                print("The cactus has water in it which can help,")
                                print("the lizard would be good food.")

                                answer = input("Which do you choose? (lizard/cactus)")

                                if answer.lower().strip() == "lizard":
                                    print("You walk over to the lizard and kill it.")
                                    print("You make a fire and start to cook it.")
                                    print("As you cook it you go over to the cactus,")
                                    print("when you get to the cactus you cut it open and drink the water.")
                                    print("You then set up camp and sleep so that you can continue on.")
                                    print("The next day you see a town in the desert.")
                                    print("You have no clue who is in the town.")

                                    answer = input("Should you enter the town? (yes/no)")

                                    if answer.lower().strip() == "yes":
                                        print("You enter the town and the people of the town are very welcoming.")
                                        print("They offer you food, water, and shelter.")
                                        print("They only ask you help take out a druid that has been terrorizing their town.")
                                        print("The druid is a millenia old and very wise.")

                                        answer = input("Will you help the town? (yes/no)")
                                        
                                

                                    elif answer.lower().strip() == "no":
                                        print("You continue on your journey.")
                                        print("A couple days later you realize that you still need food.")
                                        print("You continue and find a dead animal on the ground.")
                                        print("Due to the lack of food you go and take the animal.")
                                        print("As you eat the animal there is a coyote that wants the food.")
                                        print("It sneaks up behind you and attacks and you were not ready.")
                                        print("The coyote ends up killing you for food.")
                                        print("GAME OVER! YOU DIED!")

                                        ################# END OF PATH #################
                                        
                                    

                                    
                                elif answer.lower().strip() == "cactus":
                                    print("You do to the cactus and cut it open and drink the water.")
                                    print("After you drink the water you look for the lizard.")
                                    print("The lizard is gone and now you have no food.")
                                    print("A long time later")
                                    print("30 days ago starvation set in,")
                                    print("You have yet to find any food.")
                                    print("4 days later")
                                    print("GAME OVER! YOU DIED! :(")

                                    ################# END OF PATH #################
                                    

                        elif answer.lower().strip() == "help him":
                            print("Thank you adventurer!")
                            print("We have to be quiet in order to escape,")
                            print("if we are not the Ogres will find us and eat us.")
                            print("The only way out is the way we came so we must hurry.")
                            print("You take the hunter and help him through the woods,")
                            print("You start to get close to the exit,")
                            print("you put him on his horse and he rides off to Prust.")
                            print("Thats when you hear something behind you,")
                            print("then everything goes black.")
                            print("You awaken at a Ogre village.")
                            print("There is a fire in front of you and you are tied to a log.")
                            print("You have none of your weapons and you start to look around,")
                            print("for something to get yourself free.")
                            print("You see a knife near your feet and the fire is behind you.")

                            answer = input("How will you escape? (cut out/ burn the rope)")

                            if answer.lower().strip() == "cut out":
                                print("You reach for the knife and grab it.")
                                print("You had no clue but it was a trap,")
                                print("The Ogres wanted you to grab the knife.")
                                print("They now decide to put you over the fire.")
                                print("You now have no way out and end up burning alive.")
                                print("GAME OVER! YOU DIED! :(")
                                
                                ################# END OF PATH #################
                                
                                
                            elif answer.lower().strip() == "burn the rope":
                                print("You start to wiggle towards the fire.")
                                print("The Ogres have no idea of what you doing.")
                                print("You get close to the fire and the rope starts to burn.")
                                print("In order to burn the rope, you must burn your hands.")
                                print("You take the sacrafice and burn your hands.")
                                print("After a bit you are free and sneak away.")
                                print("You make your way out of the woods,")
                                print("then you have to start wrapping your hands in cloth")
                                print("in order to protect them from futher harm.")
                                print("You escaped but lost your share of food because of the Ogres.")
                                print("Your hourse is gone and you must walk back to Prust.")
                                print("6 days later")
                                print("You arrived in Prust and you are greeted with open arms.")
                                print("You see the hunter you saved and he asks what happened to your hands.")
                                print("You explain to the crowd what happened and that you lost the food.")
                                print("They said that they are not worried about the food,")
                                print("They are more worried about your hands and healing them.")
                                print("They say that there is a healer in town who can help,")
                                print("or you can learn how to heal your hand.")

                                answer = input("What do you want to do? (healer/by yourself)")

                                if answer.lower().strip() == "healer":
                                    print("Welcome adventurer...")

                                    import time      
                                    time.sleep(1.5)

                                    print("You see a hooded figure in front of you.")
                                    print("I see your hand is severly burned.")
                                    print("I have two choices for you...")
                                    print("The first one is the double-edged potion.")
                                    print("The second is an herb that takes a while to work.")

                                    answer = input("Which one do you want? (herb/potion)")

                                    if answer.lower().strip() == "herb":
                                        print("4444")
                                    elif answer.lower().strip() == "potion":
                                        print("3333")
                                    
                                elif answer.lower().strip() == "by yourself":
                                    print("You know some basic healing strategies.")
                                    print("The most basic potion I know is the green potion.")
                                    print("This potion heals you but takes a day to work.")
                                    print("Or I could let myself heal over time.")

                                    answer = input("How should I heal myself? (over time/ green potion)")

                                    if answer.lower().strip() == "over time":
                                        print("9999")
                                    elif answer.lower().strip() == "green potion":
                                        print("6666")
                            
                                  

                    elif answer.lower().strip() == "settlement":
                        print("Cool! You are going to get our supplies!")
                        print("You need to make your way to Numenthorn.")
                        print("There you will find supplies that were stolen from us.")
                        print("The commoners there can be hostile so bring your weapons.")
                        print("You reach your Numenthorn and it is quiet.")
                        print("It looks like everyone left and in hurry.")
                        print("You hear a roar and look behind you and realize what scared them.")

                        import time
                        time.sleep(1)

                        print("A giant Basilisk is staring right at you.")
                        print("HURRY YOU MUST CHOOSE WHAT TO DO! (attack/hide)")

                        answer = input("What do you do?")

            elif int(answer) > 50 and answer <= 80:
                print("You are getting old Hunter. Your age may hurt you.")
                answer = input ("Do you want to continue? (yes/no)")

                if answer.lower().strip() == "yes":

                    print("Great! Welcome to Camp Prust!")
                    print("I hope you can make yourself comfortable here.")

                    import time      
                    time.sleep(1.5)
                    
                    print("We need food and supplies can you do one")
                    answer = input("Where would you rather go? (woods/settlement)")

                    if answer.lower().strip() == "woods":
                        print("Great! You are going to help us get some food!")
                        print("The people from Camp Prust love meats and berries,")
                        print("beware though Ogres wander in the woods at night.")
                        print("While hunting one of your fellow hunters get severely hurt,")
                        print("you only have 1 hour before it becomes dark.")
                        print("There is just enough time to get out of the woods.")
                        print("Sadly if you want to save the hunter you must stay during the night")

                        answer = input("What do you do? (leave him/help him)")

                        if answer.lower().strip() == "leave him":
                            print("You decided to leave the fellow hunter.")
                            print("As you leave you hear the hunters scream,")
                            print("it pierces your ears and the guilt sets in.")
                            print("You bring the food back to Prust.")
                            print("Some of the people realize the missing person.")
                            print("You see the family of the hunter in the distance.")
                            print("They comfront you and ask what happened.")

                            answer = input("How do you tell them he died? (left him/with honor)")

                            if answer.lower().strip() == "left him":
                                print("HOW COULD YOU!")
                                print("He trusted you with his life and you betrayed him.")
                                print("The people of Prust seem to be turning against you.")
                                print("Leave Prust and never return you traitor,")
                                print("you hear in the crowd.")
                                print("We will kill you if you stay here,")
                                print("you hear from another member of the crowd")
                                print("Adventurer I fear you are in danger here,")
                                print("and you have to leave, I am sorry.")
                                print("As you leave Prust you keep the food you gathered.")
                                print("10 days later")
                                print("You find yourself in the desert,")
                                print("you realize that you are running low on food and water.")
                                print("There is no oasis near by and you start to realize,")
                                print("this could be your last couple days but you must move forward.")
                                print("4 days later")
                                print("You have officially run out of food and water,")
                                print("You start to hallucinate and see things.")
                                print("In the distance you see a cactus and a lizard.")
                                print("The cactus has water in it which can help,")
                                print("the lizard would be good food.")

                                answer = input("Which do you choose? (lizard/cactus)")

                                if answer.lower().strip() == "lizard":
                                    print("You walk over to the lizard and kill it.")
                                    print("You make a fire and start to cook it.")
                                    print("As you cook it you go over to the cactus,")
                                    print("when you get to the cactus you cut it open and drink the water.")
                                    print("You then set up camp and sleep so that you can continue on.")
                                    print("The next day you see a town in the desert.")
                                    print("You have no clue who is in the town.")

                                    answer = input("Should you enter the town? (yes/no)")

                                    if answer.lower().strip() == "yes":
                                        print("You enter the town and the people of the town are very welcoming.")
                                        print("They offer you food, water, and shelter.")
                                        print("They only ask you help take out a druid that has been terrorizing their town.")
                                        print("The druid is a millenia old and very wise.")

                                        answer = input("Will you help the town? (yes/no)")
                                        
                                

                                    elif answer.lower().strip() == "no":
                                        print("You continue on your journey.")
                                        print("A couple days later you realize that you still need food.")
                                        print("You continue and find a dead animal on the ground.")
                                        print("Due to the lack of food you go and take the animal.")
                                        print("As you eat the animal there is a coyote that wants the food.")
                                        print("It sneaks up behind you and attacks and you were not ready.")
                                        print("The coyote ends up killing you for food.")
                                        print("GAME OVER! YOU DIED!")

                                        ################# END OF PATH #################
                                        
                                    

                                    
                                elif answer.lower().strip() == "cactus":
                                    print("You do to the cactus and cut it open and drink the water.")
                                    print("After you drink the water you look for the lizard.")
                                    print("The lizard is gone and now you have no food.")
                                    print("A long time later")
                                    print("30 days ago starvation set in,")
                                    print("You have yet to find any food.")
                                    print("4 days later")
                                    print("GAME OVER! YOU DIED! :(")

                                    ################# END OF PATH #################
                                    

                        elif answer.lower().strip() == "help him":
                            print("Thank you adventurer!")
                            print("We have to be quiet in order to escape,")
                            print("if we are not the Ogres will find us and eat us.")
                            print("The only way out is the way we came so we must hurry.")
                            print("You take the hunter and help him through the woods,")
                            print("You start to get close to the exit,")
                            print("you put him on his horse and he rides off to Prust.")
                            print("Thats when you hear something behind you,")
                            print("then everything goes black.")
                            print("You awaken at a Ogre village.")
                            print("There is a fire in front of you and you are tied to a log.")
                            print("You have none of your weapons and you start to look around,")
                            print("for something to get yourself free.")
                            print("You see a knife near your feet and the fire is behind you.")

                            answer = input("How will you escape? (cut out/ burn the rope)")

                            if answer.lower().strip() == "cut out":
                                print("You reach for the knife and grab it.")
                                print("You had no clue but it was a trap,")
                                print("The Ogres wanted you to grab the knife.")
                                print("They now decide to put you over the fire.")
                                print("You now have no way out and end up burning alive.")
                                print("GAME OVER! YOU DIED! :(")
                                
                                ################# END OF PATH #################
                                
                                
                            elif answer.lower().strip() == "burn the rope":
                                print("You start to wiggle towards the fire.")
                                print("The Ogres have no idea of what you doing.")
                                print("You get close to the fire and the rope starts to burn.")
                                print("In order to burn the rope, you must burn your hands.")
                                print("You take the sacrafice and burn your hands.")
                                print("After a bit you are free and sneak away.")
                                print("You make your way out of the woods,")
                                print("then you have to start wrapping your hands in cloth")
                                print("in order to protect them from futher harm.")
                                print("You escaped but lost your share of food because of the Ogres.")
                                print("Your hourse is gone and you must walk back to Prust.")
                                print("6 days later")
                                print("You arrived in Prust and you are greeted with open arms.")
                                print("You see the hunter you saved and he asks what happened to your hands.")
                                print("You explain to the crowd what happened and that you lost the food.")
                                print("They said that they are not worried about the food,")
                                print("They are more worried about your hands and healing them.")
                                print("They say that there is a healer in town who can help,")
                                print("or you can learn how to heal your hand.")

                                answer = input("What do you want to do? (healer/by yourself)")

                                if answer.lower().strip() == "healer":
                                    print("Welcome adventurer...")

                                    import time      
                                    time.sleep(1.5)

                                    print("You see a hooded figure in front of you.")
                                    print("I see your hand is severly burned.")
                                    print("I have two choices for you...")
                                    print("The first one is the double-edged potion.")
                                    print("The second is an herb that takes a while to work.")

                                    answer = input("Which one do you want? (herb/potion)")

                                    if answer.lower().strip() == "herb":
                                        print("4444")
                                    elif answer.lower().strip() == "potion":
                                        print("3333")
                                    
                                elif answer.lower().strip() == "by yourself":
                                    print("You know some basic healing strategies.")
                                    print("The most basic potion I know is the green potion.")
                                    print("This potion heals you but takes a day to work.")
                                    print("Or I could let myself heal over time.")

                                    answer = input("How should I heal myself? (over time/ green potion)")

                                    if answer.lower().strip() == "over time":
                                        print("9999")
                                    elif answer.lower().strip() == "green potion":
                                        print("6666")
                            
                                  

                    elif answer.lower().strip() == "settlement":
                        print("Cool! You are going to get our supplies!")
                        print("You need to make your way to Numenthorn.")
                        print("There you will find supplies that were stolen from us.")
                        print("The commoners there can be hostile so bring your weapons.")
                        print("You reach your Numenthorn and it is quiet.")
                        print("It looks like everyone left and in hurry.")
                        print("You hear a roar and look behind you and realize what scared them.")

                        import time
                        time.sleep(1)

                        print("A giant Basilisk is staring right at you.")
                        print("HURRY YOU MUST CHOOSE WHAT TO DO! (attack/hide)")

                        answer = input("What do you do?")

            elif int(answer) > 80:
                print("Sorry, but you are too old Hunter.")
                print("Your age will only hold you back.")
                

        elif answer.lower.strip() == "girl":
            answer = input("What is your age? (has to be above 18!!)")

            if int(answer) < 18:
                print("Sorry, go back to your parents you are not ready.")
                print("Try again when you are older.")

            elif int(answer) >= 18 and int(answer) <= 23:
                print("You are a new hunter!")
                answer = input("Do you want to continue? (yes/no)")

                if answer.lower().strip() == "yes":

                    print("Great! Welcome to Camp Prust!")
                    print("I hope you can make yourself comfortable here.")

                    import time      
                    time.sleep(1.5)
                    
                    print("We need food and supplies can you do one")
                    answer = input("Where would you rather go? (woods/settlement)")

                    if answer.lower().strip() == "woods":
                        print("Great! You are going to help us get some food!")
                        print("The people from Camp Prust love meats and berries,")
                        print("beware though Ogres wander in the woods at night.")
                        print("While hunting one of your fellow hunters get severely hurt,")
                        print("you only have 1 hour before it becomes dark.")
                        print("There is just enough time to get out of the woods.")
                        print("Sadly if you want to save the hunter you must stay during the night")

                        answer = input("What do you do? (leave him/help him)")

                        if answer.lower().strip() == "leave him":
                            print("You decided to leave the fellow hunter.")
                            print("As you leave you hear the hunters scream,")
                            print("it pierces your ears and the guilt sets in.")
                            print("You bring the food back to Prust.")
                            print("Some of the people realize the missing person.")
                            print("You see the family of the hunter in the distance.")
                            print("They comfront you and ask what happened.")

                            answer = input("How do you tell them he died? (left him/with honor)")

                            if answer.lower().strip() == "left him":
                                print("HOW COULD YOU!")
                                print("He trusted you with his life and you betrayed him.")
                                print("The people of Prust seem to be turning against you.")
                                print("Leave Prust and never return you traitor,")
                                print("you hear in the crowd.")
                                print("We will kill you if you stay here,")
                                print("you hear from another member of the crowd")
                                print("Adventurer I fear you are in danger here,")
                                print("and you have to leave, I am sorry.")
                                print("As you leave Prust you keep the food you gathered.")
                                print("10 days later")
                                print("You find yourself in the desert,")
                                print("you realize that you are running low on food and water.")
                                print("There is no oasis near by and you start to realize,")
                                print("this could be your last couple days but you must move forward.")
                                print("4 days later")
                                print("You have officially run out of food and water,")
                                print("You start to hallucinate and see things.")
                                print("In the distance you see a cactus and a lizard.")
                                print("The cactus has water in it which can help,")
                                print("the lizard would be good food.")

                                answer = input("Which do you choose? (lizard/cactus)")

                                if answer.lower().strip() == "lizard":
                                    print("You walk over to the lizard and kill it.")
                                    print("You make a fire and start to cook it.")
                                    print("As you cook it you go over to the cactus,")
                                    print("when you get to the cactus you cut it open and drink the water.")
                                    print("You then set up camp and sleep so that you can continue on.")
                                    print("The next day you see a town in the desert.")
                                    print("You have no clue who is in the town.")

                                    answer = input("Should you enter the town? (yes/no)")

                                    if answer.lower().strip() == "yes":
                                        print("You enter the town and the people of the town are very welcoming.")
                                        print("They offer you food, water, and shelter.")
                                        print("They only ask you help take out a druid that has been terrorizing their town.")
                                        print("The druid is a millenia old and very wise.")

                                        answer = input("Will you help the town? (yes/no)")
                                        
                                

                                    elif answer.lower().strip() == "no":
                                        print("You continue on your journey.")
                                        print("A couple days later you realize that you still need food.")
                                        print("You continue and find a dead animal on the ground.")
                                        print("Due to the lack of food you go and take the animal.")
                                        print("As you eat the animal there is a coyote that wants the food.")
                                        print("It sneaks up behind you and attacks and you were not ready.")
                                        print("The coyote ends up killing you for food.")
                                        print("GAME OVER! YOU DIED!")

                                        ################# END OF PATH #################
                                        
                                    

                                    
                                elif answer.lower().strip() == "cactus":
                                    print("You do to the cactus and cut it open and drink the water.")
                                    print("After you drink the water you look for the lizard.")
                                    print("The lizard is gone and now you have no food.")
                                    print("A long time later")
                                    print("30 days ago starvation set in,")
                                    print("You have yet to find any food.")
                                    print("4 days later")
                                    print("GAME OVER! YOU DIED! :(")

                                    ################# END OF PATH #################
                                    

                        elif answer.lower().strip() == "help him":
                            print("Thank you adventurer!")
                            print("We have to be quiet in order to escape,")
                            print("if we are not the Ogres will find us and eat us.")
                            print("The only way out is the way we came so we must hurry.")
                            print("You take the hunter and help him through the woods,")
                            print("You start to get close to the exit,")
                            print("you put him on his horse and he rides off to Prust.")
                            print("Thats when you hear something behind you,")
                            print("then everything goes black.")
                            print("You awaken at a Ogre village.")
                            print("There is a fire in front of you and you are tied to a log.")
                            print("You have none of your weapons and you start to look around,")
                            print("for something to get yourself free.")
                            print("You see a knife near your feet and the fire is behind you.")

                            answer = input("How will you escape? (cut out/ burn the rope)")

                            if answer.lower().strip() == "cut out":
                                print("You reach for the knife and grab it.")
                                print("You had no clue but it was a trap,")
                                print("The Ogres wanted you to grab the knife.")
                                print("They now decide to put you over the fire.")
                                print("You now have no way out and end up burning alive.")
                                print("GAME OVER! YOU DIED! :(")
                                
                                ################# END OF PATH #################
                                
                                
                            elif answer.lower().strip() == "burn the rope":
                                print("You start to wiggle towards the fire.")
                                print("The Ogres have no idea of what you doing.")
                                print("You get close to the fire and the rope starts to burn.")
                                print("In order to burn the rope, you must burn your hands.")
                                print("You take the sacrafice and burn your hands.")
                                print("After a bit you are free and sneak away.")
                                print("You make your way out of the woods,")
                                print("then you have to start wrapping your hands in cloth")
                                print("in order to protect them from futher harm.")
                                print("You escaped but lost your share of food because of the Ogres.")
                                print("Your hourse is gone and you must walk back to Prust.")
                                print("6 days later")
                                print("You arrived in Prust and you are greeted with open arms.")
                                print("You see the hunter you saved and he asks what happened to your hands.")
                                print("You explain to the crowd what happened and that you lost the food.")
                                print("They said that they are not worried about the food,")
                                print("They are more worried about your hands and healing them.")
                                print("They say that there is a healer in town who can help,")
                                print("or you can learn how to heal your hand.")

                                answer = input("What do you want to do? (healer/by yourself)")

                                if answer.lower().strip() == "healer":
                                    print("Welcome adventurer...")

                                    import time      
                                    time.sleep(1.5)

                                    print("You see a hooded figure in front of you.")
                                    print("I see your hand is severly burned.")
                                    print("I have two choices for you...")
                                    print("The first one is the double-edged potion.")
                                    print("The second is an herb that takes a while to work.")

                                    answer = input("Which one do you want? (herb/potion)")

                                    if answer.lower().strip() == "herb":
                                        print("4444")
                                    elif answer.lower().strip() == "potion":
                                        print("3333")
                                    
                                elif answer.lower().strip() == "by yourself":
                                    print("You know some basic healing strategies.")
                                    print("The most basic potion I know is the green potion.")
                                    print("This potion heals you but takes a day to work.")
                                    print("Or I could let myself heal over time.")

                                    answer = input("How should I heal myself? (over time/ green potion)")

                                    if answer.lower().strip() == "over time":
                                        print("9999")
                                    elif answer.lower().strip() == "green potion":
                                        print("6666")
                            
                                  

                    elif answer.lower().strip() == "settlement":
                        print("Cool! You are going to get our supplies!")
                        print("You need to make your way to Numenthorn.")
                        print("There you will find supplies that were stolen from us.")
                        print("The commoners there can be hostile so bring your weapons.")
                        print("You reach your Numenthorn and it is quiet.")
                        print("It looks like everyone left and in hurry.")
                        print("You hear a roar and look behind you and realize what scared them.")

                        import time
                        time.sleep(1)

                        print("A giant Basilisk is staring right at you.")
                        print("HURRY YOU MUST CHOOSE WHAT TO DO! (attack/hide)")

                        answer = input("What do you do?")
                                   

            elif int(answer) > 23 and int(answer) <= 50:
                print("Welcome experienced Hunter!")
                answer = input ("Are you ready to go? (yes/no)")

                if answer.lower().strip() == "yes":

                    print("Great! Welcome to Camp Prust!")
                    print("I hope you can make yourself comfortable here.")

                    import time      
                    time.sleep(1.5)
                    
                    print("We need food and supplies can you do one")
                    answer = input("Where would you rather go? (woods/settlement)")

                    if answer.lower().strip() == "woods":
                        print("Great! You are going to help us get some food!")
                        print("The people from Camp Prust love meats and berries,")
                        print("beware though Ogres wander in the woods at night.")
                        print("While hunting one of your fellow hunters get severely hurt,")
                        print("you only have 1 hour before it becomes dark.")
                        print("There is just enough time to get out of the woods.")
                        print("Sadly if you want to save the hunter you must stay during the night")

                        answer = input("What do you do? (leave him/help him)")

                        if answer.lower().strip() == "leave him":
                            print("You decided to leave the fellow hunter.")
                            print("As you leave you hear the hunters scream,")
                            print("it pierces your ears and the guilt sets in.")
                            print("You bring the food back to Prust.")
                            print("Some of the people realize the missing person.")
                            print("You see the family of the hunter in the distance.")
                            print("They comfront you and ask what happened.")

                            answer = input("How do you tell them he died? (left him/with honor)")

                            if answer.lower().strip() == "left him":
                                print("HOW COULD YOU!")
                                print("He trusted you with his life and you betrayed him.")
                                print("The people of Prust seem to be turning against you.")
                                print("Leave Prust and never return you traitor,")
                                print("you hear in the crowd.")
                                print("We will kill you if you stay here,")
                                print("you hear from another member of the crowd")
                                print("Adventurer I fear you are in danger here,")
                                print("and you have to leave, I am sorry.")
                                print("As you leave Prust you keep the food you gathered.")
                                print("10 days later")
                                print("You find yourself in the desert,")
                                print("you realize that you are running low on food and water.")
                                print("There is no oasis near by and you start to realize,")
                                print("this could be your last couple days but you must move forward.")
                                print("4 days later")
                                print("You have officially run out of food and water,")
                                print("You start to hallucinate and see things.")
                                print("In the distance you see a cactus and a lizard.")
                                print("The cactus has water in it which can help,")
                                print("the lizard would be good food.")

                                answer = input("Which do you choose? (lizard/cactus)")

                                if answer.lower().strip() == "lizard":
                                    print("You walk over to the lizard and kill it.")
                                    print("You make a fire and start to cook it.")
                                    print("As you cook it you go over to the cactus,")
                                    print("when you get to the cactus you cut it open and drink the water.")
                                    print("You then set up camp and sleep so that you can continue on.")
                                    print("The next day you see a town in the desert.")
                                    print("You have no clue who is in the town.")

                                    answer = input("Should you enter the town? (yes/no)")

                                    if answer.lower().strip() == "yes":
                                        print("You enter the town and the people of the town are very welcoming.")
                                        print("They offer you food, water, and shelter.")
                                        print("They only ask you help take out a druid that has been terrorizing their town.")
                                        print("The druid is a millenia old and very wise.")

                                        answer = input("Will you help the town? (yes/no)")
                                        
                                

                                    elif answer.lower().strip() == "no":
                                        print("You continue on your journey.")
                                        print("A couple days later you realize that you still need food.")
                                        print("You continue and find a dead animal on the ground.")
                                        print("Due to the lack of food you go and take the animal.")
                                        print("As you eat the animal there is a coyote that wants the food.")
                                        print("It sneaks up behind you and attacks and you were not ready.")
                                        print("The coyote ends up killing you for food.")
                                        print("GAME OVER! YOU DIED!")

                                        ################# END OF PATH #################
                                        
                                    

                                    
                                elif answer.lower().strip() == "cactus":
                                    print("You do to the cactus and cut it open and drink the water.")
                                    print("After you drink the water you look for the lizard.")
                                    print("The lizard is gone and now you have no food.")
                                    print("A long time later")
                                    print("30 days ago starvation set in,")
                                    print("You have yet to find any food.")
                                    print("4 days later")
                                    print("GAME OVER! YOU DIED! :(")

                                    ################# END OF PATH #################
                                    

                        elif answer.lower().strip() == "help him":
                            print("Thank you adventurer!")
                            print("We have to be quiet in order to escape,")
                            print("if we are not the Ogres will find us and eat us.")
                            print("The only way out is the way we came so we must hurry.")
                            print("You take the hunter and help him through the woods,")
                            print("You start to get close to the exit,")
                            print("you put him on his horse and he rides off to Prust.")
                            print("Thats when you hear something behind you,")
                            print("then everything goes black.")
                            print("You awaken at a Ogre village.")
                            print("There is a fire in front of you and you are tied to a log.")
                            print("You have none of your weapons and you start to look around,")
                            print("for something to get yourself free.")
                            print("You see a knife near your feet and the fire is behind you.")

                            answer = input("How will you escape? (cut out/ burn the rope)")

                            if answer.lower().strip() == "cut out":
                                print("You reach for the knife and grab it.")
                                print("You had no clue but it was a trap,")
                                print("The Ogres wanted you to grab the knife.")
                                print("They now decide to put you over the fire.")
                                print("You now have no way out and end up burning alive.")
                                print("GAME OVER! YOU DIED! :(")
                                
                                ################# END OF PATH #################
                                
                                
                            elif answer.lower().strip() == "burn the rope":
                                print("You start to wiggle towards the fire.")
                                print("The Ogres have no idea of what you doing.")
                                print("You get close to the fire and the rope starts to burn.")
                                print("In order to burn the rope, you must burn your hands.")
                                print("You take the sacrafice and burn your hands.")
                                print("After a bit you are free and sneak away.")
                                print("You make your way out of the woods,")
                                print("then you have to start wrapping your hands in cloth")
                                print("in order to protect them from futher harm.")
                                print("You escaped but lost your share of food because of the Ogres.")
                                print("Your hourse is gone and you must walk back to Prust.")
                                print("6 days later")
                                print("You arrived in Prust and you are greeted with open arms.")
                                print("You see the hunter you saved and he asks what happened to your hands.")
                                print("You explain to the crowd what happened and that you lost the food.")
                                print("They said that they are not worried about the food,")
                                print("They are more worried about your hands and healing them.")
                                print("They say that there is a healer in town who can help,")
                                print("or you can learn how to heal your hand.")

                                answer = input("What do you want to do? (healer/by yourself)")

                                if answer.lower().strip() == "healer":
                                    print("Welcome adventurer...")

                                    import time      
                                    time.sleep(1.5)

                                    print("You see a hooded figure in front of you.")
                                    print("I see your hand is severly burned.")
                                    print("I have two choices for you...")
                                    print("The first one is the double-edged potion.")
                                    print("The second is an herb that takes a while to work.")

                                    answer = input("Which one do you want? (herb/potion)")

                                    if answer.lower().strip() == "herb":
                                        print("4444")
                                    elif answer.lower().strip() == "potion":
                                        print("3333")
                                    
                                elif answer.lower().strip() == "by yourself":
                                    print("You know some basic healing strategies.")
                                    print("The most basic potion I know is the green potion.")
                                    print("This potion heals you but takes a day to work.")
                                    print("Or I could let myself heal over time.")

                                    answer = input("How should I heal myself? (over time/ green potion)")

                                    if answer.lower().strip() == "over time":
                                        print("9999")
                                    elif answer.lower().strip() == "green potion":
                                        print("6666")
                            
                                  

                    elif answer.lower().strip() == "settlement":
                        print("Cool! You are going to get our supplies!")
                        print("You need to make your way to Numenthorn.")
                        print("There you will find supplies that were stolen from us.")
                        print("The commoners there can be hostile so bring your weapons.")
                        print("You reach your Numenthorn and it is quiet.")
                        print("It looks like everyone left and in hurry.")
                        print("You hear a roar and look behind you and realize what scared them.")

                        import time
                        time.sleep(1)

                        print("A giant Basilisk is staring right at you.")
                        print("HURRY YOU MUST CHOOSE WHAT TO DO! (attack/hide)")

                        answer = input("What do you do?")

            elif int(answer) > 50 and answer <= 80:
                print("You are getting old Hunter. Your age may hurt you.")
                answer = input ("Do you want to continue? (yes/no)")

                if answer.lower().strip() == "yes":

                    print("Great! Welcome to Camp Prust!")
                    print("I hope you can make yourself comfortable here.")

                    import time      
                    time.sleep(1.5)
                    
                    print("We need food and supplies can you do one")
                    answer = input("Where would you rather go? (woods/settlement)")

                    if answer.lower().strip() == "woods":
                        print("Great! You are going to help us get some food!")
                        print("The people from Camp Prust love meats and berries,")
                        print("beware though Ogres wander in the woods at night.")
                        print("While hunting one of your fellow hunters get severely hurt,")
                        print("you only have 1 hour before it becomes dark.")
                        print("There is just enough time to get out of the woods.")
                        print("Sadly if you want to save the hunter you must stay during the night")

                        answer = input("What do you do? (leave him/help him)")

                        if answer.lower().strip() == "leave him":
                            print("You decided to leave the fellow hunter.")
                            print("As you leave you hear the hunters scream,")
                            print("it pierces your ears and the guilt sets in.")
                            print("You bring the food back to Prust.")
                            print("Some of the people realize the missing person.")
                            print("You see the family of the hunter in the distance.")
                            print("They comfront you and ask what happened.")

                            answer = input("How do you tell them he died? (left him/with honor)")

                            if answer.lower().strip() == "left him":
                                print("HOW COULD YOU!")
                                print("He trusted you with his life and you betrayed him.")
                                print("The people of Prust seem to be turning against you.")
                                print("Leave Prust and never return you traitor,")
                                print("you hear in the crowd.")
                                print("We will kill you if you stay here,")
                                print("you hear from another member of the crowd")
                                print("Adventurer I fear you are in danger here,")
                                print("and you have to leave, I am sorry.")
                                print("As you leave Prust you keep the food you gathered.")
                                print("10 days later")
                                print("You find yourself in the desert,")
                                print("you realize that you are running low on food and water.")
                                print("There is no oasis near by and you start to realize,")
                                print("this could be your last couple days but you must move forward.")
                                print("4 days later")
                                print("You have officially run out of food and water,")
                                print("You start to hallucinate and see things.")
                                print("In the distance you see a cactus and a lizard.")
                                print("The cactus has water in it which can help,")
                                print("the lizard would be good food.")

                                answer = input("Which do you choose? (lizard/cactus)")

                                if answer.lower().strip() == "lizard":
                                    print("You walk over to the lizard and kill it.")
                                    print("You make a fire and start to cook it.")
                                    print("As you cook it you go over to the cactus,")
                                    print("when you get to the cactus you cut it open and drink the water.")
                                    print("You then set up camp and sleep so that you can continue on.")
                                    print("The next day you see a town in the desert.")
                                    print("You have no clue who is in the town.")

                                    answer = input("Should you enter the town? (yes/no)")

                                    if answer.lower().strip() == "yes":
                                        print("You enter the town and the people of the town are very welcoming.")
                                        print("They offer you food, water, and shelter.")
                                        print("They only ask you help take out a druid that has been terrorizing their town.")
                                        print("The druid is a millenia old and very wise.")

                                        answer = input("Will you help the town? (yes/no)")
                                        
                                

                                    elif answer.lower().strip() == "no":
                                        print("You continue on your journey.")
                                        print("A couple days later you realize that you still need food.")
                                        print("You continue and find a dead animal on the ground.")
                                        print("Due to the lack of food you go and take the animal.")
                                        print("As you eat the animal there is a coyote that wants the food.")
                                        print("It sneaks up behind you and attacks and you were not ready.")
                                        print("The coyote ends up killing you for food.")
                                        print("GAME OVER! YOU DIED!")

                                        ################# END OF PATH #################
                                        
                                    

                                    
                                elif answer.lower().strip() == "cactus":
                                    print("You do to the cactus and cut it open and drink the water.")
                                    print("After you drink the water you look for the lizard.")
                                    print("The lizard is gone and now you have no food.")
                                    print("A long time later")
                                    print("30 days ago starvation set in,")
                                    print("You have yet to find any food.")
                                    print("4 days later")
                                    print("GAME OVER! YOU DIED! :(")

                                    ################# END OF PATH #################
                                    

                        elif answer.lower().strip() == "help him":
                            print("Thank you adventurer!")
                            print("We have to be quiet in order to escape,")
                            print("if we are not the Ogres will find us and eat us.")
                            print("The only way out is the way we came so we must hurry.")
                            print("You take the hunter and help him through the woods,")
                            print("You start to get close to the exit,")
                            print("you put him on his horse and he rides off to Prust.")
                            print("Thats when you hear something behind you,")
                            print("then everything goes black.")
                            print("You awaken at a Ogre village.")
                            print("There is a fire in front of you and you are tied to a log.")
                            print("You have none of your weapons and you start to look around,")
                            print("for something to get yourself free.")
                            print("You see a knife near your feet and the fire is behind you.")

                            answer = input("How will you escape? (cut out/ burn the rope)")

                            if answer.lower().strip() == "cut out":
                                print("You reach for the knife and grab it.")
                                print("You had no clue but it was a trap,")
                                print("The Ogres wanted you to grab the knife.")
                                print("They now decide to put you over the fire.")
                                print("You now have no way out and end up burning alive.")
                                print("GAME OVER! YOU DIED! :(")
                                
                                ################# END OF PATH #################
                                
                                
                            elif answer.lower().strip() == "burn the rope":
                                print("You start to wiggle towards the fire.")
                                print("The Ogres have no idea of what you doing.")
                                print("You get close to the fire and the rope starts to burn.")
                                print("In order to burn the rope, you must burn your hands.")
                                print("You take the sacrafice and burn your hands.")
                                print("After a bit you are free and sneak away.")
                                print("You make your way out of the woods,")
                                print("then you have to start wrapping your hands in cloth")
                                print("in order to protect them from futher harm.")
                                print("You escaped but lost your share of food because of the Ogres.")
                                print("Your hourse is gone and you must walk back to Prust.")
                                print("6 days later")
                                print("You arrived in Prust and you are greeted with open arms.")
                                print("You see the hunter you saved and he asks what happened to your hands.")
                                print("You explain to the crowd what happened and that you lost the food.")
                                print("They said that they are not worried about the food,")
                                print("They are more worried about your hands and healing them.")
                                print("They say that there is a healer in town who can help,")
                                print("or you can learn how to heal your hand.")

                                answer = input("What do you want to do? (healer/by yourself)")

                                if answer.lower().strip() == "healer":
                                    print("Welcome adventurer...")

                                    import time      
                                    time.sleep(1.5)

                                    print("You see a hooded figure in front of you.")
                                    print("I see your hand is severly burned.")
                                    print("I have two choices for you...")
                                    print("The first one is the double-edged potion.")
                                    print("The second is an herb that takes a while to work.")

                                    answer = input("Which one do you want? (herb/potion)")

                                    if answer.lower().strip() == "herb":
                                        print("4444")
                                    elif answer.lower().strip() == "potion":
                                        print("3333")
                                    
                                elif answer.lower().strip() == "by yourself":
                                    print("You know some basic healing strategies.")
                                    print("The most basic potion I know is the green potion.")
                                    print("This potion heals you but takes a day to work.")
                                    print("Or I could let myself heal over time.")

                                    answer = input("How should I heal myself? (over time/ green potion)")

                                    if answer.lower().strip() == "over time":
                                        print("9999")
                                    elif answer.lower().strip() == "green potion":
                                        print("6666")
                            
                                  

                    elif answer.lower().strip() == "settlement":
                        print("Cool! You are going to get our supplies!")
                        print("You need to make your way to Numenthorn.")
                        print("There you will find supplies that were stolen from us.")
                        print("The commoners there can be hostile so bring your weapons.")
                        print("You reach your Numenthorn and it is quiet.")
                        print("It looks like everyone left and in hurry.")
                        print("You hear a roar and look behind you and realize what scared them.")

                        import time
                        time.sleep(1)

                        print("A giant Basilisk is staring right at you.")
                        print("HURRY YOU MUST CHOOSE WHAT TO DO! (attack/hide)")

                        answer = input("What do you do?")

            elif int(answer) > 80:
                print("Sorry, but you are too old Hunter.")
                print("Your age will only hold you back.")
            
        else:
            print("We respect your answer.")
            print("But it dosent fit the parameters of the game. :(")
        

    elif answer.lower().strip() == "warlock":
    #"elif" is another if statement (W3Schools)

        print("Welcome Warlock! Now I need to know a bit about you.")
        answer = input("Are you a Boy or a Girl? (boy/girl)")

        if answer.lower().strip() == "boy":
            answer = input("What is your age? (has to be above 18!!)")

            if int(answer) < 18:
                print("Sorry, go back to your parents you are not ready.")
                print("Try again when you are older.")

            elif int(answer) >= 18 and int(answer) <= 23:
                print("You are a new Warlock!")
                answer = input("Do you want to continue? (yes/no)")

                if answer.lower().strip() == "yes":

                    print("Great! Welcome to Fathomire!")
                    print("I hope you can make yourself comfortable here.")
                                   

            elif int(answer) > 23 and int(answer) <= 50:
                print("Welcome experienced Warlock!")
                answer = input ("Are you ready to go? (yes/no)")

                if answer.lower().strip() == "yes":

                    print("Great! Welcome to Fathomire!")
                    print("I hope you can make yourself comfortable here.")

            elif int(answer) > 50 and answer <= 80:
                print("You are getting old Warlock. Your age may hurt you.")
                answer = input ("Do you want to continue? (yes/no)")

                if answer.lower().strip() == "yes":

                    print("Great! Welcome to Fathomire!")
                    print("I hope you can make yourself comfortable here.")

            elif int(answer) > 80:
                print("Sorry, but you are too old Warlock.")
                print("Your age will only hold you back.")
                

        elif answer.lower.strip() == "girl":
            answer = input("What is your age? (has to be above 18!!)")

            if int(answer) < 18:
                print("Sorry, go back to your parents you are not ready.")
                print("Try again when you are older.")

            elif int(answer) >= 18 and int(answer) <= 23:
                print("You are a new Warlock!")
                answer = input("Do you want to continue? (yes/no)")

                if answer.lower().strip() == "yes":

                    print("Great! Welcome to Fathomire!")
                    print("I hope you can make yourself comfortable here.")
                                   

            elif int(answer) > 23 and int(answer) <= 50:
                print("Welcome experienced Warlock!")
                answer = input ("Are you ready to go? (yes/no)")

                if answer.lower().strip() == "yes":

                    print("Great! Welcome to Fathomire!")
                    print("I hope you can make yourself comfortable here.")

            elif int(answer) > 50 and answer <= 80:
                print("You are getting old Warlock. Your age may hurt you.")
                answer = input ("Do you want to continue? (yes/no)")

                if answer.lower().strip() == "yes":

                    print("Great! Welcome to Fathomire!")
                    print("I hope you can make yourself comfortable here.")

            elif int(answer) > 80:
                print("Sorry, but you are too old Warlock.")
                print("Your age will only hold you back.")
            
        else:
            print("We respect your answer.")
            print("But it dosent fit the parameters of the game. :(")
        

    

    else:
        print('Your choice is invalid...')
        
else:
    print("That's to bad! :(")
    


#Sprint 2
#Integrate new concepts (from ACM / IEEE)
#standard conditional structures / statements: if, if-else, if-elif, if-elif-else DONE!
#relational operators ( == != > >= < <= ) DONE!
#standard iterative structures: while, for DONE!
#function definitions (do not define a function inside another function, def should be at the left margin)DONE! 
#parameter passing (write a function that accepts parameters) DONE!
#do not use "global" DONE!
#Submission instructions: 
#Submit a PDF as before and...
#Create a GitHub repository for your program, upload your Main.py file through the browser, and submit a link to it 
