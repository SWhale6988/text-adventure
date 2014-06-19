                                                                     
#from shops import declareshops                                     
from quests import declarequests                                                                  
from items import declareitems
from rooms import declarerooms
import random
#shops = declareshops()
rooms = declarerooms()
items = declareitems()
quests = declarequests(items,rooms)
 #Defines items
rooms = declarerooms()


location = rooms["entrancegate"]

level = 1
strength = random.randint(1,5)
stamina = random.randint(1,5)    #defines stats
agility = random.randint(1,5) 
wisdom = random.randint(1,5) 
luck = random.randint(1,4)

questlist = []


questlist.append(quests[0])   #gives first quest
inventory = [[items["Pork Chop"],1],    [items["Wooden Sword"],1]       ]
gold = 20
stats = [level,strength,stamina,agility,wisdom,luck]   #Compiles stats into a list


while True:
    options = location[2] #Gets options
   #for x in range(len(questlist)):
       # if location == questlist[x+1][1]:
          #  inventory.append(questlist[x][2])

    
    print(location[0]) #Prints location name
    print("\n" + location[1])       #prints location information
    print("You may go to:")
            




        
    for count in range(len(options)):
        print(str(count+1) + ".     " + options[count][0])  #prints options
    choice = input('>  ') #gets user input

    if choice == "1" or choice == "2" or choice == "3" or choice == "4" or choice == "5": #tests if the input is an interger
        choice = int(choice) #if it is, converts it to an interger
        if choice < len(options)+1 and choice > 0: #If the choice is within the range of the options
            location = options[int(choice)-1] #Location changes
        else:
            print("Invalid choice") #Otherwise invalid choice. (repeats)





    elif choice == 'quests' or choice == "quests": #if user asks for quests
        print("\n")
        for count in range(len(quests)): #prints quests
            print(str(count+1) + ".     "+ quests[count][0])
            
        print("Select a quest to find out more information\n")
        choice = input('>  ') #gets user input



        if choice == "1" or choice == "2" or choice == "3" or choice == "4" or choice == "5":
            choice = int(choice) #changes choice to an interger
            
            if choice < len(options)+1 and choice > 0: #if choice is within the range of the options
                print(quests[choice-1][0]+ " - " + quests[choice-1][1]+"\n") #prints quest information
                print("-"*50+"\n") #prints dashes
            else:
                print("Invalid choice")
        

        
    
    elif choice == 'inventory' or choice == 'Inventory': #if choice is inventory
        print("\n")
        for count in range(len(inventory)):  #prints inventory
            print(inventory[count-1][0][0] + "     " + "x "+ str(inventory[count-1][1]))
        print("\n")

    else:
        print("Invalid choice")

