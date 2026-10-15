import math


def separate_by_class(samples):
    separated = {}
    for sample in samples:
        label = sample['label']
        if label not in separated:
            separated[label] = []
        separated[label].append(sample["attributes"])
    return separated


def calculate_mean(values):

    total = 0.0
    count = 0
    for v in values:
        total += v
        count += 1
    return total / count


def calculate_stdev(values, mean):
    total = 0.0
    count = 0
    for v in values:
        total = total + (v - mean)**2
        count += 1
    return math.sqrt(total / count)


def calculate_class_statistics(separated):
    statistics = {}
    for label, rows in separated.items():
        num_attributes = len(rows[0])
        stats = []
        for i in range(num_attributes):
            column_values = []
            for row in rows:
                column_values.append(row[i])
            mean = calculate_mean(column_values)
            stdev = calculate_stdev(column_values, mean)
            stats.append((mean, stdev))
        statistics[label] = stats
    return statistics


def calculate_priors(separated, total_count):
    priors = {}
    for label, rows in separated.items():
        count = 0
        for _ in rows:
            count += 1
        priors[label] = count / total_count
    return priors


def train(samples):
    separated = separate_by_class(samples)

    total = 0
    for label in separated:
        for _ in separated[label]:
            total = total + 1

    statistics = calculate_class_statistics(separated)
    priors = calculate_priors(separated, total)

    print("=== Training results ===\n")
    for label in statistics:
        print(f"Label: {label}  |  Prior: {priors[label]:.4f}")
        for i, (m, s) in enumerate(statistics[label]):
            print(f"  attribute {i+1}: μ = {m:.4f}, σ = {s:.4f}")
        print()

    return statistics, priors, separated


def check_and_apply_smoothing(statistics, priors, separated, epsilon=1e-6):
    print("=== SMOOTHING CONTROL ===\n")
    smoothing_applied = False

    for label in statistics:
        for i in range(len(statistics[label])):
            mean, stdev = statistics[label][i]
            if stdev == 0:
                print(f"  Smoothing needed: class={label}, attribute {i+1}")
                print(f"    BEFORE  -> μ = {mean:.6f}, σ = {stdev:.6f}")
                stdev = stdev + epsilon
                statistics[label][i] = (mean, stdev)
                print(f"    AFTER -> μ = {mean:.6f}, σ = {stdev:.6f}")
                smoothing_applied = True

    if not smoothing_applied:
        print("\n  There is no need for smoothing.")
        print("  smoothing applied for rule:\n")
        for label in statistics:
            mean, stdev = statistics[label][0]
            print(f"  Class={label}, Attribute 1")
            print(f"    BEFORE  -> μ = {mean:.6f}, σ = {stdev:.6f}")
            stdev = stdev + epsilon
            statistics[label][0] = (mean, stdev)
            print(f"    AFTER -> μ = {mean:.6f}, σ = {stdev:.6f}")

    return statistics


def gaussian_probability(x, mean, stdev):
    exponent = -((x - mean) ** 2) / (2 * stdev ** 2)
    return (1 / (stdev * math.sqrt(2 * math.pi))) * math.exp(exponent)


def calculate_class_probabilities(statistics, priors, input_vector):
    probabilities = {}
    for label in statistics:
        probabilities[label] = priors[label]
        for i in range(len(statistics[label])):
            mean, stdev = statistics[label][i]
            probabilities[label] = probabilities[label] * gaussian_probability(input_vector[i], mean, stdev)
    return probabilities


def predict(statistics, priors, input_vector):
    probabilities = calculate_class_probabilities(statistics, priors, input_vector)
    best_label = None
    best_prob = -1
    for label in probabilities:
        if best_label is None or probabilities[label] > best_prob:
            best_label = label
            best_prob = probabilities[label]
    return best_label, best_prob


def evaluate(statistics, priors, test_data):
    correct = 0
    total = 0
    predictions = []

    for sample in test_data:
        actual = sample["label"]
        predicted, prob = predict(statistics, priors, sample["attributes"])
        predictions.append((actual, predicted))
        if actual == predicted:
            correct = correct + 1
        total = total + 1

    accuracy = (correct / total) * 100

    print(f"=== RESULTS ===\n")
    print(f"TRUE PREDICT: {correct} / {total}")
    print(f"Accuracy: {accuracy:.2f}%\n")

    return accuracy, predictions


def build_confusion_matrix(predictions):
    labels = []
    for actual, predicted in predictions:
        found = False
        for l in labels:
            if l == actual:
                found = True
        if not found:
            labels.append(actual)

    labels.sort()

    size = 0
    for _ in labels:
        size = size + 1

    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(0)
        matrix.append(row)

    label_to_index = {}
    idx = 0
    for l in labels:
        label_to_index[l] = idx
        idx = idx + 1

    for actual, predicted in predictions:
        i = label_to_index[actual]
        j = label_to_index[predicted]
        matrix[i][j] = matrix[i][j] + 1

    print("=== CONFUSION MATRIX ===\n")

    header = "                "
    for l in labels:
        header = header + l + "  "
    print(header)

    for i in range(size):
        row_str = labels[i]
        while len(row_str) < 16:
            row_str = row_str + " "
        for j in range(size):
            cell = str(matrix[i][j])
            while len(cell) < len(labels[j]) + 2:
                cell = " " + cell
            row_str = row_str + cell
        print(row_str)

    print()
    return matrix, labels
