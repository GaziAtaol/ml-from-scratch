import heapq
import math


def frequencies(text):
    counts = {}
    for ch in text:
        counts[ch] = counts.get(ch, 0) + 1
    return counts


def build_codes(counts):
    if not counts:
        return {}
    if len(counts) == 1:
        return {next(iter(counts)): "0"}

    heap = []
    order = 0
    for ch in sorted(counts, key=lambda c: (counts[c], c)):
        heap.append((counts[ch], order, ch))
        order += 1
    heapq.heapify(heap)

    while len(heap) > 1:
        f1, _, left = heapq.heappop(heap)
        f2, _, right = heapq.heappop(heap)
        heapq.heappush(heap, (f1 + f2, order, (left, right)))
        order += 1

    codes = {}
    stack = [(heap[0][2], "")]
    while stack:
        node, prefix = stack.pop()
        if isinstance(node, tuple):
            stack.append((node[1], prefix + "1"))
            stack.append((node[0], prefix + "0"))
        else:
            codes[node] = prefix
    return codes


def encode(text, codes):
    return "".join(codes[ch] for ch in text)


def decode(bits, codes):
    reverse = {code: ch for ch, code in codes.items()}
    result = []
    current = ""
    for b in bits:
        current += b
        if current in reverse:
            result.append(reverse[current])
            current = ""
    return "".join(result)


def fixed_length_bits(distinct):
    if distinct <= 1:
        return 1
    return math.ceil(math.log2(distinct))
