from algorithm import (
    train,
    check_and_apply_smoothing,
    evaluate,
    build_confusion_matrix,
    predict
)
from data_loader import load_data


def manual_input_loop(statistics, priors):
    print("=== MANUEL CLASSIFICATION ===")
    print("PRESS Q TO EXIT.\n")

    while True:
        user_input = input("ENTER 4 ATTRIBUTES ")
        user_input = user_input.strip()

        if user_input.lower() == "q":
            print("EXECUTING.")
            break

        parts = []
        if "," in user_input:
            for p in user_input.split(","):
                parts.append(p.strip())
        else:
            for p in user_input.split():
                parts.append(p.strip())

        count = 0
        for _ in parts:
            count = count + 1

        if count != 4:
            print("YOU HAVE TO ENTER 4 ATTRIBUTE\n")
            continue

        valid = True
        attributes = []
        for p in parts:
            try:
                value = float(p.replace(",", "."))
                attributes.append(value)
            except:
                print(f"ERROR: '{p}' IS A NOT VALID NUMBER.\n")
                valid = False
                break

        if not valid:
            continue

        predicted, prob = predict(statistics, priors, attributes)

        print(f"\n  INPUT: {attributes}")
        print(f"  PREDICT: {predicted}")
        print(f"  PROBABILITY: {prob:.6f}\n")


def main():

    train_data = load_data("training-data/iris_training.txt")
    test_data = load_data("test-data/iris_test.txt")

    statistics, priors, separated = train(train_data)

    statistics = check_and_apply_smoothing(statistics, priors, separated)

    accuracy, predictions = evaluate(statistics, priors, test_data)
    build_confusion_matrix(predictions)

    manual_input_loop(statistics, priors)

if __name__ == "__main__":
    main()
