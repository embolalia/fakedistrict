from collections import defaultdict
import csv
import json

# TODO anomalous total votes in NY1, maybe others? any way to detect? presumably total votes will be more or less equal in """contested""" elections
# MIT's source is https://historycms2.house.gov/Institution/Election-Statistics/2020election/ which doesn't mention the 691,731 number anywhere

with open('1976-2020-house.csv') as csvfile:
    dialect = csv.Sniffer().sniff(csvfile.read(1024))
    csvfile.seek(0)

    reader = csv.DictReader(csvfile, dialect=dialect)

    votage = defaultdict(lambda: defaultdict(dict))
    # district: {candidate: {party: pct}
    modes = []

    for row in reader:
        # TODO handle special elections
        if row['year'] != "2020" or row['stage'] != 'gen' or row['special'] == 'TRUE':
            continue
        if row['mode'] not in modes:
            modes.append(row['mode'])

        district = row['state'] + row['district']
        if district != "NEW YORK14":
            continue
        print(row['candidatevotes'], row['candidate'], row['totalvotes'])
        candidate = row['candidate']
        party = row['party']
        percentage = int(row['candidatevotes']) / int(row['totalvotes'])

        votage[district][candidate][party] = percentage

# fusion tickets are great, but a pain to process
winner_data = {}
for district, lines in votage.items():
    if district != "NEW YORK14":
        continue
    print(lines)
    vote_totals = {}
    for candidate, parties in lines.items():
        best_line = max(parties.items(), key=lambda l: l[1])
        party = best_line[0]
        total = sum(parties.values())

        vote_totals[party] = total
    winner = max(vote_totals.items(), key=lambda v: v[1])

    winner_data[district] = list(winner)

# TODO include number of empty ballots already cast
with open('data.json', 'w') as out:
    out.write("districtData = ")
    json.dump(winner_data, out)