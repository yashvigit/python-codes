with open('source.txt', 'r') as src, open('target.txt', 'w') as tgt:
    for line in src:
        tgt.write(line.upper())

print("File copied with lowercase converted to uppercase.")