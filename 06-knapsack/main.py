import random

from data_loader import load_datasets
from algorithms import brute_force, greedy

DATA_FILE = "data/knapsack.txt"


def choose_dataset(count):
    text = input(f"Dataset number 1-{count} (press Enter for a random one): ").strip()
    if text == "":
        number = random.randint(1, count)
        print(f"Random choice: dataset {number}")
        return number
    try:
        number = int(text)
    except ValueError:
        number = 0
    if not 1 <= number <= count:
        print(f"Invalid choice, using a random dataset instead.")
        number = random.randint(1, count)
        print(f"Random choice: dataset {number}")
    return number


def show(title, result, capacity, checked_label):
    items, total, used, seconds, checked = result
    triples = [[nr, size, value] for nr, size, value in items]
    print(f"\n=== {title} ===")
    print(f"Items [nr, size, value]: {triples}")
    print(f"Total value: {total}")
    print(f"Capacity used: {used} / {capacity}")
    print(f"Execution time: {seconds:.6f} s")
    print(f"{checked_label}: {checked}")


def main():
    capacity, datasets = load_datasets(DATA_FILE)
    number = choose_dataset(len(datasets))
    items = datasets[number - 1]
    print(f"{len(items)} items, capacity {capacity}")

    print("Running brute force, the largest datasets take about half a minute...")
    show("Brute force", brute_force(items, capacity), capacity, "Subsets investigated")
    show("Greedy", greedy(items, capacity), capacity, "Items examined (one growing subset)")

if __name__ == "__main__":
    main()
