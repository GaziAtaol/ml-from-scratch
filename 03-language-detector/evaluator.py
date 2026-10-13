def predict_v1(perceptrons, language_names, vector):

    best_lang = None
    best_net  = float("-inf")

    for perceptron, lang in zip(perceptrons, language_names):
        net_val = perceptron.net(vector)
        output  = 1 if net_val > 0 else 0
        if output == 1 and net_val > best_net:
            best_net  = net_val
            best_lang = lang

    if best_lang is None:
        for perceptron, lang in zip(perceptrons, language_names):
            net_val = perceptron.net(vector)
            if net_val > best_net:
                best_net  = net_val
                best_lang = lang

    return best_lang

def predict_v2(perceptrons, language_names, vector):

    best_lang = None
    best_net  = float("-inf")

    for perceptron, lang in zip(perceptrons, language_names):
        net_val = perceptron.net(vector)
        if net_val > best_net:
            best_net  = net_val
            best_lang = lang

    return best_lang

def evaluate(perceptrons, language_names, dataset, variant=1):

    predict_fn = predict_v1 if variant == 1 else predict_v2

    matrix = {t: {p: 0 for p in language_names} for t in language_names}

    for true_lang, vectors in dataset.items():
        for vec in vectors:
            pred_lang = predict_fn(perceptrons, language_names, vec)
            if pred_lang in matrix[true_lang]:
                matrix[true_lang][pred_lang] += 1

    col_w = 12
    print("\nConfusion Matrix (rows=true, cols=predicted):")
    header = f"{'':>{col_w}}" + "".join(f"{lang:>{col_w}}" for lang in language_names)
    print(header)
    print("  " + "-" * len(header))


    for true_lang in language_names:
        row = f"{true_lang:>{col_w}}"
        for pred_lang in language_names:
            row += f"{matrix[true_lang][pred_lang]:>{col_w}}"
        print(row)

    total_correct = 0
    total_samples = 0

    print(f"\n{'Language':<14} {'Precision':>10} {'Recall':>10} {'F1':>10} {'Samples':>10}")
    print("  " + "-" * 58)

    precision_list = []
    recall_list    = []
    f1_list        = []

    for lang in language_names:
        tp = matrix[lang][lang]
        fp = sum(matrix[other][lang] for other in language_names if other != lang)
        fn = sum(matrix[lang][other] for other in language_names if other != lang)
        samples = tp + fn

        precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        recall    = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f1        = (2 * precision * recall / (precision + recall)
                     if (precision + recall) > 0 else 0.0)

        precision_list.append(precision)
        recall_list.append(recall)
        f1_list.append(f1)

        total_correct += tp
        total_samples += samples

        print(f"{lang:<14} {precision:>10.4f} {recall:>10.4f} {f1:>10.4f} {samples:>10}")

    n = len(language_names)
    macro_precision = sum(precision_list) / n
    macro_recall    = sum(recall_list)    / n
    macro_f1        = sum(f1_list)        / n
    accuracy        = total_correct / total_samples if total_samples > 0 else 0.0

    print("  " + "-" * 58)
    print(f"{'Macro avg':<14} {macro_precision:>10.4f} {macro_recall:>10.4f} {macro_f1:>10.4f}")
    print(f"\nAccuracy: {total_correct}/{total_samples}  ({accuracy*100:.2f}%)")

    return accuracy, macro_precision, macro_recall, macro_f1