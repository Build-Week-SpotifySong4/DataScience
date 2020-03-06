# ml_component/server/models.py
from ml_component.server import db  


class Song(db.Model):
    __tablename__ = "songs"
    id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String)
    track_id = db.Column(db.String)
    track_name = db.Column(db.String)
    acousticness = db.Column(db.Float)
    danceability = db.Column(db.Float)
    duration_ms = db.Column(db.Integer)
    energy = db.Column(db.Float)
    instrumentalness = db.Column(db.Float)
    key = db.Column(db.Integer)
    liveness = db.Column(db.Float)
    loudness = db.Column(db.Float)
    mode = db.Column(db.Integer)
    speechiness = db.Column(db.Float)
    tempo = db.Column(db.Float)
    time_signature = db.Column(db.Integer)
    valence = db.Column(db.Float)
    popularity = db.Column(db.Integer)

    def to_json(self):
        return {
            "id": self.id,
            "track_id": self.track_id, 
            "artist_name": self.artist_name,
            "track_name": self.track_name,
            "acousticness": self.acousticness,
            "danceability": self.danceability,
            "duration_ms": self.duration_ms,
            "energy": self.energy,
            "instrumentalness": self.instrumentalness,
            "key": self.key,
            "liveness": self.liveness,
            "loudness": self.loudness,
            "mode": self.mode,
            "speechiness": self.speechiness,
            "tempo": self.tempo,
            "time_signature": self.time_signature,
            "valence": self.valence,
            "popularity": self.popularity
        }
    
    def build_insert_query(self):
        """
        wow this is a mess,
        please update if you have a better method 
        to do so. 
        just ensure that the order is the same unless
        you want to add labels for each prior to the
        VALUES section of the query.
        """
        return '''
        INSERT INTO songs 
        (id, track_id, artist_name, track_name, acousticness, danceability, duration_ms, energy, instrumentalness, key, liveness, loudness, mode, speechiness, tempo, time_signature, valence, popularity)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        ''', (
            self.id,
            self.track_id, 
            self.artist_name,
            self.track_name,
            self.acousticness,
            self.danceability,
            self.duration_ms,
            self.energy,
            self.instrumentalness,
            self.key,
            self.liveness,
            self.loudness,
            self.mode,
            self.speechiness,
            self.tempo,
            self.time_signature,
            self.valence,
            self.popularity
        )