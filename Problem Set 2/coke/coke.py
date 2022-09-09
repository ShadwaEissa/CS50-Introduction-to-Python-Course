amount_due = 50

while amount_due > 0:
    print("Amount Due: ",amount_due)
    coin_inserted = int(input("Insert coin: "))
    if coin_inserted in [25, 10, 5]:
        amount_due = amount_due - coin_inserted

change_owed = abs(amount_due)
print("Change_owed: ",change_owed)

    

