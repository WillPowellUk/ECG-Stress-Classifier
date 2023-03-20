import pandas as pd
import os
import pickle

def progress_bar(current, total, bar_length=20):
    fraction = current / total

    arrow = int(fraction * bar_length - 1) * '-' + '>'
    padding = int(bar_length - len(arrow)) * ' '

    ending = '\n' if current == total else '\r'

    print(f'Progress: [{arrow}{padding}] {int(fraction*100)}%', end=ending)

def save_list_of_dataframes(df_list, folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    # save each dataframe as a CSV file in the folder
    for i, df in enumerate(df_list):
        filename = os.path.join(folder_path, f'df_{i}.csv')
        df.to_csv(filename, index=False)

    print("Dataframes saved as CSV files in folder:", folder_path)

def load_list_of_dataframes(folder_path):
    # initialize an empty list to hold the dataframes
    df_list = []

    try:
        # iterate over all files in the folder
        for filename in os.listdir(folder_path):
            if filename.endswith('.csv'):
                # read the CSV file into a dataframe and append to the list
                filepath = os.path.join(folder_path, filename)
                df = pd.read_csv(filepath)
                df_list.append(df)
    except FileNotFoundError:
        return False
    
    print(f"Using stored dataframe from {folder_path}")
    return df_list

def insert_dataframe(main_df, new_df):
    # get the index of the second to last column
    idx = len(main_df.columns) - 1

    # split the original dataframe into two parts
    df1 = main_df.iloc[:, :idx]
    df2 = main_df.iloc[:, idx:]

    # concatenate the two dataframes with the new dataframe in between
    return pd.concat([df1, new_df, df2], axis=1)
    

if __name__=='__main__':
    df1 = pd.DataFrame()
    df2 = pd.DataFrame()
    dfs = {}
    dfs[0] = df1
    dfs[1] = df2
    save_dataframe(dfs, 'Data/test.pkl')
    df = load_dataframe('Data/test.pkl')