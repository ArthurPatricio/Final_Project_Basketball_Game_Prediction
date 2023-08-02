# Import Libs

import requests
import pandas as pd
import tqdm

def get_games():

    season_type = input('Insert the season type, "Regular+Season" or "Playoffs": ')

    #seasons =input('Enter the seasons you would like to get data from separated by space (ex:"2020-21 2019-20"): ')
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

    season_list = ['2022-23', '2021-22', '2020-21', '2019-20', '2018-19', '2017-18']

    dfs=[]

    for season_id in tqdm.tqdm(season_list):
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

    team_ids = final_df['TEAM_ID']

    team_ids.drop_duplicates(inplace=True)

    df_b = []

    for team_id in tqdm.tqdm(team_ids):
        for season in tqdm.tqdm(season_list):             
            df_a = final_df.loc[(final_df['season_id'] == season) & (final_df['TEAM_ID'] == team_id)]
            #print(season)
            #print(team_id)
            #print(df_a)
            df_a.sort_values(by=['GAME_DATE'], ascending=True, inplace=True)
            #print(len(df_a))
            df_a['GAME_N'] = range(1,len(df_a)+1)
            df_b.append(df_a)

    df_final = pd.concat(df_b, sort=False)

    df_final.reset_index(drop=True, inplace=True)

    df_final.to_excel('games_list_'+ season_type +'.xlsx')

if __name__ == '__main__':
    get_games()
