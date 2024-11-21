import argparse



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

def output(data):
    medals = {'Gold': 0, 'Silver': 0, 'Bronze': 0}
    count = 0
    for row in data:
        TEAM = row[6]
        NOC = row[7]
        MEDAL = row[14]
        if row[9] in str(args.medals) and MEDAL != 'NA':
            if TEAM in str(args.medals) or NOC in str(args.medals):
                print(f'{row[1]} - {row[12]} - {row[-1]}')
                count += 1
        if TEAM in str(args.medals) or NOC in str(args.medals):
            if MEDAL != 'NA':
                medals[MEDAL] += 1
        if count == 10:
            break

        if TEAM not in str(args.medals) or NOC not in in str(args.medals):
            print('Country not found')

        if row[9] not in str(args.medals):
            print('No Olympics were held that year')



    print(f'Gold:{medals['Gold']}, Silver:{medals['Silver']}, Bronze:{medals['Bronze']}')


parser = argparse.ArgumentParser()
parser.add_argument('file', type=str, help='Choose the file')
parser.add_argument('-medals', nargs=2, help='Medals for a team during the year')

args = parser.parse_args()
data = installer(args.file)
output(data)