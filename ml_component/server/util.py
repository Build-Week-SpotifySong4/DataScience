# ml_component/server/util.py
from joblib import load
import pandas as pd 
import os
from dotenv import load_dotenv
load_dotenv()

import spotipy
# import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.oauth2 as oauth2


curr_dir = os.path.dirname(os.path.realpath(__file__))
model_path = 'lib/SpotifyKDTree.joblib'
scaled_path = 'lib/SpotifyScaled.joblib'
csv_path = 'lib/spotify_standardized.csv'

Spot_KDTree = load(os.path.join(curr_dir, model_path))
Spot_Scaled = load(os.path.join(curr_dir, scaled_path))
df_import = pd.read_csv(os.path.join(curr_dir, csv_path), index_col=0)

cid = os.getenv("spotify_cid")
secret = os.getenv("spotify_secret")
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)


def get_features(id):
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)    

    token = client_credentials_manager.get_access_token()

    feat = sp.audio_features(tracks=id)
    
    i = feat[0]
    feat_dict = {'danceability':i['danceability'], 'energy':i['energy'], 'key':i['key'], 'loudness':i['loudness'],                  
                 'mode':i['mode'], 'speechiness':i['speechiness'], 'acousticness':i['acousticness'],  
                 'instrumentalness':i['instrumentalness'], 'liveness':i['liveness'], 'valence':i['valence'],
                 'tempo':i['tempo'], 'time_signature':i['time_signature']}
    return(feat_dict)

def get_recommendations(id, k=11):
    feats = list(get_features(id).values())
    scaled_feats = Spot_Scaled.transform([feats])
    
    top_k_ind = Spot_KDTree.query(scaled_feats, k=k)[1][0,1:]
    
    top_k_id = df_import.iloc[top_k_ind].index.tolist()
    
    return top_k_id