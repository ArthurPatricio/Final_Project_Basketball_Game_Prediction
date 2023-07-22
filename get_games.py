import pandas as pd
import requests
import json
import tqdm

def get_games():
    headers  = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'x-nba-stats-token': 'true',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        'x-nba-stats-origin': 'stats',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Referer': 'https://stats.nba.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    parameters = {
                'Counter': 1000,
                'DateFrom': '',
                'DateTo': '',
                'Direction': "DESC",
                'LeagueID': "00",
                'PlayerOrTeam': "T",
                'Season': "2022-23",
                'SeasonType': "Regular Season",
                'Sorter': "DATE",
                }

    columns_list = {
                    0:"TEAM_ID", 
                    1:"TEAM_NAME",
                    2:"GP",
                    3:"W",
                    4:"L",
                    5:"W_PCT",
                    6:"MIN",
                    7:"FGM",
                    8:"FGA",
                    9:"FG_PCT",
                    10:"FG3M",
                    11:"FG3A",
                    12:"FG3_PCT",
                    13:"FTM",
                    14:"FTA",
                    15:"FT_PCT",
                    16:"OREB",
                    17:"DREB",
                    18:"REB",
                    19:"AST",
                    20:"TOV",
                    21:"STL",
                    22:"BLK",
                    23:"BLKA",
                    24:"PF",
                    25:"PFD",
                    26:"PTS",
                    27:"PLUS_MINUS",
                    28:"GP_RANK",
                    29:"W_RANK",
                    30:"L_RANK",
                    31:"W_PCT_RANK",
                    32:"MIN_RANK",
                    33:"FGM_RANK",
                    34:"FGA_RANK",
                    35:"FG_PCT_RANK",
                    36:"FG3M_RANK",
                    37:"FG3A_RANK",
                    38:"FG3_PCT_RANK",
                    39:"FTM_RANK",
                    40:"FTA_RANK",
                    41:"FT_PCT_RANK",
                    42:"OREB_RANK",
                    43:"DREB_RANK",
                    44:"REB_RANK",
                    45:"AST_RANK",
                    46:"TOV_RANK",
                    47:"STL_RANK",
                    48:"BLK_RANK",
                    49:"BLKA_RANK",
                    50:"PF_RANK",
                    51:"PFD_RANK",
                    52:"PTS_RANK",
                    53:"PLUS_MINUS_RANK"
                    }

    game_dates = pd.read_excel('box_scores_Regular+Season.xlsx')
    game_dates = game_dates['GAME_DATE'] + "-" + game_dates['season_id']
    game_dates.drop_duplicates(inplace=True)
    game_dates = game_dates.to_list()

    dfs=[]
    for game_date in tqdm.tqdm(game_dates):
        gm_dt = game_date
        game_date = game_date.split('-')
        season = game_date[3]
        season_s = season.split('_')
    #for season_id in season_list:
        games_info_url = f'https://stats.nba.com/stats/leaguedashteamstats?Conference=&DateFrom=&DateTo={game_date[1]}%2F{game_date[2]}%2F{game_date[0]}&Division=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=PerGame&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season={season_s[0]}-{season_s[1]}&SeasonSegment=&SeasonType=Regular%20Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision='
        #json response
        response = requests.get(url=games_info_url, headers=headers).json()
        #pulling just desired data
        games_info = response['resultSets'][0]['rowSet']
        df = pd.DataFrame(games_info)
        df['GAME_DATE'] = gm_dt
        df['SEASON'] = season
        #print(gm_dt)
        #print(f'{game_date[1]}%2F{game_date[2]}%2F{game_date[0]}')
        dfs.append(df) 

    final_df = pd.concat(dfs)

    final_df = final_df.rename(columns=columns_list)

    final_df.to_excel('test_v2.xlsx')

