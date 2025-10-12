import argparse
import json
import sys
from typing import Dict, Any, Tuple, Optional


def get_positive_int(prompt: str) -> int:
    """Prompt until the user enters a positive integer or cancels."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Enter an integer.")
        except (KeyboardInterrupt, EOFError):
            print("\nInput cancelled.")
            sys.exit(1)


def read_two_ints_from_stdin() -> Optional[Tuple[int, int]]:
    """Attempt to read two ints from piped stdin. Return None if not available or invalid."""
    if sys.stdin is None or sys.stdin.isatty():
        return None
    data = sys.stdin.read().strip().split()
    if len(data) < 2:
        return None
    try:
        a, b = int(data[0]), int(data[1])
        if a > 0 and b > 0:
            return a, b
    except ValueError:
        pass
    return None


def compute_stats(g1: int, g2: int) -> Dict[str, Any]:
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


def print_stats(stats: Dict[str, Any]) -> None:
    print(f"The gold coin is: {stats['total']}")
    print(f"The gold coin double is: {stats['double']}")
    print(f"Product: {stats['product']}")
    print(f"Difference: {stats['difference']}")
    print(f"Average: {stats['average']:.2f}")
    print(f"Max: {stats['max']}; Min: {stats['min']}")
    print(stats["comparison"])


def save_results(stats: Dict[str, Any], path: str) -> None:
    try:
        if path == "-":
            # write JSON to stdout
            json.dump(stats, sys.stdout, indent=2)
            sys.stdout.write("\n")
            print("Results printed to stdout.")
            return
        with open(path, "w", encoding="utf-8") as f:
            json.dump(stats, f, indent=2)
        print(f"Results saved to: {path}")
    except OSError as exc:
        print(f"Failed to save results to {path}: {exc}", file=sys.stderr)
        sys.exit(1)


def main() -> None:
    parser = argparse.ArgumentParser(description="Calculate stats for two gold coins.")
    parser.add_argument("gold", nargs="?", type=int, help="first gold coin (positive integer)")
    parser.add_argument("gold2", nargs="?", type=int, help="second gold coin (positive integer)")
    parser.add_argument("--save", "-s", help="path to save results as JSON (use '-' for stdout)")
    parser.add_argument("--json", "-j", action="store_true", help="also print results as JSON to stdout")
    args = parser.parse_args()

    # 1) Try command-line args
    gold_coin: Optional[int] = None
    gold_coin_2: Optional[int] = None
    if args.gold is not None and args.gold2 is not None:
        if args.gold > 0 and args.gold2 > 0:
            gold_coin, gold_coin_2 = args.gold, args.gold2
        else:
            print("Command-line values must be positive integers. Falling back to other input methods.", file=sys.stderr)

    # 2) Try piped stdin
    if gold_coin is None:
        stdin_vals = read_two_ints_from_stdin()
        if stdin_vals:
            gold_coin, gold_coin_2 = stdin_vals

    # 3) Interactive fallback
    if gold_coin is None:
        gold_coin = get_positive_int("Please Enter the gold coin (positive integer): ")
        gold_coin_2 = get_positive_int("Please Enter the gold coin 2 (positive integer): ")

    stats = compute_stats(gold_coin, gold_coin_2)
    print_stats(stats)

    if args.json:
        json.dump(stats, sys.stdout, indent=2)
        sys.stdout.write("\n")

    if args.save:
        save_results(stats, args.save)


if __name__ == "__main__":
    main()

