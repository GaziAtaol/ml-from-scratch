from data_loader import load_data, get_num_attributes
from perceptron import Perceptron
from trainer import train
from evaluator import evaluate

# ── CONFIG ────────────────────────────────────────────────
TRAINING_FILE  = "iris_training.txt"
TEST_FILE      = "iris_test.txt"
LEARNING_RATE  = 0.1
DECIMAL_SEP    = ","
# ──────────────────────────────────────────────────────────


def ask_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("yes", "y"):
            return True
        elif answer in ("no", "n"):
            return False
        else:
            print("  Please answer yes or no.")

def get_new_sample(num_attributes):
    attributes = []
    print()
    for i in range(1, num_attributes + 1):
        while True:
            try:
                raw   = input(f"Enter value for attribute {i}: ")
                value = float(raw.replace(DECIMAL_SEP, "."))
                attributes.append(value)
                break
            except ValueError:
                print(f"Invalid input. Please enter a number (e.g. 5{DECIMAL_SEP}1).")

    return {"attributes": attributes, "label": None}

def main():
    print("=" * 55)
    print("MPP2 Perceptron Classifier (Iris-setosa)")
    print("=" * 55)

    training_samples = load_data(TRAINING_FILE,binary=True)
    test_samples = load_data(TEST_FILE,binary=True)
    num_attributes = get_num_attributes(training_samples)

    print(f"\n Training file : {TRAINING_FILE}")
    print(f" Test file : {TEST_FILE}")
    print(f" Training samples : {len(training_samples)}")
    print(f" Test samples : {len(test_samples)}")
    print(f" Attributes : {num_attributes}")
    print(f" Learning rate : {LEARNING_RATE}")

    print("\n--- Training (Delta Algorithm) ---")
    perceptron = Perceptron(num_inputs=num_attributes, learning_rate=LEARNING_RATE)
    train(perceptron, training_samples)

    print("\n--- Test Set Evaluation ---")
    evaluate(perceptron, test_samples)

    print("\n--- Classify New Samples ---")
    while True:
        sample = get_new_sample(num_attributes)
        net_val = perceptron.net(sample["attributes"])
        prediction = perceptron.step(sample["attributes"])
        label = "Iris-setosa" if prediction == 1 else "Non-setosa"

        print()
        print(f"Net value : {net_val:.4f}")
        print(f"Output : {prediction}  →  {label}")

        print()
        if not ask_yes_no("Classify another sample? (yes/no): "):
            break

    print("\nGoodbye!")
    print("=" * 55)

if __name__ == "__main__":
    main()
