gold_coin = int(input("Please Enter the gold coin: any positive integer: "))
gold_coin_2 = int(input("Please Enter the gold coin 2: any positive integer: "))


total = gold_coin + gold_coin_2
print("The gold coin is: ", total)


print("The gold coin double is: ", total * 2)

if gold_coin > gold_coin_2:
    print("Gold coin 1 is greater than gold coin 2")