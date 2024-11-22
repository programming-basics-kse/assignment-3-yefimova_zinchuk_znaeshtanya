def installer(source_file):
    with open(source_file, 'r') as file:
        header = next(file)
        data = []
        line = file.readline()
        while line:
            for line in file:
                line = line[:-1].split('\t')
                data.append(line)
            line = file.readline()
    return data
