import time


def brute_force(items, capacity):
    start = time.perf_counter()
    order = sorted(items, key=lambda it: it[1])
    n = len(order)
    sizes = [it[1] for it in order]
    values = [it[2] for it in order]

    chosen = []
    best_value = 0
    best_set = []
    size = 0
    value = 0
    checked = 1
    j = 0
    while True:
        if j < n and size + sizes[j] <= capacity:
            size += sizes[j]
            value += values[j]
            chosen.append(j)
            checked += 1
            if value > best_value:
                best_value = value
                best_set = chosen.copy()
            j += 1
        else:
            if not chosen:
                break
            last = chosen.pop()
            size -= sizes[last]
            value -= values[last]
            j = last + 1

    best_items = sorted((order[i] for i in best_set), key=lambda it: it[0])
    used = sum(it[1] for it in best_items)
    seconds = time.perf_counter() - start
    return best_items, best_value, used, seconds, checked


def greedy(items, capacity):
    start = time.perf_counter()
    order = sorted(items, key=lambda it: it[2] / it[1], reverse=True)
    chosen = []
    used = 0
    examined = 0
    for it in order:
        examined += 1
        if used + it[1] <= capacity:
            chosen.append(it)
            used += it[1]
    chosen.sort(key=lambda it: it[0])
    total = sum(it[2] for it in chosen)
    seconds = time.perf_counter() - start
    return chosen, total, used, seconds, examined
