# Jesus Carlos Martinez Gonzalez
# 23/05/2023
# Song Artist

# We've given you a class called "Song" that represents
# some basic information about a song. We also wrote a
# class called "Artist" which contains some basic
# information about an artist.
#
# Your job is to create three instances of the song class,
# called song_1, song_2, and song_3.
#
# song_1 should have the following attributes:
#   name = "You Belong With Me"
#   album = "Fearless"
#   year = 2008
#   artist.name = "Taylor Swift"
#   artist.label = "Big Machine Records, LLC"
#
# song_2 should have the following attributes:
#   name = "All Too Well"
#   album = "Red"
#   year = 2012
#   artist.name = "Taylor Swift"
#   artist.label = "Big Machine Records, LLC"
#
# song_3 should have the following attributes:
#   name = "Up We Go"
#   album = "Midnight Machines"
#   year = 2016
#   artist.name = "LiGHTS"
#   artist.label = "Warner Bros. Records Inc."
#
# Notice, though, that song_1 and song_2 have the same
# artist and label. That means they should each have the
# SAME instance of artist: do not create separate instances
# of artist for each song.
#
# When your code is done running, there should exist three
# variables: song_1, song_2, and song_3, according to the
# requirements above.


class Artist:
    def __init__(self, name, label):
        self.name = name
        self.label = label


class Song:
    def __init__(self, name, album, year, artist):
        self.name = name
        self.album = album
        self.year = year
        self.artist = artist


def main():
    artist_1 = Artist("Taylor Swift", "Big Machine Records, LLC")
    artist_2 = Artist("LiGHTS", "Warner Bros. Records Inc.")

    song_1 = Song("You Belong With Me", "Fearless", 2008, artist_1)
    song_2 = Song("All Too Well", "Red", 2012, artist_1)
    song_3 = Song("Up We Go", "Midnight Machines", 2016, artist_2)


# Write a function called "get_song_string". It should accept
# one argument which will be a Song object. It should return
# a string in the following format:
#
# "<song name>" - <artist name> (<song year>)
# e.g:
# "You Belong With Me" - Taylor Swift (2008)
#
# The quotation marks around the song title should be *part*
# of the string.


def get_song_string(song):
    """Returns the song's name, that of the artist and its release year"""
    return f'"{song.name}" - {song.artist.name} ({song.year})'


if __name__ == "__main__":
    main()
