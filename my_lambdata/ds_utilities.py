import pandas as pd 
import numpy as np

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
    # print (enlarge(5))
    df = pd.DataFrame({
        'Address': ['xxx Richardson, TX',
        'yyy Plano, TX',
        'xxyy Wylie, TX WO-65758',
        'zzz Waxahachie, TX WO-999786']})
    print(df.join(df['Address'].apply(lambda x: pd.Series(address_column_split(x), index=["City", "State"]))))