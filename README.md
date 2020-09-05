# Lambdata-mark
A collection of data science utility functions.

## Installation

```
pip install -i https://test.pypi.org/simple/ Lambdata-mark==0.0.1
```

## Usage

```
from my_lambdata.ds_utilities import enlarge

print(enlarge(5))

from my_lambdata.ds_utilities import address_column_split
df = pd.DataFrame({
        'Address': ['xxx Richardson, TX',
        'yyy Plano, TX',
        'xxyy Wylie, TX WO-65758',
        'zzz Waxahachie, TX WO-999786']})
    print(df.join(df['Address'].apply(lambda x: pd.Series(address_column_split(x), index=["City", "State"]))))
```
