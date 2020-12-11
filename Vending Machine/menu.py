def menu():
    print "\t1. Dr. Pepper-1.75"
    print "\t2. Doritos-2.00"
    print "\t3. Kitkat Bar-.50"
    print "\t4. Pop-tarts-1.00"
    print "\t5. Gum-.25"
    print "Please enter the number of your item or 0 to quit:"


def getChange(change, money):

    return int(change / money)



loop = 1
choice = 0
total = 0
payment = 0
dollar = 0
quarter = 0
dime = 0
nickle = 0
pennies = 0

while (loop == 1):
    menu()
    choice = int(raw_input())

    if choice == 0:
        if total == 0:
            print "Thank you! Standby for your total.\nYou didn't order anything!"
        else:
            print "Thank you! Standby for your total.\n"
            print "Your total is " + str(total) + "!"
        
            payment = float(raw_input("Enter your payment: "))
            while(payment < total):
                print "Not enough! Enter more money:"
                payment = float(raw_input())
            
            change = payment - total
            print "Your change is: "
            dollar = getChange(change, 1.00)
            print "Dollars: " + str(dollar)
            change -= float(dollar)

            quarter = getChange(change, 0.25)
            print "Quarters : " + str(quarter)
            change -= 0.25*quarter

            dime = getChange(change, 0.1)
            print "Dimes: " + str(dime)
            change -= 0.1*dime

            nickle = getChange(change, 0.05)
            print "Nickles: " + str(nickle)
            change -= 0.05*nickle
            
            pennies = getChange(change, 0.01)
            print "Pennies: " + str(pennies)
            loop = 0
        
    
    elif choice == 1:
        print "You bought one can of Dr. Pepper for 1.75"
        total += 1.75
    
    elif choice == 2:
        print "You bought one bag of Doritos for 2.00"
        total += 2.00
    
    elif choice == 3:
        print "You bought one bag of Kitkat Bar for 0.50"
        total += 0.5
    
    elif choice == 4:
        print "You bought one bag of Pop-tarts for 1.00"
        total += 1.00
    
    elif choice == 5:
        print "You bought one bag of Gum for 0.50"
        total += 0.25
    
    else:
        print "Invalid entry!"
        # loop = 0
    
