# Final_Project_Basketball_Game_Prediction

# Objetivo

* Este projeto visa primeiramente realizar uma análise exploratória dos dados obtidos das últimas 6 temporadas regulares da NBA (2017-18 a 2022-23) e treinar uma rede neural com o intuito de prever-se o time vencedor de uma partida.

# Obtenção e manipulação dos dados

* Os dados foram obtidos através da API da NBA, o script 'get_team_stats.py' obtém as médias estatísticas de todos os times após cada jogo da temporada regular das úlitmas 6 temporadas (2017-18 a 2022-23). Ele pode ser oncontrato em:

    - (https://github.com/ArthurPatricio/Final_Project_Basketball_Game_Prediction/blob/main/get_team_stats.py)
* O script 'get_games.py' obtém a lista de todos os jogos das últimas 6 temporadas regulares (2017-18 a 2022-23). Ele pode ser encontrado em:

    - (https://github.com/ArthurPatricio/Final_Project_Basketball_Game_Prediction/blob/main/get_games.py)

* O script 'organize_data.py' tem os dados dados proveninetes dos 2 scripts anteriores e como suas entradas. Este script reorganiza os dados de forma que cada linha do dataframe seja única, contendo uma das partidas das últimas 6 temporadas regulares do conjunto. Colunas auxiliares foram craidas indicando o número do jogo dentro da temporada para cada time no confronto, por exemplo, um confronto pode uma partida entre de número 50 de um time A na temporada 2022-23 e a partida 48 de um time B que ele enfrenta neste confronto. 

* Os dados também foram trbalhados de forma que foram associados a cada confronto as médias estatísticas dos times. A associação é feita da seguinte forma, para cada confronto cada time recebe as sua médias estatísticas até o momento daquele jogo. Expandindo o exemplo anterior, no confronto entre os times A e B, A irá jogar sua partida de número 50, então chegara com as médias das 49 partidas anteriores a este jogo, já o time B, chegará com as médias das 47 partidas que já jogou na temporada. O script pode ser encontrado em:

    - (https://github.com/ArthurPatricio/Final_Project_Basketball_Game_Prediction/blob/main/organize_data.py)

* O último script, 'final_data.py', realiza a mesclagem final dos dados, unindo os confrontos às médias estatísticas do par de times até aquele momento (jogo) da temporada. Os dados são salvos em planilha, chamada 'nba_data.xlsx'. Ele pode ser encontrado em:

    - (https://github.com/ArthurPatricio/Final_Project_Basketball_Game_Prediction/blob/main/final_data.py)

# Linguagem, Bibliotecas e Pacotes

O trabalho foi feito todo em Python 3. Abaixo, segue a listagem de todas bibliotecas e pacotes utilizados:

    # Import libs

    import numpy as np
    import pandas as pd
    import missingno as msno
    from pandas_profiling import ProfileReport
    import matplotlib.pyplot as plt
    import seaborn as sns
    sns.set_theme(style="ticks")
    import plotly.express as px

    from sklearn.model_selection import train_test_split
    from sklearn.feature_selection import VarianceThreshold
    from sklearn import preprocessing
    from sklearn.preprocessing import LabelEncoder
    from keras import Sequential
    from keras.layers import Dense
    from tensorflow import keras
    from tensorflow.keras import layers
    from tensorflow.keras.utils import to_categorical
    from sklearn.preprocessing import StandardScaler
    from keras.callbacks import EarlyStopping, ReduceLROnPlateau, ModelCheckpoint
    import tensorflow as tf
    import tensorflow_addons as tfa

# Leitura dos Dados

A planilha 'nba_data.xlsx' foi importada e inserida em um Dataframe utilizando a biblioteca pandas.

# Read NBA data from excel file

    nba_data = pd.read_excel('nba_data.xlsx')

O dataframe tem a coluna 'Unnamed: 0' retirada.
# Drop "Unnamed: 0" column

    nba_data.drop(['Unnamed: 0'], axis=1, inplace=True)
# Análise Inicial

O dataset possui 6963 registros e 132 atributos.

    # Get nba_data dataframa shape

    nba_data.shape

    (6963, 132)

    # Get nba_data dataframe columns

    nba_data.columns

    Index(['HOME_TEAM_ID', 'HOME_TEAM_ABBREVIATION', 'HOME_GAME_ID',
       'HOME_MATCHUP', 'HOME_SEASON', 'HOME_GAME_N', 'HOME_WL', 'AWAY_TEAM_ID',
       'AWAY_TEAM_ABBREVIATION', 'AWAY_GAME_ID',
       ...
       'BLK_RANK_y', 'BLKA_RANK_y', 'PF_RANK_y', 'PFD_RANK_y', 'PTS_RANK_y',
       'PLUS_MINUS_RANK_y', 'GAME_DATE_y', 'SEASON_y', 'GAME_N_y',
       'COMPARE_y'],
      dtype='object', length=132)

      # Get nba_data dataframe describe

    nba_data.describe()

            HOME_TEAM_ID	HOME_GAME_ID	HOME_GAME_N	AWAY_TEAM_ID	AWAY_GAME_ID	AWAY_GAME_N	TEAM_ID_x	GP_x	W_x	L_x	...	AST_RANK_y	TOV_RANK_y	STL_RANK_y	BLK_RANK_y	BLKA_RANK_y	PF_RANK_y	PFD_RANK_y	PTS_RANK_y	PLUS_MINUS_RANK_y	GAME_N_y
    count	6.963000e+03	6.963000e+03	6963.000000	6.963000e+03	6.963000e+03	6963.000000	6.963000e+03	6963.000000	6963.000000	6963.000000	...	6963.000000	6963.000000	6963.000000	6963.000000	6963.000000	6963.000000	6963.000000	6963.000000	6963.000000	6963.000000
    mean	1.610613e+09	2.195075e+07	40.421657	1.610613e+09	2.195075e+07	40.431567	1.610613e+09	39.421657	19.688640	19.733017	...	15.345541	15.321844	15.419647	15.286514	15.244004	15.371248	15.439466	15.327876	15.286227	40.431567
    std	8.653343e+00	1.743568e+05	22.634354	8.640874e+00	1.743568e+05	22.614953	8.653343e+00	22.634354	13.039842	13.080083	...	8.664255	8.648501	8.662756	8.643116	8.639085	8.656732	8.616650	8.637555	8.633215	22.614953
    min	1.610613e+09	2.170002e+07	2.000000	1.610613e+09	2.170002e+07	2.000000	1.610613e+09	1.000000	0.000000	0.000000	...	1.000000	1.000000	1.000000	1.000000	1.000000	1.000000	1.000000	1.000000	1.000000	2.000000
    25%	1.610613e+09	2.180054e+07	21.000000	1.610613e+09	2.180054e+07	21.000000	1.610613e+09	20.000000	9.000000	9.000000	...	8.000000	8.000000	8.000000	8.000000	8.000000	8.000000	8.000000	8.000000	8.000000	21.000000
    50%	1.610613e+09	2.200003e+07	40.000000	1.610613e+09	2.200003e+07	40.000000	1.610613e+09	39.000000	18.000000	18.000000	...	15.000000	15.000000	15.000000	15.000000	15.000000	15.000000	16.000000	15.000000	15.000000	40.000000
    75%	1.610613e+09	2.210070e+07	60.000000	1.610613e+09	2.210070e+07	60.000000	1.610613e+09	59.000000	29.000000	29.000000	...	23.000000	23.000000	23.000000	23.000000	23.000000	23.000000	23.000000	23.000000	23.000000	60.000000
    max	1.610613e+09	2.220123e+07	82.000000	1.610613e+09	2.220123e+07	82.000000	1.610613e+09	81.000000	64.000000	64.000000	...	30.000000	30.000000	30.000000	30.000000	30.000000	30.000000	30.000000	30.000000	30.000000	82.000000
    8 rows × 114 columns

    # Get classes

    nba_data['HOME_WL'].value_counts()

    HOME_WL
    W    3936
    L    3027
    Name: count, dtype: int64

    # Get nba_data dataframe info

    nba_data.info()

# Chegagem de valores nulos

nba_data não possui nenhum valor faltante.

Foi utilizado a biblioteca missingno para realizar a checagem.

    msno.matrix(nba_data)

![msno_plot](https://github.com/ArthurPatricio/Final_Project_Basketball_Game_Prediction/blob/main/Images/msnoplot.png)

# Análise Exploratória

# 1. Vitórias e Derrotas por Time

    # Number of games per season

    nba_data['HOME_SEASON'].value_counts()

    HOME_SEASON
    2022-23    1214
    2021-22    1214
    2018-19    1214
    2017-18    1214
    2020-21    1064
    2019-20    1043
    Name: count, dtype: int64

Primeiramente, foram plotadas as vitórias e derrotas dos 10 times com melhor performance em jogos em casa nas últimas 6 temporadas apenas para termos uma visualização inicial dos nossos dados.

    # TEAMS PER HOME WINS/LOSSES BAR PLOT

    plt.figure(figsize=(20,12))
    fig11 = sns.countplot(data=nba_data, x=nba_data['HOME_TEAM_ABBREVIATION'],
                            palette = 'husl', 
                            hue = nba_data['HOME_WL'],
                            order=nba_data[nba_data['HOME_WL'] == 'W']['HOME_TEAM_ABBREVIATION'].value_counts().iloc[:10].index
                            )
    fig11.set_xlabel('WINS/LOSES', fontsize=20)
    fig11.set_ylabel('COUNT', fontsize=20)
    fig11.tick_params(labelsize=20)
    plt.title('HOME WINS/LOSES BY TEAM', fontsize = 20)
    for p in fig11.patches:
        txt = str(p.get_height().round(2))
        txt_x = p.get_x() 
        txt_y = p.get_height()
        fig11.text(txt_x,txt_y,txt)
    plt.show()

![home_win_losses_by_team](https://github.com/ArthurPatricio/Final_Project_Basketball_Game_Prediction/blob/main/Images/home_win_losses_by_team.png)

Também foram plotadas as vitórias e derrotas dos 10 times com melhor performance em jogos fora de casa nas últimas 6 temporadas apenas para termos uma visualização inicial dos nossos dados. 

    # TEAMS PER AWAY WINS/LOSSES BAR PLOT

    plt.figure(figsize=(20,12))
    fig2 = sns.countplot(data=nba_data, x=nba_data['AWAY_TEAM_ABBREVIATION'],
                            palette = 'husl', 
                            hue = nba_data['AWAY_WL'],
                            order=nba_data[nba_data['AWAY_WL'] == 'W']['AWAY_TEAM_ABBREVIATION'].value_counts().iloc[:10].index
                            )
    fig2.set_xlabel('WINS/LOSES', fontsize=20)
    fig2.set_ylabel('COUNT', fontsize=20)
    fig2.tick_params(labelsize=20)
    plt.title('AWAY WINS/LOSES BY TEAM', fontsize = 20)
    for p in fig2.patches:
        txt = str(p.get_height().round(2))
        txt_x = p.get_x() 
        txt_y = p.get_height()
        fig2.text(txt_x,txt_y,txt)
    plt.show()

![away_wins_losses_by_team](https://github.com/ArthurPatricio/Final_Project_Basketball_Game_Prediction/blob/main/Images/away_wins_losses_by_team.png)