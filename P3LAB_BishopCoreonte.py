#Coreonte Bishop
#3/22/2026
#P3LAB
#This program asks the user for an amount of money and displays the most efficient number of dollars, quarters, dimes, nickels, and pennies needed. 

#User enters money
money=float(input("Enter the amount of money as a float: $"))

#Convert money to cents
cents=int(round(money*100))

#If money is zero
if cents==0:
    print("No Change")
else:
    #Calculate dollars
    dollars=cents//100
    cents=cents-(dollars*100)

    #Calculate quarters
    quarters=cents//25
    cents=cents-(quarters*25)

    #Calculate dimes
    dimes=cents//10
    cents=cents-(dimes*10)

    #Calculate nickels
    nickels=cents//5
    cents=cents-(nickels*5)

    #Pennies
    pennies=cents

    #Display dollars
    if dollars>0:
        if dollars==1:
            print("1 Dollar")
        else:
            print(dollars,"Dollars")

    #Display quarters
    if quarters>0:
        if quarters==1:
            print("1 Quarter")
        else:
            print(quarters,"Quarters")

    #Display dimes
    if dimes>0:
        if dimes==1:
            print("1 Dime")
        else:
            print(dimes,"Dimes")

    #Display nickels
    if nickels>0:
        if nickels==1:
            print("1 Nickel")
        else:
            print(nickels,"Nickels")

    #Display pennies
    if pennies>0:
        if pennies==1:
            print("1 Penny")
        else:
            print(pennies,"Pennies")

            

    
