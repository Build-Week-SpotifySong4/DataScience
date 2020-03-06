# etl_pipeline.py
from ml_component.server import db  
from ml_component.server.models import Song
import pandas as pd
import psycopg2
import sys
import os 
from dotenv import load_dotenv
load_dotenv()


def csv_to_postgres():
    print("Starting csv to postgres (all locally)...")
    DATA_PATH = "data/"
    file_name = "April2019.csv"

    df = pd.read_csv(DATA_PATH+file_name)
    assert(df.shape == (130663, 17))

    for row in df.values:
        curr_song = Song(
            artist_name=row[0],
            track_id=row[1],
            track_name=row[2],
            acousticness=row[3],
            danceability=row[4],
            duration_ms=row[5],
            energy=row[6],
            instrumentalness=row[7],
            key=row[8],
            liveness=row[9],
            loudness=row[10],
            mode=row[11],
            speechiness=row[12],
            tempo=row[13],
            time_signature=row[14],
            valence=row[15],
            popularity=row[16]
        )
        db.session.add(curr_song)
        db.session.commit()


    # sanity check 
    assert(len(Song.query.all()) == 130663)
    print("done.")


def postgres_to_postgres():
    print("Starting postgres to postgres (local to remote)...")
    songs = Song.query.all()
    conn = psycopg2.connect(
        dbname=os.getenv("remote_db_dbname"),
        user=os.getenv("remote_db_user"),
        password=os.getenv("remote_db_password"),
        host=os.getenv("remote_db_host")
    )
    curs = conn.cursor()
    # drop table to avoid duplication of songs
    drop_table = "DROP TABLE IF EXISTS songs;"
    curs.execute(drop_table)
    # create table 
    create_table = """
    CREATE TABLE songs (
        id SERIAL,
        artist_name TEXT,
        track_id TEXT,
        track_name TEXT,
        acousticness REAL,
        danceability REAL,
        duration_ms INT,
        energy REAL,
        instrumentalness REAL,
        key INT,
        liveness REAL,
        loudness REAL,
        mode INT,
        speechiness REAL,
        tempo REAL,
        time_signature INT,
        valence REAL,
        popularity INT
    );
    """
    curs.execute(create_table)
    # add every song to the deployed db
    for song in songs:
        curr_query_string, params = song.build_insert_query()
        print(curr_query_string)
        print(params)
        curs.execute(curr_query_string, params)
    conn.commit()
    # sanity check
    sanity_check = "SELECT COUNT(*) FROM songs"
    curs.execute(sanity_check)
    remote_song_count = curs.fetchone()
    local_song_count = len(songs)
    print(remote_song_count, local_song_count)
    assert(remote_song_count == local_song_count)
    print("done.")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Please add argv local or remote")
    elif sys.argv[1] == "local":
        csv_to_postgres()
    elif sys.argv[1] == "remote": 
        postgres_to_postgres()
    else:
        print("Argv must bee local or remote")