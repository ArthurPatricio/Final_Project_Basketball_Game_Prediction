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

### Predict NBA games results using AI

https://www.researchgate.net/publication/364954141_MambaNet_A_Hybrid_Neural_Network_for_Predicting_the_NBA_Playoffs

https://github.com/polleyethan/winners_and_whiners

https://devpost.com/software/applying-deep-learning-techniques-to-nba-predictions

https://www.google.com/search?q=sportradar&rlz=1C1YTUH_pt-PTBR1008BR1008&oq=sportradar&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDEzMzVqMGoxqAIAsAIA&sourceid=chrome&ie=UTF-8

https://ieeexplore.ieee.org/document/9746397