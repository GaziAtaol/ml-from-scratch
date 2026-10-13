def evaluate(perceptron, test_samples):

    correct = 0
    total = len(test_samples)

    print()
    print(f"{'#':<5} {'True label':<12} {'Predicted':<12} {'Result'}")
    print("  " + "-" * 44)

    for i, sample in enumerate(test_samples, 1):
        attributes = sample["attributes"]
        true_label = sample["label"]

        prediction = perceptron.step(attributes)

        if prediction == true_label:
            correct += 1
            status = "correct"
        else:
            status = "WRONG"

        true_str = "setosa"    if true_label == 1 else "non-setosa"
        pred_str = "setosa"    if prediction == 1 else "non-setosa"

        print(f"{i:<5} {true_str:<12} {pred_str:<12} {status}")

    accuracy = (correct / total * 100) if total > 0 else 0.0

    print("  " + "-" * 44)
    print(f"Correctly classified : {correct} / {total}")
    print(f"Accuracy : {accuracy:.2f}%")
    print("  " + "-" * 44)

    return correct, total, accuracy
