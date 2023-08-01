import pandas as pd
import tqdm

def org_data():

    teams_stats = pd.read_excel('team_stats.xlsx')
    games = pd.read_excel('games_list_Regular+Season.xlsx')

    for game in games['GAME_ID']:
        df_home = games.loc[games['GAME_ID'] == game]
        print(df_home.loc[0]['MATCHUP'])


if __name__ == '__main__':
    org_data()