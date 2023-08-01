import pandas as pd
import tqdm

def org_data():

    teams_stats = pd.read_excel('team_stats.xlsx')
    games = pd.read_excel('games_list_Regular+Season.xlsx')

    games_ids = games['GAME_ID']
    games_ids.drop_duplicates(inplace=True)

    df_h = []
    df_a = []

    for game in games_ids:
        df = games.loc[games['GAME_ID'] == game]
        df_home = df[df['MATCHUP'].str.contains('vs.')]
        df_away = df[df['MATCHUP'].str.contains('@')]
        df_h.append(df_home)
        df_a.append(df_away)
        
    final = pd.concat([df_h, df_a], axis=1)

    final.to_excel('rapaxx.xsls')
        
#df_vs_home = df_final[df_final['MATCHUP'].str.contains('vs.')]

if __name__ == '__main__':
    org_data()