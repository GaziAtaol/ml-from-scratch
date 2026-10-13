import os
import math

def text_to_vector(text):

    counts = [0] * 26
    total  = 0
    for ch in text.upper():
        if 'A' <= ch <= 'Z':
            counts[ord(ch) - ord('A')] += 1
            total += 1
    if total == 0:
        return [0.0] * 26
    return [c / total for c in counts]

def normalize_vector(v):

    norm = math.sqrt(sum(x * x for x in v))
    if norm == 0.0:
        return [0.0] * len(v)
    return [x / norm for x in v]

def load_dataset(root_folder, normalize=False):

    if not os.path.isdir(root_folder):
        raise FileNotFoundError(f"no directory found: {root_folder}")

    dataset = {}

    for lang in sorted(os.listdir(root_folder)):
        lang_path = os.path.join(root_folder, lang)
        if not os.path.isdir(lang_path):
            continue

        vectors = []
        for fname in sorted(os.listdir(lang_path)):
            if not fname.endswith(".txt"):
                continue
            fpath = os.path.join(lang_path, fname)
            try:
                with open(fpath, encoding="utf-8", errors="ignore") as f:
                    text = f.read()
            except OSError:
                continue

            vec = text_to_vector(text)
            if normalize:
                vec = normalize_vector(vec)
            vectors.append(vec)

        if vectors:
            dataset[lang] = vectors

    return dataset