# Import Libs

import requests
import pandas as pd
from tkinter import *
"""
root = Tk()
root.title("Select NBA Season(s)")
root.geometry("840x340")

my_entries = []

def command_select_seasons():

    entry_list = ''

    for entries in my_entries:
        try:
            entry_list = entry_list + str(entries.get()) + '\n'
            my_label.config(text=entry_list)
        except:
            print('error')

    #print(entry_list)

    return entry_list

for x in range(5):
    my_entry = Entry(root)
    my_entry.grid(row=0, column=x, pady=20, padx=20)
    my_entries.append(my_entry)

my_button = Button(root, text="Select", command=command_select_seasons)
my_button.grid(row=1, column=0, pady=20)

my_label = Label(root, text='')
my_label.grid(row=3, column=0, pady=20)

my_label_2 = Label(root, text='Ex: 2022-23')
my_label_2.grid(row=1, column=1, pady=20)

exit_button = Button(root, text="Exit", command=root.destroy)
exit_button.grid(row=4, column=2, pady=20)

root.mainloop()
"""
def get_games():

    #entry_list = command_select_seasons()

    #print(entry_list)

    season_type = input('Insert the season type, "Regular+Season" or "Playoffs": ')

    seasons =input('Enter the seasons you would like to get data from separated by space (ex:"2020-21 2019-20"): ')
    season_list = seasons.split()

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

    # Save to an excel file before transposing the games
    final_df.to_excel('box_scores_'+ season_type +'.xlsx')

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
    #command_select_seasons()
    get_games()