from parsing import get_players, find_next_eligible
def main():
    total_points = 0
    countries = {'fr': 0, 'it': 0, 'ir':0, 'en':0,'wa':0,'sc':0}
    positions = {'fr':0,'h':0,'sr':0,'br':0,'sh':0,'fh':0,'c':0,'b3':0}
    positions_c = {'fr':2,'h':1,'sr':2,'br':3,'sh':1,'fh':1,'c':2,'b3':3}
    stars = 0
    lineup = {'start':0,'bench':0}
    lineup_c = {'start':15,'bench':1}
    squad = []
    db = get_players('prediction.csv')
    print(find_next_eligible(db,countries,positions,positions_c,stars,lineup,lineup_c,squad,244.1))

if __name__ == "__main__":
    main()