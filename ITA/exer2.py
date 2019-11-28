import csv
f = open("appstore_games.csv","r")
reader = csv.DictReader(f)
my_games = list(reader)

print(len(my_games))
puzz_ent_games = []

for item in my_games:
    if "Puzzle" in item["Genres"] and "Entertainment" in item["Genres"] and item["Average User Rating"]:
        puzz_ent_games.append(item)

sorted_user_rating = sorted(puzz_ent_games, key="User Rating Count", reverse=True)

print(puzz_ent_games[0]['Name'])
print(sorted_user_rating[0]['Name'])