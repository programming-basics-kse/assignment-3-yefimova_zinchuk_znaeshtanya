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
        print(f"{country}'s most successful year was {most_medals_year} with {most_medals} medal(s)")
    else:
        print(f'{country} - no medals found/no country found')


def output(data):
    medals = {'Gold': 0, 'Silver': 0, 'Bronze': 0}
    count = 0
    result_1 = ''
    result_2 = ''
    year_found = False
    country_found = False
    for row in data:
        TEAM = row[6]
        NOC = row[7]
        MEDAL = row[14]
        YEAR = row[9]

        if YEAR in str(args.medals):
            year_found = True
            if TEAM in str(args.medals) or NOC in str(args.medals):
                country_found = True
                if MEDAL != 'NA':
                    result_1 += (f'{row[1]} - {row[12]} - {row[-1]}\n')
                    count += 1
                if count == 10:
                    break
    for row in data:
        TEAM = row[6]
        NOC = row[7]
        MEDAL = row[14]
        YEAR = row[9]
        if TEAM in str(args.medals) or NOC in str(args.medals):
            if MEDAL != 'NA' and YEAR in str(args.medals):
                medals[MEDAL] += 1
    if not year_found and not country_found:
        print('Invalid input. No country and year found')
    elif not year_found:
        print('No Olympics were held that year')
    elif not country_found:
        print('Country not found')
    else:
        print(result_1)
        result_2 = (f'Gold:{medals["Gold"]}, Silver:{medals["Silver"]}, Bronze:{medals["Bronze"]}')
        print(result_2)

    return result_1, result_2


def country_validation(COUNTRY):
    if "-" in COUNTRY:
        new_row = COUNTRY.split('-')
        COUNTRY = new_row[0]
    if "/" in COUNTRY:
        new_row = COUNTRY.split('/')
        COUNTRY = new_row[0]
    return COUNTRY

def input_validation(data, country_input):
    if not country_input.isalpha():
        return 'invalid input'
    if country_input not in [row[6].lower() for row in data] and country_input not in [row[7].lower() for row in data]:
        return 'no country'
    return country_input


def years_sorter(data, country_input):
    years = {}
    sums = []
    country_input = input_validation(data, country_input)
    if country_input == 'no country':
        print('Sorry there is no such country')
        return 'no country'
    if country_input == 'invalid input':
        print('Sorry enter valid name')
        return 'invalid input'
    for row in data:
        COUNTRY = row[6].lower()
        COUNTRY_CODE = row[7].lower()
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
    for year in args.total:
        if str(year) not in [row[9] for row in data]:
            print('There were no games this year')
            return 'no games'
    for row in data:
        #COUNTRY = row[6].lower()
        COUNTRY_CODE = row[7].lower()
        MEDAL = row[14]
        YEAR = row[9]
        #COUNTRY = country_validation(COUNTRY)
        if MEDAL != 'NA':
            if YEAR in str(args.total):
                if COUNTRY_CODE not in countries:
                    countries[COUNTRY_CODE] = {'Gold': 0, 'Silver': 0, 'Bronze': 0}
                countries[COUNTRY_CODE][MEDAL] += 1
    for medal in countries.keys():
        print(f'{medal.upper()} - Gold: {countries[medal]['Gold']} - Silver: {countries[medal]['Silver']} - Bronze: {countries[medal]['Bronze']}')


def first_game(data, country_input):
    games = []
    for row in data:
        if country_input.capitalize() in row[6] or country_input.upper() in row[7]:
            games.append(row)
    games.sort(key=lambda row: int(row[9]))
    print(f'The first game was played in {games[0][9]} in {games[0][11]}')

def most_successful(sums):
    sums.sort(key=lambda part: int(part[1]))
    print(
        f'The most successful game was played in {sums[-1][0]} ({sums[-1][1]} medal(s)) and the least successful in {sums[0][0]} ({sums[0][1]} medal(s))')

def average_medals(sums):
    sum_overall = 0
    active_years = 0
    for part in sums:
        sum_overall += part[1]
        active_years += 1
    print(f'Average medals: {round(sum_overall / active_years)}')


parser = argparse.ArgumentParser()
parser.add_argument('file', type=str, help='Choose the file')
parser.add_argument('-medals',  nargs=2, help='Medals for a team during the year')
parser.add_argument('-output', nargs=1, help='Writing the output in the file')
parser.add_argument('-overall', nargs='+', type=str, help='The most successful year for countries input')
parser.add_argument('-total', nargs = 1, type=int, help = 'count total')
parser.add_argument('-interactive', type=str, help = 'see statistics')


args = parser.parse_args()
data = installer(args.file)

if args.medals:
    result_1, result_2 = output(data)
    if args.output:
        with open (args.output[0], 'w') as file:
           file.write(result_1)
           file.write(result_2)

if args.overall:
    for country in args.overall:
        overall(data, country)

if args.total:
    medals_counter(data)

if args.interactive:
    while True:
        country_input = input('Enter a country or a code ').lower()
        sums = years_sorter(data, country_input)
        if sums == 'no country' or sums == 'invalid input':
            continue
        print('\nSTATISTICS: \n')
        first_game(data, country_input)
        most_successful(sums)
        average_medals(sums)
        print('')
        while True:
            continue_game = input('Do you want to continue? ')
            if continue_game == 'no':
                exit()
            elif continue_game != 'yes' or continue_game == 'no':
                print("please enter 'yes' or 'no'")
            else:
                break
