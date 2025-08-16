
import pandas as pd
import gdown
import os

def download_if_not_exists(file_id, filename):
    url = f"https://drive.google.com/uc?id={file_id}"
    if not os.path.exists(filename):
        gdown.download(url, filename, quiet=False)
    return filename

def load_datasets():
    # Olympics dataset
    file_id1 = "1srKeo6cCOUqWlCtAexQSTF-05Oc_DC-v"
    olympics_file = download_if_not_exists(file_id1, "olympics.csv")
    df = pd.read_csv(olympics_file)

    # NOC regions dataset
    file_id2 = "1iUqj0VerynaLbbzbYRA8PlaWeBuDccnC"
    region_file = download_if_not_exists(file_id2, "noc_regions.csv")
    region_df = pd.read_csv(region_file)

    return df, region_df

# df = pd.read_csv('https://drive.google.com/uc?id=1srKeo6cCOUqWlCtAexQSTF-05Oc_DC-v')
# region_df = pd.read_csv('https://drive.google.com/uc?id=1iUqj0VerynaLbbzbYRA8PlaWeBuDccnC')


def preprocess(df,region_df):
    # filtering for summer olympics
    df = df[df['Season'] == 'Summer']
    # merge with region_df
    df = df.merge(region_df, on='NOC', how='left')
    # dropping duplicates
    df.drop_duplicates(inplace=True)
    # one hot encoding medals
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
    return df
