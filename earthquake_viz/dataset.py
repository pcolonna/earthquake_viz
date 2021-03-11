import requests
import config
import pandas as pd 

def build():
    """Code to build the whole dataset"""
    data = get_data()
    df = build_lat_long_dataframe(data)

    return df

def get_data():
    url = config.base_url
    r = requests.get(url)

    # print(r.json())
    return r.json()


def build_lat_long_dataframe(data):

    
    rows_list = []

    for i, feature in enumerate(data['features']):
        d = {'longitude':  feature['geometry']['coordinates'][0], 'latitude': feature['geometry']['coordinates'][1]}
        rows_list.append(d)

    return pd.DataFrame(rows_list)
    
if __name__ == '__main__':
    data = get_data()
    df = build_lat_long_dataframe(data)

    print(df)

    # dg = pd.DataFrame(df['geometry'])
# 
    # print(dg)