from keras.layers import SimpleRNN, Dense
from pandas.io.parsers import read_csv
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataframe = read_csv('한국에너지공단_자동차 연비표시제도_12_31_2020.csv', usecols= [5])
print(dataframe)