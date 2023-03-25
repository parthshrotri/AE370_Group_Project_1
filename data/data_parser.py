import pandas as pd
import os
import numpy as np

filename = 'mars_trajectory'
for filename in os.listdir(os.path.join(os.path.dirname(__file__), 'text_files')):
    if filename.endswith('.txt'):
        print(filename)
        data = pd.read_csv(os.path.join(os.path.dirname(__file__), 'text_files', filename), sep=',')
        data = data.drop(columns=['JDTDB','Calendar Date (TDB)','Unnamed: 8'])
        data_numpy = data.to_numpy()
        np.save( os.path.join(os.path.dirname(__file__), 'npy_files',  filename[:-4]), data_numpy)
# data = pd.read_csv(os.path.join(os.path.dirname(__file__), filename + '.txt'), sep=',')
# print(data.head())
# print(data.columns[1])
# data = data.drop(columns=['JDTDB','Calendar Date (TDB)','Unnamed: 8'])
# print(data.head())
# print(data.tail())
# data_numpy = data.to_numpy()
# print(data_numpy)
# np.save( os.path.join(os.path.dirname(__file__), filename), data_numpy)