# ml_component/tests/test_db.py
import unittest 
from ml_component.server import db 
from ml_component.server.models import Song


class TestDB(unittest.TestCase):
    def test_song_count(self):
        songs = Song.query.all() 
        self.assertEqual(len(songs), 130663)
    
    def test_first_song(self):
        test_track_id = "2RM4jf1Xa9zPgMGRDiht8O"
        curr_song = Song.query.filter_by(track_id=test_track_id).first()
        test_track_name =  "Big Bank feat. 2 Chainz, Big Sean, Nicki Minaj"
        self.assertEqual(curr_song.track_name, test_track_name)