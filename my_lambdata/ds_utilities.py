import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_wine
from pdb import set_trace as breakpoint

def enlarge(n):
    """
    Param n is a number
    Function will enlarge the number
    """
    return n * 100
# def date_column_split(df, date_column):
#     """
#     Splits a date into year, month and day columns

#     """
#     df[date_column] = pd.to_datetime(df[date_column], infer_datetime_format=True),
#     df['Year'] = df[date_column].dt.year
#     df['Month'] = df[date_column].dt.month
#     df['Day'] = df[date_column].dt.day
#     df.drop(date_column, axis=1, inplace=True)

#     return date
def address_column_split(a):
    """
    Extracts city and state in an address and provides separate columns for each
    """
    asplit = a.split(",")
    city = asplit[0].split()[-1]
    state = asplit[1].split()[0]
    return city, state
if __name__ == '__main__':
    df = pd.DataFrame({
        'Address': ['xxx Richardson, TX',
        'yyy Plano, TX',
        'xxyy Wylie, TX WO-65758',
        'zzz Waxahachie, TX WO-999786']})
    print(df.join(df['Address'].apply(lambda x: pd.Series(address_column_split(x), index=["City", "State"]))))

def train_validation_test_split(df, features, target,
                                train_size=0.7, val_size=0.1,
                                test_size=0.2, random_state=None,
                                shuffle=True):
        '''
        This function is a utility wrapper around the Scikit-Learn train_test_split that splits arrays or 
        matrices into train, validation, and test subsets.
        Args:
            df  (Pandas DataFrame): DataFrame with code
            X (list): A list of features.
            y (str): A string with target column.
            train_size (float or int): Proportion of the dataset to include in the train split (0 to 1).
            val_size (float or int): Proportion of the dataset to include in the validation split (0 to 1).
            test_size (float or int): Proportion of the dataset to include in the test split (0 to 1).
            random_state (int): Controls the shuffling applied to the data before applying the split for reproducibility.
            shuffle (bool): Whether or not to shuffle the data before splitting
        Returns:
            Train, test, and validation dataframes for features (X) and target (y). 
        '''

        X = df[features]
        y = df[target]

        X_train_val, X_test, y_train_val, y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state, shuffle=shuffle)
        X_train, X_val, y_train, y_val = train_test_split(
            X_train_val, y_train_val, test_size=val_size / (train_size + val_size),
            random_state=random_state, shuffle=shuffle)
        return X_train, X_val, X_test, y_train, y_val, y_test

if __name__ == '__main__':
    # print (enlarge(5))

    raw_data = load_wine()
    df = pd.DataFrame(data=raw_data['data'], columns=raw_data['feature_names'])
    df['target'] = raw_data['target']

    X_train, X_val, X_test, y_train, y_val, y_test = train_validation_test_split(df, features=['ash', 'hue'], target='target')

    breakpoint()