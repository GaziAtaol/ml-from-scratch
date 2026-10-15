# Huffman Coding

Huffman code for a text of any length, written in pure Python. The program prints the code of every character, the encoded string with its length in bits, and the length of the same text with a fixed-length binary code for comparison.

## How it works

1. Count how often each character occurs.
2. Put every character in a priority queue ordered by count.
3. Remove the two least frequent nodes, join them into a new node whose count is their sum, and put it back. Repeat until one tree remains.
4. Read the code of each character from the tree: 0 for a left branch, 1 for a right branch.

Frequent characters get short codes and rare characters get long ones. No code is the beginning of another code, so the encoded string can be decoded without separators. The program decodes its own output and prints whether it matches the input.

The fixed-length code uses `ceil(log2(d))` bits for each character, where `d` is the number of distinct characters in the text.

Ties between equal counts are broken by a fixed rule, so the same text always gives the same code. Other valid Huffman codes for the same text can differ in the bits, but they have the same total length.

## Run

```bash
python main.py
```

Type or paste a text, or give the path of a text file. Spaces and line breaks are encoded like any other character. If the encoded string is longer than 2000 bits, only the first 2000 bits are printed, and the length is still exact.

## Project structure

```
main.py      input and output
huffman.py   frequency count, code construction, encoding and decoding
```

## Example

Input: `this is an example of a huffman tree`

```
char    count  code
' '         7  111
a           4  000
e           4  001
f           3  1101
h           2  0100
i           2  0101
m           2  0110
n           2  0111
s           2  1000
t           2  1001
l           1  10100
o           1  10101
p           1  10110
r           1  10111
u           1  11000
x           1  11001

Huffman code: 135 bits
Fixed-length code (16 distinct characters, 4-bit codes): 144 bits
Decoding check: OK
```

The text has 36 characters, so the fixed-length code needs 144 bits and Huffman needs 135, a saving of 6.2 percent. The entropy of the character distribution puts a lower bound of 133.7 bits on any code that gives each character its own whole number of bits, so 135 is close to the limit.

Another check: `abracadabra` gives 23 bits against 33 bits with 3-bit codes.

## Notes

* The saving is small for short texts with many different characters and grows when a few characters dominate.
* A text with one distinct character gets the code `0`, so the encoded length equals the text length.
* The code table is not stored with the encoded string. To decode the string later, the table is needed as well.
