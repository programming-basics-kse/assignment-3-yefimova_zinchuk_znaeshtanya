with open('Olympic Athletes - raw.tsv', 'r') as file:
    line = file.readline()
    header = next(file)
    print(header)
    data = []
    for line in file:
        line = line[:-1].split('\t')
        data.append(line)
print(data)
