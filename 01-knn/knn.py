import math
from collections import Counter


def euclidean_distance(x, y):

    return math.sqrt(sum((xi - yi) ** 2 for xi, yi in zip(x, y)))

def get_neighbours(training_data, test_sample, k):
  
    k = min(k, len(training_data))

    distances = []
    for sample in training_data:
        dist = euclidean_distance(test_sample["attributes"], sample["attributes"])
        distances.append((dist, sample))

    distances.sort(key=lambda pair: pair[0])

    return distances[:k]


def classify(training_data, test_sample, k):
 
    neighbours = get_neighbours(training_data, test_sample, k)

    vote_counts = Counter(sample["label"] for dist, sample in neighbours)
    max_votes   = max(vote_counts.values())
    top_classes = [label for label, count in vote_counts.items() if count == max_votes]

    if len(top_classes) == 1:
        return top_classes[0]

    for dist, sample in neighbours:
        if sample["label"] in top_classes:
            return sample["label"]
