# Machine Learning Algorithms from Scratch

Classic machine learning algorithms implemented in pure Python, without scikit-learn or other machine learning libraries. Each folder is a self-contained project with its own README, code and data.

## Projects

| Folder | Algorithm | Data | Result |
|---|---|---|---|
| [01-knn](01-knn) | k-nearest neighbors with distance based tie breaking, terminal interface and Tkinter GUI | Iris (120 training and 30 test samples) and a noisy 2D dataset with 3 classes (90 training and 30 test samples) | Iris: 29 of 30 correct (96.67%) for every k from 1 to 10. Noisy data: 76.7% at k = 3 |
| [02-perceptron](02-perceptron) | Single-layer perceptron with the delta rule | Iris, setosa versus the other species (120 training and 30 test samples) | Converged in 2 to 12 iterations over 30 runs, 100% test accuracy in every run |
| [03-language-detector](03-language-detector) | One perceptron per language, step and linear variants | Self-collected texts in Polish, Turkish and German (60 training and 30 test files) | 29 of 30 (step variant) and 30 of 30 (linear variant) correct in one run |

More algorithms are added as they are finished.

## Running a project

Each project runs from its own folder:

```bash
cd 02-perceptron
python main.py
```

Most projects use only the Python standard library. `01-knn` needs `matplotlib` for the accuracy chart and uses `tkinter` for the optional GUI.

## Notes

* The accuracy figures come from the data included in each folder. The test sets are small (30 samples), so one sample changes the accuracy by 3.3 percentage points.
* The perceptron projects start from random weights, so single runs differ. The README of each project says how many runs a figure is based on.
