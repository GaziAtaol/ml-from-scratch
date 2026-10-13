from data_loader import load_dataset, normalize_vector, text_to_vector
from perceptron import Perceptron, PerceptronV2
from trainer import train_v1, train_v2
from evaluator import evaluate, predict_v1, predict_v2

TRAINING_FOLDER = "Training data"
TEST_FOLDER     = "test data"
LEARNING_RATE   = 0.01

def ask_variant():
    while True:
        print("\nSelect variant:")
        print("  1 - Binary (step activation, target 0/1)")
        print("  2 - Linear (y=net, normalized weights, target -1/+1)")
        choice = input("Choice: ").strip()
        if choice in ("1", "2"):
            return int(choice)
        print("Please enter 1 or 2.")

def read_text():
    print("Paste text. Press Enter on empty line to predict:")
    lines = []
    prev_empty = False
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line == "":
            if prev_empty or not lines:
                break
            prev_empty = True
            lines.append(line)
        else:
            prev_empty = False
            lines.append(line)
    return "\n".join(lines).strip()

def ask_yes_no(prompt):
    print(prompt + " (yes/no): ", end="", flush=True)
    while True:
        try:
            answer = input().strip().lower()
        except EOFError:
            return False
        if answer in ("yes", "y"):
            return True
        if answer in ("no", "n"):
            return False
        # silently skip garbage lines from paste overflow

def main():
    print("=" * 55)
    print("  Language Detector")
    print("=" * 55)

    variant   = ask_variant()
    normalize = (variant == 2)

    perceptrons    = []
    language_names = []

    # ── Training ──────────────────────────────────────────────────────
    if ask_yes_no("\nStart training?"):
        print(f"\nLoading training data from '{TRAINING_FOLDER}'...")
        dataset = load_dataset(TRAINING_FOLDER, normalize=normalize)

        if not dataset:
            print("No training data found. Exiting.")
            return

        language_names = list(dataset.keys())
        print(f"Languages found : {', '.join(language_names)}")
        print(f"Learning rate   : {LEARNING_RATE}")
        print(f"\n--- Training (Variant {variant}) ---")

        if variant == 1:
            perceptrons = [Perceptron(26, LEARNING_RATE) for _ in language_names]
            train_v1(perceptrons, language_names, dataset)
        else:
            perceptrons = [PerceptronV2(26, LEARNING_RATE) for _ in language_names]
            train_v2(perceptrons, language_names, dataset)

        print("\nTraining complete.")
    else:
        print("Training skipped. Exiting.")
        return

    # ── Testing ───────────────────────────────────────────────────────
    if ask_yes_no("\nStart testing?"):
        print(f"\nLoading test data from '{TEST_FOLDER}'...")
        test_data = load_dataset(TEST_FOLDER, normalize=normalize)

        if not test_data:
            print("No test data found. Skipping.")
        else:
            predict_fn = predict_v1 if variant == 1 else predict_v2

            print(f"\n--- Per-file Predictions (Variant {variant}) ---\n")
            print(f"{'#':<5} {'True':<12} {'Predicted':<12} {'Result'}")
            print("  " + "-" * 44)

            total   = 0
            correct = 0
            idx     = 1

            for true_lang, vectors in test_data.items():
                for vec in vectors:
                    pred = predict_fn(perceptrons, language_names, vec)
                    ok   = pred == true_lang
                    correct += int(ok)
                    total   += 1
                    print(f"{idx:<5} {true_lang:<12} {pred:<12} {'correct' if ok else 'WRONG'}")
                    idx += 1

            acc = correct / total * 100 if total > 0 else 0.0
            print("  " + "-" * 44)
            print(f"Correctly classified : {correct} / {total}")
            print(f"Accuracy             : {acc:.2f}%")

            print(f"\n--- Detailed Metrics ---")
            evaluate(perceptrons, language_names, test_data, variant=variant)

    # ── Classify loop ─────────────────────────────────────────────────
    if ask_yes_no("\nDo you want to classify text?"):
        while True:
            text = read_text()

            if not text:
                print("No text entered.")
            else:
                vec = text_to_vector(text)
                if normalize:
                    vec = normalize_vector(vec)

                result = (predict_v1 if variant == 1 else predict_v2)(
                    perceptrons, language_names, vec
                )

                print(f"\nDetected language : {result}")
                print("Net values:")
                for p, lang in zip(perceptrons, language_names):
                    print(f"  {lang:<14} {p.net(vec):.6f}")
                print()

            if not ask_yes_no("Classify another text?"):
                break

    print("\nGoodbye!")
    print("=" * 55)

if __name__ == "__main__":
    main()