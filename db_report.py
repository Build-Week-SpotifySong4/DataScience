# db_report.py
# from ml_component.server import db 
from ml_component.server.models import Song
import sys 
import os 
import psycopg2


def local():
    print("DB REPORT (local):")
    songs = Song.query.all() 
    print(f"Song #: {len(songs)}")
    print(f"Example track_id: {songs[0].track_id}")


def remote():
    print("DB REPORT (remote):")
    conn = psycopg2.connect(
        dbname=os.getenv("remote_db_dbname"),
        user=os.getenv("remote_db_user"),
        password=os.getenv("remote_db_password"),
        host=os.getenv("remote_db_host")
    )
    curs = conn.cursor()
    song_count = "SELECT COUNT(*) FROM songs;"
    curs.execute(song_count)
    song_count = curs.fetchone()[0]
    print(f"Song #: {song_count}")
    # print(f"Example track_id: {songs[0].track_id}")

    curs.close()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Must have argument local or remote")
    elif sys.argv[1] == "local":
        local()
    elif sys.argv[1] == "remote":
        remote()
    else:
        print("Second argument must be local or remote.")