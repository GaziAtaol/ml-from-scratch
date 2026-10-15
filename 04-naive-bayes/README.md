# Gaussian Naive Bayes Classifier

A Gaussian Naive Bayes classifier written from scratch in pure Python, with no machine learning libraries. It classifies Iris flowers into three species from four measurements.

## How it works

1. **Training.** The samples are grouped by class. For each class and each of the 4 attributes the program computes the mean and the standard deviation. The prior of a class is its share of the training samples.
2. **Smoothing check.** If an attribute has a standard deviation of zero, a small value (`1e-6`) is added so that the density does not divide by zero. The check prints what it changed.
3. **Prediction.** For a new sample, the score of each class is the prior times the product of the Gaussian densities of the 4 attributes. The class with the highest score is the prediction.
4. **Evaluation.** The program prints the number of correct predictions, the accuracy and a confusion matrix.
5. **Manual input.** After the evaluation you can type 4 numbers (separated by spaces or commas) and get the predicted class and its score. Type `q` to quit.

The standard deviation is the population standard deviation (division by `n`).

## Data

Iris measurements in centimeters: sepal length, sepal width, petal length, petal width, then the species. Values are tab separated and use a decimal comma.

```
training-data/iris_training.txt   120 samples, 40 per species
test-data/iris_test.txt            30 samples, 10 per species
```

## Run

```bash
python main.py
```

## Project structure

```
main.py          training, evaluation and manual input loop
algorithm.py     class statistics, priors, Gaussian density, prediction, confusion matrix
data_loader.py   reads the tab separated files and normalizes the labels
```

## Results

On the 30 test samples: 28 correct (93.33%).

| True class | setosa | versicolor | virginica |
|---|---|---|---|
| setosa | 10 | 0 | 0 |
| versicolor | 0 | 9 | 1 |
| virginica | 0 | 1 | 9 |

Setosa is separated perfectly. The two errors are one versicolor sample (`6.9, 3.1, 4.9, 1.5`) predicted as virginica and one virginica sample (`4.9, 2.5, 4.5, 1.7`) predicted as versicolor. These two species overlap in the data.

The training means and standard deviations are printed at the start of every run.

## Notes

* The method is deterministic, so every run gives the same result.
* The test set has 30 samples, so one sample changes the accuracy by 3.3 percentage points.
* The smoothing step is a demonstration. When no standard deviation is zero, the program still adds `1e-6` to attribute 1 of each class and prints the change. The effect on the result is negligible.
* The model assumes that the attributes are independent and Gaussian within each class. Petal length and petal width are correlated in Iris, so the assumption is only approximate.
