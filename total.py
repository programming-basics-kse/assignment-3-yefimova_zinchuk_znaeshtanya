import argparse
from main import installer


def country_validation(COUNTRY):
    if "-" in COUNTRY:
        new_row = COUNTRY.split('-')
        COUNTRY = new_row[0]
    if "/" in COUNTRY:
        new_row = COUNTRY.split('/')
        COUNTRY = new_row[0]
    return COUNTRY


def years_sorter(data):
    years = {}
    sums = []
    for row in data:
        COUNTRY = row[6]
        COUNTRY_CODE = row[7]
        MEDAL = row[14]
        YEAR = row[9]
        COUNTRY = country_validation(COUNTRY)
        if MEDAL != 'NA':
            if COUNTRY == country_input or COUNTRY_CODE == country_input:
                if YEAR not in years:
                    years[YEAR] = {'Gold': 0, 'Silver': 0, 'Bronze': 0}
                years[YEAR][MEDAL] += 1
    for year in years:
        medals_sum = sum([years[year]['Gold'], years[year]['Silver'], years[year]['Bronze']])
        sums.append((year, medals_sum))
    return sums


def medals_counter(data):
    countries = {}
    for row in data:
        COUNTRY = row[6]
        MEDAL = row[14]
        YEAR = row[9]
        COUNTRY = country_validation(COUNTRY)
        if MEDAL != 'NA':
            if YEAR in str(args.total):
                if COUNTRY not in countries:
                    countries[COUNTRY] = {'Gold': 0, 'Silver': 0, 'Bronze': 0}
                countries[COUNTRY][MEDAL] += 1
    for medal in countries.keys():
        print(f'{medal} - Gold: {countries[medal]['Gold']} - Silver: {countries[medal]['Silver']} - Bronze: {countries[medal]['Bronze']}')


def first_game(data, country_input):
    games = []
    for row in data:
        if country_input in row[6] or country_input in row[7]:
            games.append(row)
    games.sort(key=lambda row: int(row[9]))
    print(f'The first game was played in {games[0][9]} in {games[0][11]}')


def most_successful(sums):
    sums.sort(key=lambda part: int(part[1]))
    print(f'The most successful game was played in {sums[-1][0]} ({sums[-1][1]} medal(s)) and the least successful in {sums[0][0]} ({sums[0][1]} medal(s))')


def average_medals(sums):
    sum_overall = 0
    active_years = 0
    for part in sums:
        sum_overall+=part[1]
        active_years+=1
    print(f'Average medals: {round(sum_overall/active_years)}')


parser = argparse.ArgumentParser(description="process some data")
parser.add_argument('file', type=str, help = 'files')
parser.add_argument('--total','-t', nargs = 1, type=int, help = 'count total')
parser.add_argument('--interactive','-i', type=str, help = 'see statistics')


args = parser.parse_args()
data = installer(args.file)


if args.total:
    medals_counter(data)
elif args.interactive:
    while True:
        country_input = input('Enter a country or a code ')
        print('\nSTATISTICS: \n')
        sums = years_sorter(data)
        first_game(data, country_input)
        most_successful(sums)
        average_medals(sums)
        print('')
        continue_game = input('Do you wan to continue? ')
        if continue_game == 'no':
            break
