# Jesus Carlos Martinez Gonzalez
# 23/05/2023
# Song Artist

from song_artist import Song, Artist, get_song_string


def test_artist():
    artist = Artist("Some Name", "Some Label")
    assert artist.name == "Some Name"
    assert artist.label == "Some Label"


def test_song():
    artist = Artist("Some Name", "Some Label")
    song = Song("Some Song Title", "Some Album Title", 2000, artist)
    assert song.name == "Some Song Title"
    assert song.album == "Some Album Title"
    assert song.year == 2000


def test_get_song_string():
    artist = Artist("Some Name", "Some Label")
    song = Song("Some Song Title", "Some Album Title", 2000, artist)
    assert get_song_string(song) == '"Some Song Title" - Some Name (2000)'
