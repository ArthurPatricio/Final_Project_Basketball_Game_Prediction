import pandas as pd
import tqdm

def org_data():

    teams_stats = pd.read_excel('team_stats.xlsx')
    games = pd.read_excel('games_list_Regular+Season.xlsx')

    games_ids = games['GAME_ID']
    games_ids.drop_duplicates(inplace=True)

    df_h = []
    df_a = []

    for game in tqdm.tqdm(games_ids):
        df = games.loc[games['GAME_ID'] == game]
        df_home = df[df['MATCHUP'].str.contains('vs.')]
        df_home = df_home.iloc[0]
        df_away = df[df['MATCHUP'].str.contains('@')]
        df_away = df_away.iloc[0]
        df_h.append(df_home)
        df_a.append(df_away)

    df_h = pd.DataFrame(df_h)
    df_h.drop(['Unnamed: 0'], axis=1, inplace=True)
    df_h.reset_index(inplace=True, drop=True)
    df_h.rename(inplace=True, columns={'SEASON_ID': 'HOME_SEASON_ID', 'TEAM_ID': 'HOME_TEAM_ID', 'TEAM_ABBREVIATION': 'HOME_TEAM_ABBREVIATION', 'TEAM_NAME': 'HOME_TEAM_NAME', 'GAME_ID': 'HOME_GAME_ID', 'GAME_DATE': 'HOME_GAME_DATE', 'MATCHUP': 'HOME_MATCHUP', 'WL': 'HOME_WL', 'MIN': 'HOME_MINUTES', 'FGM': 'HOME_FGM', 'FGA': 'HOME_FGA', 'FG_PCT': 'HOME_FG_PCT', 'FG3M': 'HOME_FG3M', 'FG3A': 'HOME_FG3A', 'FG3_PCT': 'HOME_FG3_PCT', 'FTM': 'HOME_FTM', 'FTA': 'HOME_FTA', 'FT_PCT': 'HOME_FT_PCT', 'OREB': 'HOME_OREB', 'DREB': 'HOME_DREB', 'REB': 'HOME_REB', 'AST': 'HOME_AST', 'STL': 'HOME_STL', 'BLK': 'HOME_BLK', 'TOV': 'HOME_TOV', 'PF': 'HOME_PF', 'PTS': 'HOME_PTS', 'PLUS_MINUS': 'HOME_PLUS_MINUS', 'VIDEO_AVAILABLE': 'HOME_VIDEO_AVAILABLE', 'season_id': 'HOME_SEASON_ID', 'GAME_N': 'HOME_GAME_N'})

    df_a = pd.DataFrame(df_a)   
    df_a.drop(['Unnamed: 0'], axis=1, inplace=True)
    df_a.reset_index(inplace=True, drop=True)
    df_a.rename(inplace=True, columns={'SEASON_ID': 'AWAY_SEASON_ID', 'TEAM_ID': 'AWAY_TEAM_ID', 'TEAM_ABBREVIATION': 'AWAY_TEAM_ABBREVIATION', 'TEAM_NAME': 'AWAY_TEAM_NAME', 'GAME_ID': 'AWAY_GAME_ID', 'GAME_DATE': 'AWAY_GAME_DATE', 'MATCHUP': 'AWAY_MATCHUP', 'WL': 'AWAY_WL', 'MIN': 'AWAY_MINUTES', 'FGM': 'AWAY_FGM', 'FGA': 'AWAY_FGA', 'FG_PCT': 'AWAY_FG_PCT', 'FG3M': 'AWAY_FG3M', 'FG3A': 'AWAY_FG3A', 'FG3_PCT': 'AWAY_FG3_PCT', 'FTM': 'AWAY_FTM', 'FTA': 'AWAY_FTA', 'FT_PCT': 'AWAY_FT_PCT', 'OREB': 'AWAY_OREB', 'DREB': 'AWAY_DREB', 'REB': 'AWAY_REB', 'AST': 'AWAY_AST', 'STL': 'AWAY_STL', 'BLK': 'AWAY_BLK', 'TOV': 'AWAY_TOV', 'PF': 'AWAY_PF', 'PTS': 'AWAY_PTS', 'PLUS_MINUS': 'AWAY_PLUS_MINUS', 'VIDEO_AVAILABLE': 'AWAY_VIDEO_AVAILABLE', 'season_id': 'AWAY_SEASON_ID', 'GAME_N': 'AWAY_GAME_N'})

    final = pd.concat([df_h, df_a], axis=1)

    final = final[['HOME_TEAM_ID', 'HOME_TEAM_ABBREVIATION', 'HOME_GAME_ID', 'HOME_MATCHUP', 'HOME_SEASON_ID', 'HOME_GAME_N', 'AWAY_TEAM_ID', 'AWAY_TEAM_ABBREVIATION', 'AWAY_GAME_ID', 'AWAY_MATCHUP', 'AWAY_SEASON_ID', 'AWAY_GAME_N']]

    final.to_excel('org_games.xlsx')

if __name__ == '__main__':
    org_data()