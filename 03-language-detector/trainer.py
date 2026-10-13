MAX_ITERATIONS  = 500
STOP_THRESHOLD  = 0.01

def train_v1(perceptrons, language_names, dataset):
    print()
    print(f"{'Iteration':<12} {'Total Errors'}")
    print("  " + "-" * 28)

    for iteration in range(1, MAX_ITERATIONS + 1):

        total_errors = 0

        for perceptron, lang in zip(perceptrons, language_names):
            for train_lang, vectors in dataset.items():
                target = 1 if train_lang == lang else 0
                for vec in vectors:
                    total_errors += perceptron.update(vec, target)

        print(f"{iteration:<12} {total_errors}")

        if total_errors == 0:
            print()
            print(f"V1 training converged after {iteration} iteration(s).")
            return iteration

    print()
    print(f"V1 training stopped at max {MAX_ITERATIONS} iterations.")
    return MAX_ITERATIONS

def train_v2(perceptrons, language_names, dataset):
    print()
    print(f"{'Iteration':<12} {'Max |d-y|'}")
    print("  " + "-" * 28)

    for iteration in range(1, MAX_ITERATIONS + 1):

        for perceptron, lang in zip(perceptrons, language_names):
            for train_lang, vectors in dataset.items():
                target = 1.0 if train_lang == lang else -1.0
                for vec in vectors:
                    perceptron.update(vec, target)

        for perceptron in perceptrons:
            perceptron.normalize()

        max_error = 0.0
        for perceptron, lang in zip(perceptrons, language_names):
            for train_lang, vectors in dataset.items():
                target = 1.0 if train_lang == lang else -1.0
                for vec in vectors:
                    err = abs(target - perceptron.net(vec))
                    if err > max_error:
                        max_error = err

        print(f"{iteration:<12} {max_error:.6f}")

        if max_error < STOP_THRESHOLD:
            print()
            print(f"V2 training converged after {iteration} iteration(s).")
            return iteration

    print()
    print(f"V2 training stopped at max {MAX_ITERATIONS} iterations.")
    return MAX_ITERATIONS