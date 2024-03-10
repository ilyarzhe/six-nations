import csv
from player import Player

def get_players(file_name: str):
    with open(file_name,'r') as file:
        players_dump = csv.reader(file)
        return [Player(row[0], row[1], row[3], row[5], float(row[4]), float(row[2])) for row in players_dump]

def find_next_eligible(db, 
                        countries, 
                        positions, 
                        positions_c,
                        stars,
                        lineup,
                        lineup_c,
                        squad, 
                        total_stars):
    for player in db:
        if countries[player.country] < 4:
            if positions[player.position]<positions_c[player.position]:
                if stars + player.stars <= total_stars:
                    if lineup[player.lineup]< lineup_c[player.lineup]:
                        if player not in squad:
                            return player
    return 0   
            
def find_eligible_team(db, 
                       countries, 
                       positions,
                       positions_c, 
                       stars, 
                       lineup,
                       lineup_c, 
                       squad,
                       total_stars):
    while True:
        next_player = find_next_eligible(db, 
                                         countries, 
                                         positions, 
                                         positions_c, 
                                         stars, 
                                         lineup, 
                                         lineup_c, 
                                         squad, 
                                         total_stars)
        if next_player != 0:
            squad.append(next_player)
            countries[next_player.country]+=1
            if next_player.lineup != 'bench':
                positions[next_player.position]+=1
            lineup[next_player.lineup]+=1
            stars+=next_player.stars
        if lineup['start'] == lineup_c['start'] and lineup['bench'] == lineup_c['bench']:
            break