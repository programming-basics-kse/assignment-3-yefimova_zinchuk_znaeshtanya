import argparse
from main import installer


def total_output(data):
    countries = {}
    for row in data:
        COUNTRY = row[6]
        MEDAL = row[14]
        if "-" in COUNTRY:
            new_row = COUNTRY.split('-')
            COUNTRY = new_row[0]
        if row[9] in str(args.total) and MEDAL != 'NA':
            if COUNTRY not in countries:
                countries[COUNTRY] = {'Gold': 0, 'Silver': 0, 'Bronze': 0}
            countries[COUNTRY][MEDAL] += 1
    for medal in countries.keys():
        print(f'{medal} - Gold: {countries[medal]['Gold']} - Silver: {countries[medal]['Silver']} - Bronze: {countries[medal]['Bronze']}')


parser = argparse.ArgumentParser(description="process some data")
parser.add_argument('file', type=str, help = 'files')
parser.add_argument('--total','-t', nargs = 1, type=int, help = 'count total')


args = parser.parse_args()
if args.total:
    data = installer(args.file)
    total_output(data)
