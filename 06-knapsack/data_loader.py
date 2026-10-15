import re


def load_datasets(filepath):
    with open(filepath, "r") as f:
        text = f.read()

    capacity = int(re.search(r"capacity\s+(\d+)", text).group(1))
    sizes = re.findall(r"sizes\s*=\s*\{([^}]*)\}", text)
    values = re.findall(r"vals\s*=\s*\{([^}]*)\}", text)

    datasets = []
    for s, v in zip(sizes, values):
        size_list = [int(x) for x in re.findall(r"\d+", s)]
        value_list = [int(x) for x in re.findall(r"\d+", v)]
        if len(size_list) != len(value_list):
            raise ValueError("sizes and vals have different lengths")
        items = [(i + 1, size_list[i], value_list[i]) for i in range(len(size_list))]
        datasets.append(items)
    return capacity, datasets
