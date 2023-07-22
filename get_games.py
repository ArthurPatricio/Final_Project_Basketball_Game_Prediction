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

    '''
    season_list = ['2022-23', '2021-22', '2020-21', '2019-20', '2018-19', '2017-18']

    dfs_2=[]

    for season_id in tqdm.tqdm(season_list):
        games_info_url = 'https://stats.nba.com/stats/leaguegamelog?Counter=1000&DateFrom=&DateTo=&Direction=DESC&LeagueID=00&PlayerOrTeam=T&Season='+season_id+'&SeasonType=Regular+Season&Sorter=DATE'
        #json response
        response = requests.get(url=games_info_url, headers=headers).json()
        #pulling just desired data
        games_info = response['resultSets'][0]['rowSet']
        df = pd.DataFrame(games_info, columns=columns_list_games)
        df['season_id'] =season_id
        #print(season_id)
        dfs_2.append(df) 

    final_df_2 = pd.concat(dfs_2, sort=False)

    final_df_2.to_excel('alou.xlsx')  
    '''
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

    final_df.drop_duplicates(subset=['TEAM_ID', 'GP', 'SEASON'], inplace=True)

    final_df.to_excel('team_stats.xlsx')

if __name__ == '__main__':
        get_games()