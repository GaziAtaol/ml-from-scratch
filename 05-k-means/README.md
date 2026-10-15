# k-means Clustering on the Iris Data

k-means clustering written from scratch in pure Python, with no third party libraries. The decision attribute (species) is ignored while clustering and is used only afterwards, to measure how pure each cluster is with the entropy of its species distribution.

## How it works

1. Pick k distinct samples at random as the initial centers.
2. Assign every sample to its nearest center (squared Euclidean distance) and compute the sum of squared distances from all samples to their centers.
3. Move each center to the mean of its cluster. An empty cluster keeps its old center.
4. Repeat until no sample changes its cluster.

The program prints the sum of squared distances at every iteration. At the end it prints each cluster with its center, size, entropy and members.

The entropy of a cluster is `-sum(p * log2(p))` over the species in it, in bits. 0 means the cluster holds one species only, 1.585 would be an even mix of all three.

## Data

`data/iris.txt` has 150 samples, 50 per species, with four measurements in centimeters (sepal length, sepal width, petal length, petal width), tab separated, with a decimal comma.

## Run

```bash
python main.py
```

The program asks for k (3 or more). The random start is fixed by `SEED` at the top of `main.py`. Set it to `None` for a different start on every run.

## Project structure

```
main.py          input, output and the entropy report
kmeans.py        assignment, center update, main loop and entropy
data_loader.py   reads the Iris file
data/iris.txt    150 Iris samples
```

## Results

With `SEED = 0`:

| k | Iterations | Final sum of squared distances | Weighted average entropy |
|---|---|---|---|
| 3 | 5 | 78.94 | 0.3939 bits |
| 4 | 8 | 57.47 | 0.3529 bits |
| 5 | 6 | 49.92 | 0.1115 bits |

For k = 3 the sum of squared distances falls like this: 189.72, 92.53, 79.54, 79.00, 78.94. The clusters are:

| Cluster | Size | Species inside | Entropy |
|---|---|---|---|
| 1 | 38 | 36 virginica, 2 versicolor | 0.2975 bits |
| 2 | 62 | 48 versicolor, 14 virginica | 0.7706 bits |
| 3 | 50 | 50 setosa | 0.0000 bits |

Setosa is found exactly. Versicolor and virginica overlap in the measurements, so no choice of centers separates them perfectly.

## Notes

* The result depends on the random start. In 200 runs with seeds 0 to 199 and k = 3, 156 runs ended with a sum of squared distances of about 78.9 and 44 runs got stuck in worse solutions, between 142.9 and 145.3. The default seed gives the better solution.
* Entropy measures purity against the species labels. It is not used to choose k. More clusters lower the entropy almost automatically.
* The distance is not scaled, which is fine here because all four measurements are in centimeters.
