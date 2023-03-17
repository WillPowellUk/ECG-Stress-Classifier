import pandas as pd
import os
import pickle

def progress_bar(current, total, bar_length=20):
    fraction = current / total

    arrow = int(fraction * bar_length - 1) * '-' + '>'
    padding = int(bar_length - len(arrow)) * ' '

    ending = '\n' if current == total else '\r'

    print(f'Progress: [{arrow}{padding}] {int(fraction*100)}%', end=ending)

def save_dataframe(df, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "wb") as f:
        pickle.dump(df, f)
    print(f"Dataframe saved to {file_path}")

def load_dataframe(file_path):
    try:
        with open(file_path, 'rb') as f:
            df = pickle.load(f)
    except:
        return False
    print(f"Using stored dataframe from {file_path}")
    return df
    

if __name__=='__main__':
    df1 = pd.DataFrame()
    df2 = pd.DataFrame()
    dfs = {}
    dfs[0] = df1
    dfs[1] = df2
    save_dataframe(dfs, 'Data/test.pkl')
    df = load_dataframe('Data/test.pkl')