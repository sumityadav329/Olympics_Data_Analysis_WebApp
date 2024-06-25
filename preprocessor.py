import pandas as pd


def preprocess(df, region_df):
    
    # filetering  for summer olympics
    df = df[df['Season'] == 'Summer']
    # merging with region_df
    df = df.merge(region_df, on = 'NOC', how = 'left')
    # dropping duplicates
    df.drop_duplicates(inplace = True)
    # one hot encoding medals
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis = 1)
    return df