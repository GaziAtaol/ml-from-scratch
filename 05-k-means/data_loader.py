def load_iris(filepath):
    samples = []
    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = [p.strip() for p in line.split("\t") if p.strip()]
            attributes = [float(p.replace(",", ".")) for p in parts[:-1]]
            label = parts[-1]
            samples.append({"attributes": attributes, "label": label})
    return samples
