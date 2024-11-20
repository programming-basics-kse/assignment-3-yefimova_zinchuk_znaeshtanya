def installer():
    with open('Olympic Athletes - raw.tsv', 'r') as file:
        header = next(file)
        data = []
        line = file.readline()
        while line:
            for line in file:
                line = line[:-1].split('\t')
                data.append(line)
                print(line)
            line = file.readline()
