balance = 0.0
soda = 3
chips = 1
candy = 5
while balance >= 0:
    print(f"Current balance: {balance}")
    option = input("Choose an option (insert, buy, exit): ")
    if option == "insert":
        amount = float(input("Insert an amount($1.00, $2.00, $5.00):"))
        if amount == 1 or amount == 2 or amount == 5:
            balance += amount
        else:
            print("Invalid bills")
    elif option == "buy":
        choice = input("Pick the item (chips($2.00), candy($1.25), soda($1.50)):")
        if choice == "chips":
            if chips > 0:
                if balance >= 2:
                    balance -= 2
                    chips -= 1
                    print("Chips dispense")
                else:
                     print("Insufficient funds!")
            else:
                print("Sorry, chips are out of stock!")
        elif choice == "candy":
            if candy > 0:
                if balance >= 1.25:
                    balance -= 1.25
                    candy -= 1
                    print("Candy dispense")
                else:
                    print("Insufficient funds!")
            else:
                print("Sorry, candy is out of stock!")
        elif choice == "soda":
            if soda > 0:
                if balance >= 1.5:
                    balance -= 1.5
                    soda -= 1
                    print("Soda dispense")
                else:
                    print("Insufficient funds!")
            else:
                print("Sorry, soda is out of stock!")
    elif option == "exit":
        remaining_balance = balance
        print(f"The remaining balance is ${remaining_balance}")
        print("Goodbye! See you later!")
        break
    else:
        print("Invalid choice")


