import random

from data_loader import load_iris
from kmeans import kmeans, entropy

DATA_FILE = "data/iris.txt"
SEED = 0


def read_k(n_samples):
    while True:
        text = input("Number of clusters k (at least 3): ").strip()
        try:
            k = int(text)
        except ValueError:
            print("Enter a whole number.")
            continue
        if k < 3 or k > n_samples:
            print(f"k must be between 3 and {n_samples}.")
            continue
        return k


def main():
    samples = load_iris(DATA_FILE)
    points = [s["attributes"] for s in samples]
    k = read_k(len(points))
    rng = random.Random(SEED)

    print("\n=== Iterations ===")

    def show(iteration, sse):
        print(f"Iteration {iteration:2d}: sum of squared distances = {sse:.4f}")

    assignment, centers, history = kmeans(points, k, rng, on_iteration=show)
    print(f"\nStopped after {len(history)} iterations, no point changed its cluster.")

    print("\n=== Clusters (the decision attribute was not used for clustering) ===")
    weighted = 0.0
    for c in range(k):
        members = [i for i in range(len(points)) if assignment[i] == c]
        print(f"\nCluster {c + 1}: {len(members)} points")
        center_text = ", ".join(f"{x:.3f}" for x in centers[c])
        print(f"  center: ({center_text})")
        if not members:
            print("  empty cluster")
            continue
        h, counts = entropy([samples[i]["label"] for i in members])
        weighted += h * len(members) / len(points)
        print(f"  entropy: {h:.4f} bits")
        distribution = ", ".join(f"{name}: {n}" for name, n in sorted(counts.items()))
        print(f"  decision attribute: {distribution}")
        for i in members:
            values = ", ".join(f"{x:.1f}" for x in points[i])
            print(f"  #{i + 1:3d}  ({values})  {samples[i]['label']}")

    print(f"\nWeighted average entropy: {weighted:.4f} bits")

if __name__ == "__main__":
    main()
