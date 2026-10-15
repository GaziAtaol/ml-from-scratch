# Algorithms from Scratch

Classic machine learning and algorithm design problems implemented in pure Python, without scikit-learn or other third party libraries. Each folder is a self-contained project with its own README, code and data.

## Projects

| Folder | Algorithm | Data | Result |
|---|---|---|---|
| [01-knn](01-knn) | k-nearest neighbors with distance based tie breaking, terminal interface and Tkinter GUI | Iris (120 training and 30 test samples) and a noisy 2D dataset with 3 classes (90 training and 30 test samples) | Iris: 29 of 30 correct (96.67%) for every k from 1 to 10. Noisy data: 76.7% at k = 3 |
| [02-perceptron](02-perceptron) | Single-layer perceptron with the delta rule | Iris, setosa versus the other species (120 training and 30 test samples) | Converged in 2 to 12 iterations over 30 runs, 100% test accuracy in every run |
| [03-language-detector](03-language-detector) | One perceptron per language, step and linear variants | Self-collected texts in Polish, Turkish and German (60 training and 30 test files) | Step variant: 25 to 30 of 30 correct over 15 runs. Linear variant: 30 of 30 in 3 runs |
| [04-naive-bayes](04-naive-bayes) | Gaussian Naive Bayes | Iris (120 training and 30 test samples) | 28 of 30 correct (93.33%) |
| [05-k-means](05-k-means) | k-means clustering with entropy of each cluster | Iris, 150 samples, species ignored while clustering | k = 3: sum of squared distances 78.94, setosa found exactly |
| [06-knapsack](06-knapsack) | Knapsack: brute force and greedy | 15 datasets of 30 items, capacity 50 | Brute force optimal on all 15, greedy optimal on 7 |
| [07-huffman-coding](07-huffman-coding) | Huffman coding | Any text | 135 bits against 144 bits fixed-length for a 36 character example |


## Running a project

Each project runs from its own folder:

```bash
cd 02-perceptron
python main.py
```

All projects use only the Python standard library, except that `01-knn` needs `matplotlib` for the accuracy chart and uses `tkinter` for the optional GUI.

## Notes

* The accuracy figures come from the data included in each folder. The test sets are small (30 samples), so one sample changes the accuracy by 3.3 percentage points.
* The perceptron projects and k-means start from random values, so single runs differ. The README of each project says how many runs a figure is based on.
