# Language Detector with Perceptrons

A language detector written from scratch in pure Python, with no machine learning libraries. It classifies a text as Polish, Turkish or German from the frequencies of the letters A to Z, using one perceptron per language. Two variants of the perceptron are implemented and can be compared.

## How it works

### Features

Each text becomes a vector of 26 numbers, the relative frequency of each letter A to Z. Only the 26 basic Latin letters are counted, so characters such as `ą`, `ł`, `ş`, `ü` or `ß` are ignored.

### One perceptron per language

Every language has its own perceptron. A perceptron is trained to output a high value for texts in its language and a low value for all other texts (one versus the rest).

| | Variant 1 (binary) | Variant 2 (linear) |
|---|---|---|
| Activation | Step function with a threshold | Identity, `y = net` |
| Targets | 1 for the language, 0 for the others | +1 for the language, -1 for the others |
| Inputs | Raw letter frequencies | Frequency vectors normalized to unit length |
| Weights | Random in [-0.5, 0.5] plus a threshold | Random, normalized to unit length after each pass |
| Training stops | When a full pass makes no errors | When the largest error `|d - y|` is below 0.01 |
| Prediction | Among perceptrons that output 1, the largest `net`. If none outputs 1, the largest `net` overall | The largest `net` |

Both variants use the delta rule, `w = w + learning_rate * (target - output) * x`, with a learning rate of 0.01 and at most 500 passes over the training data.

### Evaluation

The program prints the prediction for every test file, a confusion matrix, and precision, recall and F1 for each language with their macro average. After testing, you can paste any text and see the detected language and the `net` value of every perceptron.

## Data

The texts were collected by the author. Each language has its own folder of `.txt` files, and the folder name is the language label.

```
Training data/
  German/    20 files
  Polish/    20 files
  Turkish/   20 files
test data/
  German/    10 files
  Polish/    10 files
  Turkish/   10 files
```

That is 60 training files and 30 test files. The folder names in `Training data` and `test data` must match.

## Run

```bash
python main.py
```

The program asks for the variant (1 or 2), then offers to train, test and classify text. The learning rate is set at the top of `main.py`. Training limits are at the top of `trainer.py`.

## Project structure

```
main.py          interactive program
data_loader.py   letter frequency vectors and dataset loading
perceptron.py    Perceptron (variant 1) and PerceptronV2 (variant 2)
trainer.py       training loops for both variants
evaluator.py     prediction, confusion matrix, precision, recall and F1
```

## Results

Results of one run on the 30 test files. The weights start at random values, so the numbers change from run to run.

| Variant | Training | Test accuracy | Macro F1 |
|---|---|---|---|
| 1 (binary) | Converged after 185 iterations | 29 of 30 (96.67%) | 0.9666 |
| 2 (linear) | Stopped at the limit of 500 iterations | 30 of 30 (100%) | 1.0000 |

Confusion matrix of variant 1 (rows are the true language):

| | Polish | Turkish | German |
|---|---|---|---|
| Polish | 10 | 0 | 0 |
| Turkish | 0 | 10 | 0 |
| German | 1 | 0 | 9 |

One German text was classified as Polish.

## Notes

* **Variant 2 never reaches its stopping condition.** Both the inputs and the weights have unit length, so `|net|` can never exceed 1. Reaching `net` close to +1 for one language and close to -1 for all others, on every training text, is not possible with this data. The largest error stays at about 1.077 after the first 100 iterations. The classification still works, because the prediction only compares `net` values and does not need them to reach the targets.
* **The two variants are not ranked by these results.** The difference between 29 and 30 correct texts is a single file out of 30.
* The test set is small, so each text changes the accuracy by 3.3 percentage points.
* Letter frequencies cannot separate closely related languages well, and the diacritics that distinguish many languages are not used.
