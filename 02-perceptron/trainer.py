MAX_ITERATIONS = 500

def train(perceptron, samples):

    print()
    print(f"{'Iteration':<12} {'Errors'}")
    print("  " + "-" * 24)

    for iteration in range(1, MAX_ITERATIONS + 1):

        total_errors = 0

        for sample in samples:
            error = perceptron.update(sample["attributes"], sample["label"])
            if error != 0:
                total_errors += 1

        print(f"{iteration:<12} {total_errors}")

        if total_errors == 0:
            print()
            print(f"Training completed converged after {iteration} iteration(s).")
            return iteration

    print()
    print(f"Training stopped reached max {MAX_ITERATIONS} iterations.")
    print(f"The data may not be linearly separable.")
    return MAX_ITERATIONS