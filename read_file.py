import pathlib as path
import pandas as pd
import numpy as np

date_data = pd.read_csv(path.Path().joinpath('data', 'date_data.csv'))

print(date_data)

x_axis = np.linspace(1, 1, 100)
# %%
n_random = np.random.random((100, 100))
