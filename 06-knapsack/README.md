# Knapsack Problem: Brute Force and Greedy

Two solutions of the 0/1 knapsack problem in pure Python: an exhaustive search over all subsets that fit, and a greedy algorithm that takes items by value per unit of size. The program runs both on one dataset and prints the chosen items, the total value, the capacity used, the execution time and the number of subsets investigated.

## Data

`data/knapsack.txt` holds 15 datasets. Each has 30 items with a size and a value, and the capacity of the knapsack is 50 in every dataset. The program asks for a dataset number from 1 to 15, and a random one is used if you press Enter.

## How it works

**Brute force.** Subsets are built by adding items in order of increasing size. When the next item does not fit, no larger item fits either, so the search backtracks. Every subset that fits is visited exactly once and the best one is kept. Subsets that are too large are never built, so the count of investigated subsets is the number of subsets that fit, not all `2^30` (1,073,741,824). The result is always optimal.

**Greedy.** Items are sorted by value divided by size, best first. The algorithm walks through the list once and takes every item that still fits. It finishes in microseconds but can miss the optimum.

## Run

```bash
python main.py
```

Output example (dataset 15):

```
=== Brute force ===
Items [nr, size, value]: [[2, 7, 13], [4, 2, 15], [6, 3, 3], [13, 8, 19], [14, 2, 16], [18, 7, 17], [20, 9, 17], [21, 1, 17], [23, 6, 15], [27, 5, 18]]
Total value: 150
Capacity used: 50 / 50
Execution time: 1.349333 s
Subsets investigated: 5832835
```

`nr` is the position of the item in its dataset, counting from 1.

## Project structure

```
main.py          dataset choice and output
algorithms.py    brute_force and greedy
data_loader.py   reads knapsack.txt
data/            knapsack.txt
```

## Results on all 15 datasets

The optimum was checked with an independent dynamic programming solution, and brute force matched it on every dataset. Times are from one run on a cloud machine and depend on the computer.

| Dataset | Subsets that fit | Brute force time | Best value | Greedy value |
|---|---|---|---|---|
| 1 | 155,788,840 | 34.9 s | 203 | 203 |
| 2 | 9,572,806 | 2.1 s | 179 | 177 |
| 3 | 38,290,862 | 8.5 s | 203 | 199 |
| 4 | 12,380,462 | 2.8 s | 160 | 157 |
| 5 | 35,082,935 | 8.0 s | 179 | 174 |
| 6 | 27,268,822 | 6.0 s | 157 | 157 |
| 7 | 22,720,082 | 5.2 s | 156 | 156 |
| 8 | 72,315,076 | 16.4 s | 220 | 220 |
| 9 | 28,352,595 | 6.1 s | 178 | 175 |
| 10 | 30,041,793 | 6.9 s | 167 | 166 |
| 11 | 12,846,367 | 2.9 s | 131 | 130 |
| 12 | 30,320,776 | 6.8 s | 169 | 169 |
| 13 | 29,475,800 | 6.6 s | 184 | 184 |
| 14 | 120,286,081 | 26.9 s | 230 | 227 |
| 15 | 5,832,835 | 1.3 s | 150 | 150 |

Greedy found the optimum on 7 of the 15 datasets. On the other 8 it was lower by 1 to 5 points, at most 2.8 percent of the optimum. Greedy needs about 20 microseconds, brute force needs seconds and its running time grows with the number of subsets that fit.

## Notes

* Several subsets can share the best value. Brute force reports the first one it finds, so a different item order can give a different knapsack with the same value.
* The greedy count is the 30 items it examines while growing one subset, which is not comparable to the brute force count.
* Brute force does not scale. Adding more items multiplies the number of subsets, so 40 or 50 items would take far too long. Dynamic programming solves this problem exactly in a fraction of a second.
