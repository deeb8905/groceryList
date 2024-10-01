#i could not figure out how to sort this but i got pretty much everything else working :)

startVar = 0 #varible to handle starting and stoping the loop
groceryList = [] #creating the empty list for the grocery list
itemCostList = [] #creates an empty list for specifically item cost
itemNameList = [] #creates an empty list for specifically item names
itemFCostList = [] #creates an empty list for specifically item final costs
while startVar == 0: #grocery list loop
    questionMain = (input("What do you want to do? \n 1. Add a new item \n 2. Remove an item \n 3. Read out list \n 4. Close program \n"))

    if questionMain == "1": #if statement that handles adding new items to the list
        whatItem = (input("What item are you adding to the list?"))
        howMuch = int(input("How much does it cost?"))
        howMany = float(input("How many?"))
        finalCost = float(howMany * howMuch * 1.6) #calculates the final cost + tax and turns it into a variable 
        print(f"Added {howMuch} {whatItem}s for ${finalCost} \n")
        itemCostList.append(howMuch)
        itemNameList.append(whatItem)
        itemFCostList.append(finalCost)
        print("================================")
        for x in range(len(itemCostList)): #for loop to list out the list
            print(f"{itemCostList[x]} {itemNameList[x]}s for {itemFCostList[x]} ")
        print("================================")

    elif questionMain == "2": #if statement to handle removing things from the list
        removeItemPrompt = (input("What item are you removing?"))
        z = itemNameList.index(removeItemPrompt)
        itemNameList.remove(itemNameList[z])
        itemFCostList.remove(itemFCostList[z])
        itemCostList.remove(itemCostList[z])

    elif questionMain == "3": #if statement to handle re-printing the entire list
        print("================================")
        for x in range(len(itemNameList)): #for loop to list out the list
            print(f"{itemCostList[x]} {itemNameList[x]}s for {itemFCostList[x]} ")
        print("================================")

    elif questionMain == "4": #if statement to handle closing the program when the user is finished
        print("goodbye")
        exit()