'''
# Import Libs

import requests
import pandas as pd
from tkinter import *

def get_games():

    #entry_list = command_select_seasons()

    #print(entry_list)

    #season_type = input('Insert the season type, "Regular+Season" or "Playoffs": ')

    season_type = 'Regular+Season'

    #seasons =input('Enter the seasons you would like to get data from separated by space (ex:"2020-21 2019-20"): ')

    season_list = ['2022-23',
               '2021-22',
               '2020-21',
               '2019-20',
               '2018-19',
               '2017-18',]

    #season_list = seasons.split()

    per_mode = 'PerGame'

    headers  = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'x-nba-stats-token': 'true',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        'x-nba-stats-origin': 'stats',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Referer': 'https://stats.nba.com/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    # Column names from stats.nba.com

    columns_list_games = [

    "SEASON_ID",
    "TEAM_ID",
    "TEAM_ABBREVIATION",
    "TEAM_NAME",
    "GAME_ID",
    "GAME_DATE",
    "MATCHUP",
    "WL",
    "MIN",
    "FGM",
    "FGA",
    "FG_PCT",
    "FG3M",
    "FG3A",
    "FG3_PCT",
    "FTM",
    "FTA",
    "FT_PCT",
    "OREB",
    "DREB",
    "REB",
    "AST",
    "STL",
    "BLK",
    "TOV",
    "PF",
    "PTS",
    "PLUS_MINUS",
    "VIDEO_AVAILABLE"
    ]
   
    # List of season_ids

    # season_list = ['2020-21', '2019-20', '2018-19', '2017-18', '2016-17']

    dfs=[]
    for season_id in season_list:
    #for season_id in season_list:
        games_info_url = 'https://stats.nba.com/stats/leaguegamelog?Counter=1000&DateFrom=&DateTo=&Direction=DESC&LeagueID=00&PlayerOrTeam=T&Season='+season_id+'&SeasonType='+season_type+'&Sorter=DATE'
        #json response
        response = requests.get(url=games_info_url, headers=headers).json()
        #pulling just desired data
        games_info = response['resultSets'][0]['rowSet']
        df = pd.DataFrame(games_info, columns=columns_list_games)
        df['season_id'] =season_id
        print(season_id)
        dfs.append(df) 

    # Save DataFrame to an excel file

    final_df = pd.concat(dfs, sort=False)

    # Reset index

    final_df = final_df.reset_index(drop=True)

    # Save to an excel file before transposing the games
    final_df.to_excel('box_scores_'+ season_type +'.xlsx')

    '''
'''
    df_vs_home = final_df[final_df['MATCHUP'].str.contains('vs.')]
    df_at_away = final_df[final_df['MATCHUP'].str.contains('@')]
    df_vs_home = df_vs_home.rename(columns={'SEASON_ID': 'HOME_SEASON_ID', 'TEAM_ID': 'HOME_TEAM_ID', 'TEAM_ABBREVIATION': 'HOME_TEAM_ABBREVIATION', 'TEAM_NAME': 'HOME_TEAM_NAME', 'GAME_ID': 'HOME_GAME_ID', 'GAME_DATE': 'HOME_GAME_DATE', 'MATCHUP': 'HOME_MATCHUP', 'WL': 'HOME_WL', 'MIN': 'HOME_MINUTES', 'FGM': 'HOME_FGM', 'FGA': 'HOME_FGA', 'FG_PCT': 'HOME_FG_PCT', 'FG3M': 'HOME_FG3M', 'FG3A': 'HOME_FG3A', 'FG3_PCT': 'HOME_FG3_PCT', 'FTM': 'HOME_FTM', 'FTA': 'HOME_FTA', 'FT_PCT': 'HOME_FT_PCT', 'OREB': 'HOME_OREB', 'DREB': 'HOME_DREB', 'REB': 'HOME_REB', 'AST': 'HOME_AST', 'STL': 'HOME_STL', 'BLK': 'HOME_BLK', 'TOV': 'HOME_TOV', 'PF': 'HOME_PF', 'PTS': 'HOME_PTS', 'PLUS_MINUS': 'HOME_PLUS_MINUS', 'VIDEO_AVAILABLE': 'HOME_VIDEO_AVAILABLE', 'season_id': 'HOME_SEASON_ID'})

    df_at_away = df_at_away.rename(columns={'SEASON_ID': 'AWAY_SEASON_ID', 'TEAM_ID': 'AWAY_TEAM_ID', 'TEAM_ABBREVIATION': 'AWAY_TEAM_ABBREVIATION', 'TEAM_NAME': 'AWAY_TEAM_NAME', 'GAME_ID': 'AWAY_GAME_ID', 'GAME_DATE': 'AWAY_GAME_DATE', 'MATCHUP': 'AWAY_MATCHUP', 'WL': 'AWAY_WL', 'MIN': 'AWAY_MINUTES', 'FGM': 'AWAY_FGM', 'FGA': 'AWAY_FGA', 'FG_PCT': 'AWAY_FG_PCT', 'FG3M': 'AWAY_FG3M', 'FG3A': 'AWAY_FG3A', 'FG3_PCT': 'AWAY_FG3_PCT', 'FTM': 'AWAY_FTM', 'FTA': 'AWAY_FTA', 'FT_PCT': 'AWAY_FT_PCT', 'OREB': 'AWAY_OREB', 'DREB': 'AWAY_DREB', 'REB': 'AWAY_REB', 'AST': 'AWAY_AST', 'STL': 'AWAY_STL', 'BLK': 'AWAY_BLK', 'TOV': 'AWAY_TOV', 'PF': 'AWAY_PF', 'PTS': 'AWAY_PTS', 'PLUS_MINUS': 'AWAY_PLUS_MINUS', 'VIDEO_AVAILABLE': 'AWAY_VIDEO_AVAILABLE', 'season_id': 'AWAY_SEASON_ID'})

    df_vs_home = df_vs_home.reset_index()
    df_at_away = df_at_away.reset_index()

    df_final = pd.concat([df_vs_home, df_at_away], axis=1)

    df_final.columns.value_counts()

    df_final = df_final.drop(['index'], axis = 1)
    
    df_final.to_excel('games_list_'+ season_type +'.xlsx')
    '''
if __name__ == '__main__':
        get_games()