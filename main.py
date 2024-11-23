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

def overall(data, country):

    country_medals = {}
    for row in data:
        YEAR = row[9]
        COUNTRY = row[6]
        MEDAL = row[14]
        if COUNTRY == country and MEDAL != 'NA':
            if YEAR not in country_medals:
                country_medals[YEAR] = 0
            country_medals[YEAR] += 1
    if country_medals:
        most_medals = max(country_medals.values())
        key_list = list(country_medals.keys())
        value_list = list(country_medals.values())
        most_medals_year = key_list[value_list.index(most_medals)]
        print(f'{country} - {most_medals_year} - {most_medals}')
    else:
        print(f'{country} - no medals')

parser = argparse.ArgumentParser()
parser.add_argument('file', help='files')
parser.add_argument('-overall', nargs='+', type=str, help='The most successful year for countries input')

args = parser.parse_args()
data = installer(args.file)

if args.overall:
    for country in args.overall:
        overall(data, country)