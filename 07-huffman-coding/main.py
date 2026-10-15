import os

from huffman import frequencies, build_codes, encode, decode, fixed_length_bits

MAX_PRINTED_BITS = 2000


def show_char(ch):
    names = {" ": "' '", "\n": "\\n", "\t": "\\t"}
    return names.get(ch, ch)


def read_text():
    entry = input("Text (or the path of a text file): ")
    if os.path.isfile(entry):
        with open(entry, "r", encoding="utf-8") as f:
            return f.read()
    return entry


def main():
    text = read_text()
    if not text:
        print("The text is empty.")
        return

    counts = frequencies(text)
    codes = build_codes(counts)

    print("\n=== Huffman code ===")
    print(f"{'char':<6}{'count':>7}  code")
    for ch in sorted(codes, key=lambda c: (len(codes[c]), -counts[c], c)):
        print(f"{show_char(ch):<6}{counts[ch]:>7}  {codes[ch]}")

    encoded = encode(text, codes)
    print("\n=== Encoded string ===")
    if len(encoded) <= MAX_PRINTED_BITS:
        print(encoded)
    else:
        print(encoded[:MAX_PRINTED_BITS] + " ...")
        print(f"(first {MAX_PRINTED_BITS} of {len(encoded)} bits shown)")

    per_char = fixed_length_bits(len(counts))
    fixed = per_char * len(text)
    print(f"\nHuffman code: {len(encoded)} bits")
    print(f"Fixed-length code ({len(counts)} distinct characters, {per_char}-bit codes): {fixed} bits")
    print(f"Saving: {100 * (fixed - len(encoded)) / fixed:.1f} %")
    print(f"Decoding check: {'OK' if decode(encoded, codes) == text else 'FAILED'}")

if __name__ == "__main__":
    main()
