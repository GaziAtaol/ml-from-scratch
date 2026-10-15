import math
import random


def squared_distance(a, b):
    total = 0.0
    for x, y in zip(a, b):
        total += (x - y) ** 2
    return total


def assign(points, centers):
    assignment = []
    sse = 0.0
    for p in points:
        best = 0
        best_d = squared_distance(p, centers[0])
        for c in range(1, len(centers)):
            d = squared_distance(p, centers[c])
            if d < best_d:
                best, best_d = c, d
        assignment.append(best)
        sse += best_d
    return assignment, sse


def update_centers(points, assignment, centers):
    k = len(centers)
    dims = len(points[0])
    sums = [[0.0] * dims for _ in range(k)]
    counts = [0] * k
    for p, c in zip(points, assignment):
        counts[c] += 1
        for i in range(dims):
            sums[c][i] += p[i]
    new_centers = []
    for c in range(k):
        if counts[c] == 0:
            new_centers.append(centers[c])
        else:
            new_centers.append([s / counts[c] for s in sums[c]])
    return new_centers


def kmeans(points, k, rng, max_iterations=100, on_iteration=None):
    centers = [list(points[i]) for i in rng.sample(range(len(points)), k)]
    previous = None
    history = []
    for iteration in range(1, max_iterations + 1):
        assignment, sse = assign(points, centers)
        history.append(sse)
        if on_iteration:
            on_iteration(iteration, sse)
        if assignment == previous:
            break
        previous = assignment
        centers = update_centers(points, assignment, centers)
    return assignment, centers, history


def entropy(labels):
    counts = {}
    for label in labels:
        counts[label] = counts.get(label, 0) + 1
    total = len(labels)
    result = 0.0
    for c in counts.values():
        p = c / total
        result -= p * math.log2(p)
    return result, counts
