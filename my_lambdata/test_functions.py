from my_lambdata.ds_utilities import enlarge
import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_wine
from pdb import set_trace as breakpoint

print(enlarge(5))

from my_lambdata.ds_utilities import address_column_split
df = pd.DataFrame({
        'Address': ['xxx Richardson, TX',
        'yyy Plano, TX',
        'xxyy Wylie, TX WO-65758',
        'zzz Waxahachie, TX WO-999786']})
print(df.join(df['Address'].apply(lambda x: pd.Series(address_column_split(x), index=["City", "State"]))))