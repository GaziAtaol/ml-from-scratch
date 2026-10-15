import re


def normalize_label(label):
    return re.sub(r"[\s_]+", "-", label.strip().lower())


def load_data(filepath, has_label=True):
    samples = []

    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            parts = [p.strip() for p in line.split("\t") if p.strip()]

            if has_label:

                label = normalize_label(parts[-1])
                attributes = [float(p.replace(",", ".")) for p in parts[:-1]]
            else:

                label = None
                attributes = [float(p.replace(",", ".")) for p in parts]

            samples.append({
                "attributes": attributes,
                "label": label
            })

    return samples


def get_num_attributes(samples):
    if not samples:
        return 0
    return len(samples[0]["attributes"])
