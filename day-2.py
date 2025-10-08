def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Enter an integer.")

def main():
    gold_coin = get_positive_int("Please Enter the gold coin (positive integer): ")
    gold_coin_2 = get_positive_int("Please Enter the gold coin 2 (positive integer): ")

    total = gold_coin + gold_coin_2
    print(f"The gold coin is: {total}")
    print(f"The gold coin double is: {total * 2}")
    print(f"Product: {gold_coin * gold_coin_2}")
    print(f"Difference: {abs(gold_coin - gold_coin_2)}")
    print(f"Average: {total / 2:.2f}")
    print(f"Max: {max(gold_coin, gold_coin_2)}; Min: {min(gold_coin, gold_coin_2)}")

    if gold_coin > gold_coin_2:
        print("Gold coin 1 is greater than gold coin 2")
    elif gold_coin < gold_coin_2:
        print("Gold coin 2 is greater than gold coin 1")
    else:
        print("Gold coin 1 is equal to gold coin 2")

if __name__ == "__main__":
    main()

