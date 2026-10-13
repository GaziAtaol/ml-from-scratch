# Perceptron Classifier with Iris setosa

A simple single-layer **Perceptron** implemented from scratch in Python that performs binary classification on the classic **Iris dataset**, distinguishing *Iris-setosa* from all other species.

---

## How It Works

The perceptron learns a linear decision boundary using the **Delta (Widrow-Hoff) learning rule**:

- Weights and a threshold are initialised with random values in `[-0.5, 0.5]`.
- During each training iteration every sample is presented and the weights are updated whenever the prediction is wrong:

  ```
  wᵢ ← wᵢ + η · (target − output) · xᵢ
  θ  ← θ  − η · (target − output)
  ```

- Training stops when all samples are classified correctly, or after a maximum of **500 iterations**.

---

## Project Structure

```
.
├── main.py              # Entry point – wires everything together and runs the interactive CLI
├── perceptron.py        # Perceptron class (net, step, update)
├── trainer.py           # Training loop (Delta algorithm)
├── evaluator.py         # Evaluates accuracy on a test set
├── data_loader.py       # Reads tab-separated data files
├── iris_training.txt    # Training set  (119 samples)
├── iris_test.txt        # Test set      (30 samples)
├── iris_training_hard.txt  # Harder training split (50 samples)
└── iris_test_hard.txt      # Harder test split     (15 samples)
```

---

## Data Format

Each line in a data file is tab separated and contains four numeric attributes followed by the class label:

```
5,4    3,7    1,5    0,2    Iris-setosa
6,3    3,3    4,7    1,6    Iris-versicolor
```

> **Note:** decimal values use a **comma** as the separator (European locale).

The four attributes correspond to the standard Iris measurements:

| # | Attribute        |
|---|-----------------|
| 1 | Sepal length (cm) |
| 2 | Sepal width  (cm) |
| 3 | Petal length (cm) |
| 4 | Petal width  (cm) |

Labels are mapped to binary targets automatically:

| Label           | Target |
|-----------------|--------|
| `Iris-setosa`   | `1`    |
| anything else   | `0`    |

---

## Getting Started

### Requirements

- Python 3.8+
- No external libraries required (standard library only)

### Run

```bash
python main.py
```

The program will:

1. Load and display dataset statistics.
2. Train the perceptron, printing the error count per iteration.
3. Evaluate accuracy on the test set.
4. Enter an interactive loop where you can classify new samples by typing the four attribute values.

### Example session

```
=======================================================
MPP2 Perceptron Classifier (Iris setosa)
=======================================================

 Training file : iris_training.txt
 Test file     : iris_test.txt
 Training samples : 119
 Test samples     : 30
 Attributes       : 4
 Learning rate    : 0.1

--- Training (Delta Algorithm) ---

Iteration    Errors
  ------------------------
1            12
2            4
3            0

Training completed converged after 3 iteration(s).

--- Test Set Evaluation ---

#     True label   Predicted    Result
  --------------------------------------------
1     setosa       setosa       correct
...
Accuracy : 100.00%

--- Classify New Samples ---

Enter value for attribute 1: 5,1
Enter value for attribute 2: 3,5
Enter value for attribute 3: 1,4
Enter value for attribute 4: 0,2

Net value : 0.8312
Output    : 1  →  Iris-setosa

Classify another sample? (yes/no): no

Goodbye!
=======================================================
```

---

## Configuration

All tuneable constants are at the top of `main.py`:

| Constant        | Default                | Description                       |
|-----------------|------------------------|-----------------------------------|
| `TRAINING_FILE` | `iris_training.txt`    | Path to the training data file    |
| `TEST_FILE`     | `iris_test.txt`        | Path to the test data file        |
| `LEARNING_RATE` | `0.1`                  | Perceptron learning rate (η)      |
| `DECIMAL_SEP`   | `,`                    | Decimal separator for user input  |

`MAX_ITERATIONS` (default `500`) is defined in `trainer.py`.

---

## Module Overview

| Module          | Responsibility |
|-----------------|----------------|
| `perceptron.py` | `Perceptron` class computes net input (`net`), binary output (`step`), and performs a single weight update (`update`) |
| `trainer.py`    | Runs the full training loop over the dataset until convergence or max iterations |
| `evaluator.py`  | Iterates over the test set, prints per sample results, and reports overall accuracy |
| `data_loader.py`| Parses tab separated files, normalises labels, and converts them to binary targets |
| `main.py`       | Orchestrates loading, training, evaluation, and the interactive classification loop |

---

## License

This project is released for educational purposes.
