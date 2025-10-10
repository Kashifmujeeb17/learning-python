import argparse
import json
import sys
from typing import Dict

def get_positive_int(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Enter an integer.")

def compute_stats(g1: int, g2: int) -> dict:
    total = g1 + g2
    return {
        "gold1": g1,
        "gold2": g2,
        "total": total,
        "double": total * 2,
        "product": g1 * g2,
        "difference": abs(g1 - g2),
        "average": total / 2,
        "max": max(g1, g2),
        "min": min(g1, g2),
        "comparison": (
            "Gold coin 1 is greater than gold coin 2"
            if g1 > g2 else
            "Gold coin 2 is greater than gold coin 1"
            if g1 < g2 else
            "Gold coin 1 is equal to gold coin 2"
        ),
    }

def print_stats(stats: dict) -> None:
    print(f"The gold coin is: {stats['total']}")
    print(f"The gold coin double is: {stats['double']}")
    print(f"Product: {stats['product']}")
    print(f"Difference: {stats['difference']}")
    print(f"Average: {stats['average']:.2f}")
    print(f"Max: {stats['max']}; Min: {stats['min']}")
    print(stats["comparison"])

def save_results(stats: dict, path: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=2)
    print(f"Results saved to: {path}")

def main():
    parser = argparse.ArgumentParser(description="Calculate stats for two gold coins.")
    parser.add_argument("gold", nargs="?", type=int, help="first gold coin (positive integer)")
    parser.add_argument("gold2", nargs="?", type=int, help="second gold coin (positive integer)")
    parser.add_argument("--save", "-s", help="path to save results as JSON")
    args = parser.parse_args()

    if args.gold is not None and args.gold2 is not None:
        if args.gold <= 0 or args.gold2 <= 0:
            print("Command-line values must be positive integers. Falling back to interactive input.")
            gold_coin = get_positive_int("Please Enter the gold coin (positive integer): ")
            gold_coin_2 = get_positive_int("Please Enter the gold coin 2 (positive integer): ")
        else:
            gold_coin = args.gold
            gold_coin_2 = args.gold2
    else:
        gold_coin = get_positive_int("Please Enter the gold coin (positive integer): ")
        gold_coin_2 = get_positive_int("Please Enter the gold coin 2 (positive integer): ")

    stats = compute_stats(gold_coin, gold_coin_2)
    print_stats(stats)

    if args.save:
        save_results(stats, args.save)

if __name__ == "__main__":
    main()

