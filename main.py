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
                print(line)
            line = file.readline()
    return data

def output(data):
    medals = {'Gold': 0, 'Silver': 0, 'Bronze': 0}
    count = 0
    result_1 = ''
    for row in data:
        TEAM = row[6]
        NOC = row[7]
        MEDAL = row[14]
        if row[9] in str(args.medals) and MEDAL != 'NA':
            if TEAM in str(args.medals) or NOC in str(args.medals):
                result_1 += (f'{row[1]} - {row[12]} - {row[-1]}\n')
                count += 1
        if TEAM in str(args.medals) or NOC in str(args.medals):
            if MEDAL != 'NA':
                medals[MEDAL] += 1
        if count == 10:
            break
    print(result_1)

    if TEAM not in str(args.medals) and NOC not in str(args.medals):
        print('Country not found')

    if row[9] not in str(args.medals):
        print('No Olympics were held that year')



    result_2 = (f'Gold:{medals["Gold"]}, Silver:{medals["Silver"]}, Bronze:{medals["Bronze"]}')
    print(result_2)

    return result_1, result_2

parser = argparse.ArgumentParser()
parser.add_argument('file', type=str, help='Choose the file')
parser.add_argument('-medals', nargs=2, help='Medals for a team during the year')
parser.add_argument('-output', nargs=1, help='Writing the output in the file')

args = parser.parse_args()



data = installer(args.file)


result_1, result_2 = output(data)
if args.output:
    with open (args.output[0], 'w') as file:
       file.write(result_1)
       file.write(result_2)
