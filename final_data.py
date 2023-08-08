import pandas as pd
import tqdm


def final_data():

    final = pd.read_excel('test_org_games.xlsx')
    teams_stats = pd.read_excel('test_teams_stats_Regular+Season.xlsx')

    left_join = pd.merge(final, teams_stats, left_on='HOME_COMPARE', right_on='COMPARE')
    left_join = pd.merge(left_join, teams_stats, left_on='AWAY_COMPARE', right_on='COMPARE')

    left_join.drop("Unnamed: 0_x",axis=1, inplace=True)
    left_join.drop("Unnamed: 0_y",axis=1, inplace=True)
    left_join.drop("Unnamed: 0",axis=1, inplace=True)

    left_join.to_excel('test_left_join.xlsx')
    left_join.to_json('test_json.json', orient='index')


if __name__ == '__main__':
        final_data()